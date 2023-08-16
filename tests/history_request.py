#!/usr/bin/env python
# coding: utf-8
"""
Copyright 2023 Bloomberg Finance L.P.

Sample code provided by Bloomberg is made available for illustration
purposes only. Sample code is modifiable by individual users and is not
reviewed for reliability, accuracy and is not supported as part of any
Bloomberg service.  Users are solely responsible for the selection of and
use or intended use of the sample code, its applicability, accuracy and
adequacy, and the resultant output thereof. Sample code is proprietary and
confidential to Bloomberg and neither the recipient nor any of its
representatives may distribute, publish or display such code to any other
party, other than information disclosed to its employees on a need-to-know
basis in connection with the purpose for which such code was provided.
Sample code provided by Bloomberg is provided without any representations or
warranties and subject to modification by Bloomberg in its sole discretion.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
BLOOMBERG BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
# # Request a Timeseries of End-of-Day Values
#
# This sample creates a historical data request for a custom universe.
# See [README](../../../README.html) for more details.


################################################################################

import sys

sys.path.append('../src')

# - Import related libraries
import json
import os
import datetime
import logging
import pprint
import uuid
from urllib.parse import urljoin
from utils.bbgConnect import connect

################################################################################
# - Import module needed to authorize into BEAP service
#
from bwslib.bws_auth import download, handle_response

LOG = logging.getLogger(__name__)
HOST = 'https://api.bloomberg.com'

if __name__ == '__main__':

    SESSION, SSE_CLIENT = connect("credential.json")

    ############################################################################
    # - Discover catalog identifier for scheduling requests.
    catalogs_url = urljoin(HOST, '/eap/catalogs/')
    response = SESSION.get(catalogs_url)

    # Extract a/the account number from the response.
    handle_response(response)

    # We got back a good response. Let's extract our account number.
    catalogs = response.json()['contains']
    for catalog in catalogs:
        if catalog['subscriptionType'] == 'scheduled':
            # Take the catalog having "scheduled" subscription type,
            # which corresponds to the Data License account number.
            catalog_id = catalog['identifier']
            break
    else:
        # We exhausted the catalogs, but didn't find a non-'bbg' catalog.
        LOG.error('Scheduled catalog not in %r', response.json()['contains'])
        raise RuntimeError('Scheduled catalog not found')

    ############################################################################
    # - Construct the URL that will be the prefix for the other requests.
    account_url = urljoin(HOST, '/eap/catalogs/{c}/'.format(c=catalog_id))
    LOG.info("Scheduled catalog URL: %s", account_url)

    ############################################################################
    # # Request

    ############################################################################
    # - Create the request component.
    # Generate a timestamp and random ID so we can create unique component identifier.
    # NOTE The request_id must be 21 characters or less.
    request_id = 'r' + datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S') + str(uuid.uuid1())[:6]

    request_payload = {
        '@type': 'HistoryRequest',
        'identifier': request_id,
        'name': 'SampleHistoryRequest',
        'description': 'My favorite history request',
        'universe': {
            '@type': 'Universe',
            'contains': [
                {
                    '@type': 'Identifier',
                    'identifierType': 'ISIN',
                    'identifierValue': 'ARPCDB320099',  # CO26
                },
            ]
        },
        'fieldList': {
            '@type': 'HistoryFieldList',
            'contains': [
                {'mnemonic': 'ID_BB_UNIQUE'},
                {'mnemonic': 'PX_LAST'}
            ],
        },
        'trigger': {
            '@type': 'SubmitTrigger'
        },
        'runtimeOptions': {
            '@type': 'HistoryRuntimeOptions',
            'dateRange': {
                '@type': 'IntervalDateRange',
                'startDate': '2021-01-01',
                'endDate': '2023-05-01'
            },
            "period": "daily"
        },
        'formatting': {
            '@type': 'MediaType',
            'outputMediaType': 'application/json',
        }
    }

    LOG.info('Request component payload:\n%s', pprint.pformat(request_payload))

    requests_url = urljoin(account_url, 'requests/')
    response = SESSION.post(requests_url, json=request_payload)

    # Check it went well and extract the URL of the created request.
    handle_response(response)

    request_location = response.headers['Location']
    request_url = urljoin(HOST, request_location)

    LOG.info('%s resource has been successfully created at %s',
             request_id,
             request_url)

    ############################################################################
    # - Inspect the newly-created request component.
    SESSION.get(request_url)

    ############################################################################
    # ## Request outputs
    #
    # Once request was successfully created it is accepted to execution by the
    # HAPI service.
    # In order to detect the time of corresponding reply delivery the SSE
    # session is used.
    # Once reply is delivered this code will receive corresponding SSE
    # notification.

    ############################################################################
    # - Wait for notification that our output is ready for download. We allow a
    # reasonable amount of time for the request to be processed and avoid
    # waiting forever for the purposes of the sample code -- a timeout may not
    # apply to your actual business workflow. For larger requests or requests
    # made during periods of high load, you may need to increase the timeout.
    reply_timeout = datetime.timedelta(minutes=45)
    expiration_timestamp = datetime.datetime.utcnow() + reply_timeout
    while datetime.datetime.utcnow() < expiration_timestamp:
        # Read the next available event.
        event = SSE_CLIENT.read_event()

        if event.is_heartbeat():
            LOG.info('Received heartbeat event, keep waiting for events')
            continue

        LOG.info('Received reply delivery notification event: %s', event)
        event_data = json.loads(event.data)

        try:
            distribution = event_data['generated']
            reply_url = distribution['@id']
            distribution_id = distribution['identifier']

            dataset = distribution['snapshot']['dataset']
            dataset_id = dataset['identifier']

            catalog = dataset['catalog']
            reply_catalog_id = catalog['identifier']
        except KeyError:
            LOG.info("Received other event type, continue waiting")
        else:
            is_required_reply = request_id == dataset_id
            is_same_catalog = reply_catalog_id == catalog_id

            if not is_required_reply or not is_same_catalog:
                LOG.info("Some other delivery occurred - continue waiting")
                continue

            output_file_path = os.path.join('downloads', distribution_id)

            # Add 'Accept-Encoding: gzip' header to reduce download time.
            # Note that the vast majority of dataset files exceed 100MB in size,
            # so compression will speed up downloading significantly.
            headers = {'Accept-Encoding': 'gzip'}
            download_response = download(SESSION,
                                         reply_url,
                                         output_file_path,
                                         headers=headers)
            LOG.info('Reply was downloaded, exit now')
            break
    else:
        LOG.info('Reply NOT delivered, try to increase waiter loop timeout')