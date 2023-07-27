# coding: utf-8

"""
    DL REST API

    # Overview [DATA&lt;GO&gt;](https://data.bloomberg.com) and [DL REST API](https://api.bloomberg.com/eap) are the Web interfaces for the Bloomberg Data License Platform. The [Data License Platform Guide](https://data.bloomberg.com/docs/data-license/) provides a general overview of the platform and its capabilities. DL REST API is the REST API for the Bloomberg Data License Platform, which powers [DATA&lt;GO&gt;](https://data.bloomberg.com).  You can use [DL REST API](https://api.bloomberg.com/eap) to access any capability or data that is accessible through [DATA&lt;GO&gt;](https://data.bloomberg.com): For example, to automate the retrieval of bulk datasets and Bloomberg metadata or, to request, schedule and retrieve custom datasets using reusable resources.   # Getting Started To get started with DL REST API, you need to : * Register your application at https://console.bloomberg.com/ * Obtain a set of credentials for your application at https://console.bloomberg.com/ * Add your IP address to the allowlist for your application at https://console.bloomberg.com/ * Download sample code at https://developer.bloomberg.com/portal/downloads * Use the sample code to connect to the [entrypoint](#tag/entrypoint) at https://api.bloomberg.com/eap/ * Explore DATA&lt;GO&gt;, a WEB UI that is powered by DL REST API, to get familiar with DL REST API concepts. Login at https://data.bloomberg.com/  ## Authentication and Authorization Each request to DL REST API must include a [JSON Web Token (JWT)](https://jwt.io/) header, unique to and matching the request. The token must be signed with a valid Data License credential (see [sample code](#section/Getting-Started)). The Data License Platform verifies that the token corresponds to the endpoint being requested and is unique. The Platform also checks the credential used to sign the token, to verify access rights to the resource being requested.  Credentials and permitted IP address allowlists are managed through https://console.bloomberg.com/.  The credentials must be : 1. Issued by a Data License account with active Bloomberg Data License agreements. 2. Unexpired 3. Configured with a permitted IP allowlist entry for the address issuing the request.  DL REST API supports server mode Authentication Flow. Hybrid and device modes are not supported.  Navigate to [DL REST APIConsole > Develop > Developer Documentation > API References > Authentication & Authorization](https://console.bloomberg.com/) to learn more about DL REST API authentication. ## Version Headers Every request to DL REST API must include an `api-version` header (set to `api-version` to 2 for the version described by this specification).  This is the only supported value for `api-version`.  Requests that do not set the `api-version` header, and requests that provide an unsupported `api-version` header value will be rejected with a 400 response code. Response headers include a `latest-api-version` which returns the latest available version of the api. ## Search * Many collection endpoints provide search templates that can be used to query them, including full text search. These are provided using the [Hydra](https://www.hydra-cg.com/spec/latest/core/) [`search`](https://www.hydra-cg.com/spec/latest/core/#hydra:search) property. * Ordering of the returned results is controlled by the `sort` query parameter. * Other sort fields such as `title` can be used * The default sort order is ascending. If the sort field is prefixed with `-` it will return results in descending order, e.g. https://api.bloomberg.com/eap/catalogs/bbg/datasets/?sort=-title ## Pagination * Paging sequence bounds for paged collections will always be indicated with `first` and `last` links (either in the LDP-Paging headers or in the Hydra PartialCollectionView). * Within a paging sequence, a `next` link will be present on all pages except the last and a `prev` link will be present on all pages except the first, to aid sequential traversal. * Pages beyond the paging sequence bounds will return a response with an empty collection. * Pages beyond the paging sequence bounds will not have `next` or `prev` links. * Pages that support the `pageSize` query parameter permit a user defined `pageSize`. ## Redirects * `latest` represents the most recently created resource in a particular collection. It is currently applicable for the `snapshots` endpoints. Since \"latest\" changes meaning over time, this a convenience shortcut rather than a canonical resource. * While Bloomberg Data License makes every effort to maintain stable URLs, API users should receive and process HTTP redirect codes, and must specify a header to determine the version of the API to which they are coding (this document describes version 2) . ## Rate Limiting The number of requests is currently limited to 1000 requests per second per IP address, and 1200 requests per minute per application. An application in this context is defined as a [Bloomberg Enterprise Console Application](https://console.bloomberg.com/). Any request rate greater than this number will be rejected with an HTTP error code of `429`. ## Compression By default all datasets (excluding parquet archives which are already compact) are returned uncompressed. You can negotiate gzip compression by setting the \"Accept-Encoding\" request header to \"gzip\" as per [rfc2612](https://tools.ietf.org/html/rfc2616#section-14.3).  # New Features ## JSON Output You can now request DataRequest, BvalSnapshotRequest and PricingSnapshotRequest datasets in either JSON and CSV format.   ## Mnemonics in CSV and JSON You can now standardize all your workflows using mnemonics as field identifiers on input and output. CSV and JSON output is now available with mnemonics as field identifiers. Where you submit or schedule a request using previous (\"old\") mnemonics, the output file will return the mnemonics as you requested them, ensuring your workflow remains stable over time. You may continue to use clean names where you already do so, but Bloomberg recommends that where possible and compatible with your existing systems, new workflows are implemented using mnemonics rather than clean names, in both the `fieldList` and the `request` output format specification.  ## Bulk Format Fields A bulk format field defines a nested or embedded schema. Bloomberg represents rich content that cannot be encoded in a single scalar value using bulk format fields. Bulk Format fields are now available in JSON, CSV and Bloomberg file formats. See [here](https://developer.bloomberg.com/portal/documents/per_security/getting_started_with_rest_api/1185__distributions_and_file_formats#processing_bulk_fields) for more details to understand bulk format fields and how they are encoded in each of the file formats.  ## Inline Resources (Single POST Request) Implement a simple atomic request operation in your workflow: The DL REST API now allows you submit or schedule a per security request in a single HTTP POST that defines the universe, fieldlist and trigger, and submits or schedules the request for execution. Refer to the [sample code](https://developer.bloomberg.com/portal/downloads), or \"Inline Universe\", \"Inline FieldList\" and \"Inline Trigger\" properties in the [request POST](#operation/postRequest) section of this specification.   Re-usable resources continue to be fully supported for advanced workflows where you need to share universes or fieldlists.  ## Resource Deletion Manage the universes, fieldlists and triggers in your catalog: The DL REST API now supports archival of these resources, where they are not currently referenced by an active request. Remove resources with an HTTP DELETE, and retrieve or recover deleted resources through the [deleted `universe`](#operation/getDeletedUniverse), [deleted `fieldlist`](#operation/getDeletedFieldList), and [deleted `trigger`](#operation/getDeletedTrigger) endpoints.  Refer the sections in this specification on deleting a [`universe`](#operation/deleteUniverse), [`fieldlist`](#operation/deleteFieldList), or [`trigger`](#operation/deleteTrigger) for more information.  # Features ## Entity Data Requests Bloomberg's Entity Data provides legal entity data for public and private companies, funds, government agencies, and municipalities. You can request Entity Data through DL REST API by POSTing a resource of type EntityRequest to /catalogs/{catalog}/requests/. * Legal Entity Identifiers (LEI) are supported for Entity Requests. * Field lists are strongly typed to match the Entity Data request type. * Security level overrides are ignored by Entity Requests. ## CSV Output You can now request DataRequest and BvalSnapshotRequest datasets in a standard [CSV](https://www.ietf.org/rfc/rfc4180.txt) format. CSV output from DL REST API is normalized to [XSD 1.1 types](https://www.w3.org/TR/xmlschema11-2/) such as xsd:boolean and xsd:date to facilitate ingestion.\" ## History Archives DL REST API now offers parquet time-series archives for subscribers to Bulk History products. - The `archives` endpoint allows you to discover and request parquet \"archives\" representing a time-series of snapshots of a dataset. It supports bitemporal search by as-of snapshot dates and by as-at issued date-times). - `archives` are published in two different forms, so you can select a publication model to  meet your workflow needs. - The first publication model is intended for clients ingesting data into a data lake or data science platform: Download archives of status \"final\" and \"current\" (an archive becomes final when it reaches 1GB), replacing the most recent \"current\" archive each day in your system until this becomes \"final\". - The second model is designed to drive an ETL process feeding an ODS or data warehouse. Download \"ongoing\" daily parquet archives as they become available, appending the data to the data have already collected. - Since parquet is a compact format,  DL REST API does not further compress parquet archives, so downloads must set the `Accept-Encoding` header to `Identity`. ## Push Notifications To avoid polling the REST APIs for new distributions, DL REST API provides an API for receiving push notifications when `distributions` become available. We provide a [W3C Server Sent Event Stream](https://html.spec.whatwg.org/multipage/server-sent-events.html) to push notifications to connected clients over HTTP. Subscribe to the event stream at the [`/notifications/sse`](#tag/sse) endpoint to receive push notifications of `DistributionPublishedActivity` events for Bulk and Custom [`dataset`](#tag/dataset) publications immediately when they are available. ## BVAL Evaluated Pricing Bloomberg's BVAL evaluated pricing service provides accurate and defensible pricing of fixed income and derivatives instruments. If you are a subscriber to the BVAL service, you can request a BVAL Snapshot through DL REST API by POSTing a resource of type `BvalSnapshotRequest` to [/catalogs/{catalog}/requests/](#operation/postRequest). You can expect the response to be delivered according to the `snapshotTier` you select. You should expect a Tier 1 response within 45 minutes of the snapshot time, and a Tier 2 response within 3 hours. You can also request BVAL prices after the snapshot time, through a `DataRequest`, using the pricing sources indicated in the table below.  ### BVAL Snapshots  BVAL Snapshots are available at the following snapshot times and can be specified in a `BvalSnapshotRequest` or `DataRequest`. DL REST API provides a [push notification](#section/New-Features/Push-Notifications) immediately that the response is available.  New York Early Close pricing is available on SIFMA Recommended Early Close days. The New York 15:00 snapshot will run at 13:00, and the New York 16:00 at 14:00. Enabled clients will receive their datasets at earlier times if they follow the submission guidelines below. Please contact your BVAL Sales representative to get enabled for Early Close pricing.  |Snapshot Time|Snapshot Timezone|SIFMA Early Close Snapshot Time|T1 Request By|T2 Request By|T1 Response By|T2 Response By| | --- | --- | --- | --- | --- | --- | --- | |15:00|America/New_York|13:00|17:30|15:00|15:45|18:00| |16:00|America/New_York|14:00|18:30|16:00|16:45|19:00| |12:00|Europe/London| |14:30|12:00|12:45|15:00| |15:00|Europe/London| |17:30|15:00|15:45|18:00| |16:15|Europe/London| |18:45|16:15|17:00|19:15| |15:00|Asia/Tokyo| |17:30|15:00|15:45|18:00| |16:00|Asia/Tokyo| |18:30|16:00|16:45|19:00| |17:00|Asia/Tokyo| |19:30|17:00|17:45|20:00| |17:00|Asia/Shanghai| |19:30|17:00|17:45|20:00| |17:00|Australia/Sydney| |19:30|17:00|17:45|20:00|  BVAL snapshots are available up to a cutoff time: The cutoff time is defined as 2.5 hours after the snapshot for a Tier 1 Request, and the snapshot time itself for a Tier 2 request.  ### BVAL Pricing Source (PCS) Requests The following pricing sources can also be specified in a `DataRequest`.  |Pricing Source|Comments|Snapshot Time|Snapshot Timezone| | --- | --- | --- | --- | | BVN3 | | 15:00 | America/New_York | | BVN4 | | 16:00 | America/New_York | | BL12 | | 12:00 | Europe/London | | BLN3 | | 15:00 | Europe/London | | BLN4 | | 16:15 | Europe/London | | BVT3 | | 15:00 | Asia/Tokyo | | BVT4 | | 16:00 | Asia/Tokyo | | BVT5 | | 17:00 | Asia/Tokyo | | BSH5 | | 17:00 | Asia/Shanghai | | BVS5 | | 17:00 | Australia/Sydney | | BVAL | Latest available BVAL Evaluated Price. | latest | any | | BVIC | Latest available BVAL Index Convention Price |latest | any |  ## Pricing Snapshots Bloomberg's Pricing Snapshots provide a precise point in time snapshot of market prices for any instrument, available at 15 minute intervals throughout the day. You can request a Pricing Snapshot through DL REST API by POSTing a resource of type PricingSnapshotRequest to [/catalogs/{catalog}/requests/](#operation/postRequest) up to 15 minutes prior to the snapshot time. The response will be delivered shortly after the snapshot time, subject to an embargo period for the requested instruments (see [Exchange Delay](https://data.bloomberg.com/catalogs/bbg/fields/exchangeDelay/)). ## History Requests Request a historic time series over a specified date range and period through DL REST API by POSTing a resource of type `HistoryRequest` to [/catalogs/{catalog}/requests/](#operation/postRequest). - In DL REST API V2, fieldLists are strongly typed to match the request type. DL REST API V1 fieldLists are only supported for `requests` of type `DataRequest` - Security level overrides are ignored by history requests. ## Corporate Actions Requests Request current and future corporate actions through DL REST API by POSTing a resource of type `ActionsRequest` to [/catalogs/{catalog}/requests/](#operation/postRequest). - Request corporate actions that will become effective up to two years in the future or that were recorded by Bloomberg up to seven days prior to request execution. - Review the metadata at https://data.bloomberg.com/documents/actions/ to understand the layout and content of the dataset for an `ActionsRequest`. - Corporate action requests do not require a `FieldList` - all available actions for the security and for its issuer are returned. - Security level overrides are ignored by corporate actions requests. ## Parallel and Resumable Downloads DL REST API supports fast and resumable parallel downloads using the HTTP range requests. This capability is available for all [distributions](#operation/getDistribution), using gzip encoding (set Accept-Encoding to gzip). Refer to the sample code at https://service.bloomberg.com/ for an example of a parallel download from DL REST API using range headers. ## Show Subscribed Datasets Filter by datasets to which you have subscribed with query parameter `subscribed=true` when getting [/catalogs/bbg/datasets/](#operation/getDatasets). ## Extended Pagination Specify page size against supported endpoints with query parameter `pageSize`. ## Request References Where a resource is referenced by an active (scheduled) request, and updates to that resource are restricted, the boolean property `referencedByActiveRequests` will be set to `true`. ## Detailed Error messages Responses are now provided in [JSON-API](https://jsonapi.org/) response format, including an [RFC6901](https://tools.ietf.org/html/rfc6901) pointer to each section of the submitted document that could not be processed.  # API Specification This is the specification for the Bloomberg Data License DL REST API ([DL REST API](https://api.bloomberg.com/eap)).   # noqa: E501

    OpenAPI spec version: 2.8.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import io
import json
import logging
import re
import ssl

import certifi
# python 2 and python 3 compatibility library
import six
from six.moves.urllib.parse import urlencode

try:
    import urllib3
except ImportError:
    raise ImportError('Swagger python client requires urllib3.')


logger = logging.getLogger(__name__)


class RESTResponse(io.IOBase):

    def __init__(self, resp):
        self.urllib3_response = resp
        self.status = resp.status
        self.reason = resp.reason
        self.data = resp.data

    def getheaders(self):
        """Returns a dictionary of the response headers."""
        return self.urllib3_response.getheaders()

    def getheader(self, name, default=None):
        """Returns a given response header."""
        return self.urllib3_response.getheader(name, default)


class RESTClientObject(object):

    def __init__(self, configuration, pools_size=4, maxsize=None):
        # urllib3.PoolManager will pass all kw parameters to connectionpool
        # https://github.com/shazow/urllib3/blob/f9409436f83aeb79fbaf090181cd81b784f1b8ce/urllib3/poolmanager.py#L75  # noqa: E501
        # https://github.com/shazow/urllib3/blob/f9409436f83aeb79fbaf090181cd81b784f1b8ce/urllib3/connectionpool.py#L680  # noqa: E501
        # maxsize is the number of requests to host that are allowed in parallel  # noqa: E501
        # Custom SSL certificates and client certificates: http://urllib3.readthedocs.io/en/latest/advanced-usage.html  # noqa: E501

        # cert_reqs
        if configuration.verify_ssl:
            cert_reqs = ssl.CERT_REQUIRED
        else:
            cert_reqs = ssl.CERT_NONE

        # ca_certs
        if configuration.ssl_ca_cert:
            ca_certs = configuration.ssl_ca_cert
        else:
            # if not set certificate file, use Mozilla's root certificates.
            ca_certs = certifi.where()

        addition_pool_args = {}
        if configuration.assert_hostname is not None:
            addition_pool_args['assert_hostname'] = configuration.assert_hostname  # noqa: E501

        if maxsize is None:
            if configuration.connection_pool_maxsize is not None:
                maxsize = configuration.connection_pool_maxsize
            else:
                maxsize = 4

        # https pool manager
        if configuration.proxy:
            self.pool_manager = urllib3.ProxyManager(
                num_pools=pools_size,
                maxsize=maxsize,
                cert_reqs=cert_reqs,
                ca_certs=ca_certs,
                cert_file=configuration.cert_file,
                key_file=configuration.key_file,
                proxy_url=configuration.proxy,
                **addition_pool_args
            )
        else:
            self.pool_manager = urllib3.PoolManager(
                num_pools=pools_size,
                maxsize=maxsize,
                cert_reqs=cert_reqs,
                ca_certs=ca_certs,
                cert_file=configuration.cert_file,
                key_file=configuration.key_file,
                **addition_pool_args
            )

    def request(self, method, url, query_params=None, headers=None,
                body=None, post_params=None, _preload_content=True,
                _request_timeout=None):
        """Perform requests.

        :param method: http request method
        :param url: http request url
        :param query_params: query parameters in the url
        :param headers: http request headers
        :param body: request json body, for `application/json`
        :param post_params: request post parameters,
                            `application/x-www-form-urlencoded`
                            and `multipart/form-data`
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        """
        method = method.upper()
        assert method in ['GET', 'HEAD', 'DELETE', 'POST', 'PUT',
                          'PATCH', 'OPTIONS']

        if post_params and body:
            raise ValueError(
                "body parameter cannot be used with post_params parameter."
            )

        post_params = post_params or {}
        headers = headers or {}

        timeout = None
        if _request_timeout:
            if isinstance(_request_timeout, (int, ) if six.PY3 else (int, long)):  # noqa: E501,F821
                timeout = urllib3.Timeout(total=_request_timeout)
            elif (isinstance(_request_timeout, tuple) and
                  len(_request_timeout) == 2):
                timeout = urllib3.Timeout(
                    connect=_request_timeout[0], read=_request_timeout[1])

        if 'Content-Type' not in headers:
            headers['Content-Type'] = 'application/json'

        try:
            # For `POST`, `PUT`, `PATCH`, `OPTIONS`, `DELETE`
            if method in ['POST', 'PUT', 'PATCH', 'OPTIONS', 'DELETE']:
                if query_params:
                    url += '?' + urlencode(query_params)
                if re.search('json', headers['Content-Type'], re.IGNORECASE):
                    request_body = '{}'
                    if body is not None:
                        request_body = json.dumps(body)
                    r = self.pool_manager.request(
                        method, url,
                        body=request_body,
                        preload_content=_preload_content,
                        timeout=timeout,
                        headers=headers)
                elif headers['Content-Type'] == 'application/x-www-form-urlencoded':  # noqa: E501
                    r = self.pool_manager.request(
                        method, url,
                        fields=post_params,
                        encode_multipart=False,
                        preload_content=_preload_content,
                        timeout=timeout,
                        headers=headers)
                elif headers['Content-Type'] == 'multipart/form-data':
                    # must del headers['Content-Type'], or the correct
                    # Content-Type which generated by urllib3 will be
                    # overwritten.
                    del headers['Content-Type']
                    r = self.pool_manager.request(
                        method, url,
                        fields=post_params,
                        encode_multipart=True,
                        preload_content=_preload_content,
                        timeout=timeout,
                        headers=headers)
                # Pass a `string` parameter directly in the body to support
                # other content types than Json when `body` argument is
                # provided in serialized form
                elif isinstance(body, str):
                    request_body = body
                    r = self.pool_manager.request(
                        method, url,
                        body=request_body,
                        preload_content=_preload_content,
                        timeout=timeout,
                        headers=headers)
                else:
                    # Cannot generate the request from given parameters
                    msg = """Cannot prepare a request message for provided
                             arguments. Please check that your arguments match
                             declared content type."""
                    raise ApiException(status=0, reason=msg)
            # For `GET`, `HEAD`
            else:
                r = self.pool_manager.request(method, url,
                                              fields=query_params,
                                              preload_content=_preload_content,
                                              timeout=timeout,
                                              headers=headers)
        except urllib3.exceptions.SSLError as e:
            msg = "{0}\n{1}".format(type(e).__name__, str(e))
            raise ApiException(status=0, reason=msg)

        if _preload_content:
            r = RESTResponse(r)

            # log response body
            logger.debug("response body: %s", r.data)

        if not 200 <= r.status <= 299:
            raise ApiException(http_resp=r)

        return r

    def GET(self, url, headers=None, query_params=None, _preload_content=True,
            _request_timeout=None):
        return self.request("GET", url,
                            headers=headers,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            query_params=query_params)

    def HEAD(self, url, headers=None, query_params=None, _preload_content=True,
             _request_timeout=None):
        return self.request("HEAD", url,
                            headers=headers,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            query_params=query_params)

    def OPTIONS(self, url, headers=None, query_params=None, post_params=None,
                body=None, _preload_content=True, _request_timeout=None):
        return self.request("OPTIONS", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)

    def DELETE(self, url, headers=None, query_params=None, body=None,
               _preload_content=True, _request_timeout=None):
        return self.request("DELETE", url,
                            headers=headers,
                            query_params=query_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)

    def POST(self, url, headers=None, query_params=None, post_params=None,
             body=None, _preload_content=True, _request_timeout=None):
        return self.request("POST", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)

    def PUT(self, url, headers=None, query_params=None, post_params=None,
            body=None, _preload_content=True, _request_timeout=None):
        return self.request("PUT", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)

    def PATCH(self, url, headers=None, query_params=None, post_params=None,
              body=None, _preload_content=True, _request_timeout=None):
        return self.request("PATCH", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)


class ApiException(Exception):

    def __init__(self, status=None, reason=None, http_resp=None):
        if http_resp:
            self.status = http_resp.status
            self.reason = http_resp.reason
            self.body = http_resp.data
            self.headers = http_resp.getheaders()
        else:
            self.status = status
            self.reason = reason
            self.body = None
            self.headers = None

    def __str__(self):
        """Custom error messages for exception"""
        error_message = "({0})\n"\
                        "Reason: {1}\n".format(self.status, self.reason)
        if self.headers:
            error_message += "HTTP response headers: {0}\n".format(
                self.headers)

        if self.body:
            error_message += "HTTP response body: {0}\n".format(self.body)

        return error_message
