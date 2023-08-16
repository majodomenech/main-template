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
# # Simple Request for a Custom Dataset
#
# This sample shows how to create the simplest possible custom request that
# is processed on submission (an ad hoc request).
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
    # - Discover catalog identifier for scheduling requests
    catalogs_url = urljoin(HOST, '/eap/catalogs/')
    response = SESSION.get(catalogs_url)

    # Extract a/the account number from the response.
    handle_response(response)

    # We got back a good response. Let's extract our account number
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
    # # Request

    catalog_url = urljoin(HOST, '/eap/catalogs/bbg/fields/')
    # requests_url = urljoin(catalog_url,
    #                        '?page={page}'.format(page=1))
    requests_url = urljoin(catalog_url,"pxLast")

    response = SESSION.get(requests_url)

    # Check it went well and extract the URL of the created request.
    handle_response(response)

    print(response.text)
