# coding: utf-8

"""
    DL REST API

    # Overview [DATA&lt;GO&gt;](https://data.bloomberg.com) and [DL REST API](https://api.bloomberg.com/eap) are the Web interfaces for the Bloomberg Data License Platform. The [Data License Platform Guide](https://data.bloomberg.com/docs/data-license/) provides a general overview of the platform and its capabilities. DL REST API is the REST API for the Bloomberg Data License Platform, which powers [DATA&lt;GO&gt;](https://data.bloomberg.com).  You can use [DL REST API](https://api.bloomberg.com/eap) to access any capability or data that is accessible through [DATA&lt;GO&gt;](https://data.bloomberg.com): For example, to automate the retrieval of bulk datasets and Bloomberg metadata or, to request, schedule and retrieve custom datasets using reusable resources.   # Getting Started To get started with DL REST API, you need to : * Register your application at https://console.bloomberg.com/ * Obtain a set of credentials for your application at https://console.bloomberg.com/ * Add your IP address to the allowlist for your application at https://console.bloomberg.com/ * Download sample code at https://developer.bloomberg.com/portal/downloads * Use the sample code to connect to the [entrypoint](#tag/entrypoint) at https://api.bloomberg.com/eap/ * Explore DATA&lt;GO&gt;, a WEB UI that is powered by DL REST API, to get familiar with DL REST API concepts. Login at https://data.bloomberg.com/  ## Authentication and Authorization Each request to DL REST API must include a [JSON Web Token (JWT)](https://jwt.io/) header, unique to and matching the request. The token must be signed with a valid Data License credential (see [sample code](#section/Getting-Started)). The Data License Platform verifies that the token corresponds to the endpoint being requested and is unique. The Platform also checks the credential used to sign the token, to verify access rights to the resource being requested.  Credentials and permitted IP address allowlists are managed through https://console.bloomberg.com/.  The credentials must be : 1. Issued by a Data License account with active Bloomberg Data License agreements. 2. Unexpired 3. Configured with a permitted IP allowlist entry for the address issuing the request.  DL REST API supports server mode Authentication Flow. Hybrid and device modes are not supported.  Navigate to [DL REST APIConsole > Develop > Developer Documentation > API References > Authentication & Authorization](https://console.bloomberg.com/) to learn more about DL REST API authentication. ## Version Headers Every request to DL REST API must include an `api-version` header (set to `api-version` to 2 for the version described by this specification).  This is the only supported value for `api-version`.  Requests that do not set the `api-version` header, and requests that provide an unsupported `api-version` header value will be rejected with a 400 response code. Response headers include a `latest-api-version` which returns the latest available version of the api. ## Search * Many collection endpoints provide search templates that can be used to query them, including full text search. These are provided using the [Hydra](https://www.hydra-cg.com/spec/latest/core/) [`search`](https://www.hydra-cg.com/spec/latest/core/#hydra:search) property. * Ordering of the returned results is controlled by the `sort` query parameter. * Other sort fields such as `title` can be used * The default sort order is ascending. If the sort field is prefixed with `-` it will return results in descending order, e.g. https://api.bloomberg.com/eap/catalogs/bbg/datasets/?sort=-title ## Pagination * Paging sequence bounds for paged collections will always be indicated with `first` and `last` links (either in the LDP-Paging headers or in the Hydra PartialCollectionView). * Within a paging sequence, a `next` link will be present on all pages except the last and a `prev` link will be present on all pages except the first, to aid sequential traversal. * Pages beyond the paging sequence bounds will return a response with an empty collection. * Pages beyond the paging sequence bounds will not have `next` or `prev` links. * Pages that support the `pageSize` query parameter permit a user defined `pageSize`. ## Redirects * `latest` represents the most recently created resource in a particular collection. It is currently applicable for the `snapshots` endpoints. Since \"latest\" changes meaning over time, this a convenience shortcut rather than a canonical resource. * While Bloomberg Data License makes every effort to maintain stable URLs, API users should receive and process HTTP redirect codes, and must specify a header to determine the version of the API to which they are coding (this document describes version 2) . ## Rate Limiting The number of requests is currently limited to 1000 requests per second per IP address, and 1200 requests per minute per application. An application in this context is defined as a [Bloomberg Enterprise Console Application](https://console.bloomberg.com/). Any request rate greater than this number will be rejected with an HTTP error code of `429`. ## Compression By default all datasets (excluding parquet archives which are already compact) are returned uncompressed. You can negotiate gzip compression by setting the \"Accept-Encoding\" request header to \"gzip\" as per [rfc2612](https://tools.ietf.org/html/rfc2616#section-14.3).  # New Features ## JSON Output You can now request DataRequest, BvalSnapshotRequest and PricingSnapshotRequest datasets in either JSON and CSV format.   ## Mnemonics in CSV and JSON You can now standardize all your workflows using mnemonics as field identifiers on input and output. CSV and JSON output is now available with mnemonics as field identifiers. Where you submit or schedule a request using previous (\"old\") mnemonics, the output file will return the mnemonics as you requested them, ensuring your workflow remains stable over time. You may continue to use clean names where you already do so, but Bloomberg recommends that where possible and compatible with your existing systems, new workflows are implemented using mnemonics rather than clean names, in both the `fieldList` and the `request` output format specification.  ## Bulk Format Fields A bulk format field defines a nested or embedded schema. Bloomberg represents rich content that cannot be encoded in a single scalar value using bulk format fields. Bulk Format fields are now available in JSON, CSV and Bloomberg file formats. See [here](https://developer.bloomberg.com/portal/documents/per_security/getting_started_with_rest_api/1185__distributions_and_file_formats#processing_bulk_fields) for more details to understand bulk format fields and how they are encoded in each of the file formats.  ## Inline Resources (Single POST Request) Implement a simple atomic request operation in your workflow: The DL REST API now allows you submit or schedule a per security request in a single HTTP POST that defines the universe, fieldlist and trigger, and submits or schedules the request for execution. Refer to the [sample code](https://developer.bloomberg.com/portal/downloads), or \"Inline Universe\", \"Inline FieldList\" and \"Inline Trigger\" properties in the [request POST](#operation/postRequest) section of this specification.   Re-usable resources continue to be fully supported for advanced workflows where you need to share universes or fieldlists.  ## Resource Deletion Manage the universes, fieldlists and triggers in your catalog: The DL REST API now supports archival of these resources, where they are not currently referenced by an active request. Remove resources with an HTTP DELETE, and retrieve or recover deleted resources through the [deleted `universe`](#operation/getDeletedUniverse), [deleted `fieldlist`](#operation/getDeletedFieldList), and [deleted `trigger`](#operation/getDeletedTrigger) endpoints.  Refer the sections in this specification on deleting a [`universe`](#operation/deleteUniverse), [`fieldlist`](#operation/deleteFieldList), or [`trigger`](#operation/deleteTrigger) for more information.  # Features ## Entity Data Requests Bloomberg's Entity Data provides legal entity data for public and private companies, funds, government agencies, and municipalities. You can request Entity Data through DL REST API by POSTing a resource of type EntityRequest to /catalogs/{catalog}/requests/. * Legal Entity Identifiers (LEI) are supported for Entity Requests. * Field lists are strongly typed to match the Entity Data request type. * Security level overrides are ignored by Entity Requests. ## CSV Output You can now request DataRequest and BvalSnapshotRequest datasets in a standard [CSV](https://www.ietf.org/rfc/rfc4180.txt) format. CSV output from DL REST API is normalized to [XSD 1.1 types](https://www.w3.org/TR/xmlschema11-2/) such as xsd:boolean and xsd:date to facilitate ingestion.\" ## History Archives DL REST API now offers parquet time-series archives for subscribers to Bulk History products. - The `archives` endpoint allows you to discover and request parquet \"archives\" representing a time-series of snapshots of a dataset. It supports bitemporal search by as-of snapshot dates and by as-at issued date-times). - `archives` are published in two different forms, so you can select a publication model to  meet your workflow needs. - The first publication model is intended for clients ingesting data into a data lake or data science platform: Download archives of status \"final\" and \"current\" (an archive becomes final when it reaches 1GB), replacing the most recent \"current\" archive each day in your system until this becomes \"final\". - The second model is designed to drive an ETL process feeding an ODS or data warehouse. Download \"ongoing\" daily parquet archives as they become available, appending the data to the data have already collected. - Since parquet is a compact format,  DL REST API does not further compress parquet archives, so downloads must set the `Accept-Encoding` header to `Identity`. ## Push Notifications To avoid polling the REST APIs for new distributions, DL REST API provides an API for receiving push notifications when `distributions` become available. We provide a [W3C Server Sent Event Stream](https://html.spec.whatwg.org/multipage/server-sent-events.html) to push notifications to connected clients over HTTP. Subscribe to the event stream at the [`/notifications/sse`](#tag/sse) endpoint to receive push notifications of `DistributionPublishedActivity` events for Bulk and Custom [`dataset`](#tag/dataset) publications immediately when they are available. ## BVAL Evaluated Pricing Bloomberg's BVAL evaluated pricing service provides accurate and defensible pricing of fixed income and derivatives instruments. If you are a subscriber to the BVAL service, you can request a BVAL Snapshot through DL REST API by POSTing a resource of type `BvalSnapshotRequest` to [/catalogs/{catalog}/requests/](#operation/postRequest). You can expect the response to be delivered according to the `snapshotTier` you select. You should expect a Tier 1 response within 45 minutes of the snapshot time, and a Tier 2 response within 3 hours. You can also request BVAL prices after the snapshot time, through a `DataRequest`, using the pricing sources indicated in the table below.  ### BVAL Snapshots  BVAL Snapshots are available at the following snapshot times and can be specified in a `BvalSnapshotRequest` or `DataRequest`. DL REST API provides a [push notification](#section/New-Features/Push-Notifications) immediately that the response is available.  New York Early Close pricing is available on SIFMA Recommended Early Close days. The New York 15:00 snapshot will run at 13:00, and the New York 16:00 at 14:00. Enabled clients will receive their datasets at earlier times if they follow the submission guidelines below. Please contact your BVAL Sales representative to get enabled for Early Close pricing.  |Snapshot Time|Snapshot Timezone|SIFMA Early Close Snapshot Time|T1 Request By|T2 Request By|T1 Response By|T2 Response By| | --- | --- | --- | --- | --- | --- | --- | |15:00|America/New_York|13:00|17:30|15:00|15:45|18:00| |16:00|America/New_York|14:00|18:30|16:00|16:45|19:00| |12:00|Europe/London| |14:30|12:00|12:45|15:00| |15:00|Europe/London| |17:30|15:00|15:45|18:00| |16:15|Europe/London| |18:45|16:15|17:00|19:15| |15:00|Asia/Tokyo| |17:30|15:00|15:45|18:00| |16:00|Asia/Tokyo| |18:30|16:00|16:45|19:00| |17:00|Asia/Tokyo| |19:30|17:00|17:45|20:00| |17:00|Asia/Shanghai| |19:30|17:00|17:45|20:00| |17:00|Australia/Sydney| |19:30|17:00|17:45|20:00|  BVAL snapshots are available up to a cutoff time: The cutoff time is defined as 2.5 hours after the snapshot for a Tier 1 Request, and the snapshot time itself for a Tier 2 request.  ### BVAL Pricing Source (PCS) Requests The following pricing sources can also be specified in a `DataRequest`.  |Pricing Source|Comments|Snapshot Time|Snapshot Timezone| | --- | --- | --- | --- | | BVN3 | | 15:00 | America/New_York | | BVN4 | | 16:00 | America/New_York | | BL12 | | 12:00 | Europe/London | | BLN3 | | 15:00 | Europe/London | | BLN4 | | 16:15 | Europe/London | | BVT3 | | 15:00 | Asia/Tokyo | | BVT4 | | 16:00 | Asia/Tokyo | | BVT5 | | 17:00 | Asia/Tokyo | | BSH5 | | 17:00 | Asia/Shanghai | | BVS5 | | 17:00 | Australia/Sydney | | BVAL | Latest available BVAL Evaluated Price. | latest | any | | BVIC | Latest available BVAL Index Convention Price |latest | any |  ## Pricing Snapshots Bloomberg's Pricing Snapshots provide a precise point in time snapshot of market prices for any instrument, available at 15 minute intervals throughout the day. You can request a Pricing Snapshot through DL REST API by POSTing a resource of type PricingSnapshotRequest to [/catalogs/{catalog}/requests/](#operation/postRequest) up to 15 minutes prior to the snapshot time. The response will be delivered shortly after the snapshot time, subject to an embargo period for the requested instruments (see [Exchange Delay](https://data.bloomberg.com/catalogs/bbg/fields/exchangeDelay/)). ## History Requests Request a historic time series over a specified date range and period through DL REST API by POSTing a resource of type `HistoryRequest` to [/catalogs/{catalog}/requests/](#operation/postRequest). - In DL REST API V2, fieldLists are strongly typed to match the request type. DL REST API V1 fieldLists are only supported for `requests` of type `DataRequest` - Security level overrides are ignored by history requests. ## Corporate Actions Requests Request current and future corporate actions through DL REST API by POSTing a resource of type `ActionsRequest` to [/catalogs/{catalog}/requests/](#operation/postRequest). - Request corporate actions that will become effective up to two years in the future or that were recorded by Bloomberg up to seven days prior to request execution. - Review the metadata at https://data.bloomberg.com/documents/actions/ to understand the layout and content of the dataset for an `ActionsRequest`. - Corporate action requests do not require a `FieldList` - all available actions for the security and for its issuer are returned. - Security level overrides are ignored by corporate actions requests. ## Parallel and Resumable Downloads DL REST API supports fast and resumable parallel downloads using the HTTP range requests. This capability is available for all [distributions](#operation/getDistribution), using gzip encoding (set Accept-Encoding to gzip). Refer to the sample code at https://service.bloomberg.com/ for an example of a parallel download from DL REST API using range headers. ## Show Subscribed Datasets Filter by datasets to which you have subscribed with query parameter `subscribed=true` when getting [/catalogs/bbg/datasets/](#operation/getDatasets). ## Extended Pagination Specify page size against supported endpoints with query parameter `pageSize`. ## Request References Where a resource is referenced by an active (scheduled) request, and updates to that resource are restricted, the boolean property `referencedByActiveRequests` will be set to `true`. ## Detailed Error messages Responses are now provided in [JSON-API](https://jsonapi.org/) response format, including an [RFC6901](https://tools.ietf.org/html/rfc6901) pointer to each section of the submitted document that could not be processed.  # API Specification This is the specification for the Bloomberg Data License DL REST API ([DL REST API](https://api.bloomberg.com/eap)).   # noqa: E501

    OpenAPI spec version: 2.8.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from blapi.api_client import ApiClient


class MethodsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def catalogs_bbg_publishers_head(self, jwt, api_version, **kwargs):  # noqa: E501
        """Headers for a collection of Publisher resources  # noqa: E501

        Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.catalogs_bbg_publishers_head(jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.catalogs_bbg_publishers_head_with_http_info(jwt, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.catalogs_bbg_publishers_head_with_http_info(jwt, api_version, **kwargs)  # noqa: E501
            return data

    def catalogs_bbg_publishers_head_with_http_info(self, jwt, api_version, **kwargs):  # noqa: E501
        """Headers for a collection of Publisher resources  # noqa: E501

        Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.catalogs_bbg_publishers_head_with_http_info(jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['jwt', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method catalogs_bbg_publishers_head" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `catalogs_bbg_publishers_head`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `catalogs_bbg_publishers_head`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'jwt' in params:
            header_params['JWT'] = params['jwt']  # noqa: E501
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/catalogs/bbg/publishers/', 'HEAD',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def catalogs_bbg_publishers_options(self, jwt, api_version, **kwargs):  # noqa: E501
        """Options for a collection of Publisher resources  # noqa: E501

        Returns the methods that are supported by this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.catalogs_bbg_publishers_options(jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.catalogs_bbg_publishers_options_with_http_info(jwt, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.catalogs_bbg_publishers_options_with_http_info(jwt, api_version, **kwargs)  # noqa: E501
            return data

    def catalogs_bbg_publishers_options_with_http_info(self, jwt, api_version, **kwargs):  # noqa: E501
        """Options for a collection of Publisher resources  # noqa: E501

        Returns the methods that are supported by this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.catalogs_bbg_publishers_options_with_http_info(jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['jwt', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method catalogs_bbg_publishers_options" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `catalogs_bbg_publishers_options`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `catalogs_bbg_publishers_options`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'jwt' in params:
            header_params['JWT'] = params['jwt']  # noqa: E501
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/ld+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/catalogs/bbg/publishers/', 'OPTIONS',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def catalogs_bbg_publishers_publisher_name_head(self, publisher_name, jwt, api_version, **kwargs):  # noqa: E501
        """Headers for metadata for a publisher  # noqa: E501

        Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.catalogs_bbg_publishers_publisher_name_head(publisher_name, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str publisher_name: Publisher name (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.catalogs_bbg_publishers_publisher_name_head_with_http_info(publisher_name, jwt, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.catalogs_bbg_publishers_publisher_name_head_with_http_info(publisher_name, jwt, api_version, **kwargs)  # noqa: E501
            return data

    def catalogs_bbg_publishers_publisher_name_head_with_http_info(self, publisher_name, jwt, api_version, **kwargs):  # noqa: E501
        """Headers for metadata for a publisher  # noqa: E501

        Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.catalogs_bbg_publishers_publisher_name_head_with_http_info(publisher_name, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str publisher_name: Publisher name (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['publisher_name', 'jwt', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method catalogs_bbg_publishers_publisher_name_head" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'publisher_name' is set
        if ('publisher_name' not in params or
                params['publisher_name'] is None):
            raise ValueError("Missing the required parameter `publisher_name` when calling `catalogs_bbg_publishers_publisher_name_head`")  # noqa: E501
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `catalogs_bbg_publishers_publisher_name_head`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `catalogs_bbg_publishers_publisher_name_head`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'publisher_name' in params:
            path_params['publisherName'] = params['publisher_name']  # noqa: E501

        query_params = []

        header_params = {}
        if 'jwt' in params:
            header_params['JWT'] = params['jwt']  # noqa: E501
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/catalogs/bbg/publishers/{publisherName}/', 'HEAD',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def catalogs_bbg_publishers_publisher_name_options(self, publisher_name, jwt, api_version, **kwargs):  # noqa: E501
        """Options for metadata for a publisher  # noqa: E501

        Returns the methods that are supported by this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.catalogs_bbg_publishers_publisher_name_options(publisher_name, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str publisher_name: Publisher name (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.catalogs_bbg_publishers_publisher_name_options_with_http_info(publisher_name, jwt, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.catalogs_bbg_publishers_publisher_name_options_with_http_info(publisher_name, jwt, api_version, **kwargs)  # noqa: E501
            return data

    def catalogs_bbg_publishers_publisher_name_options_with_http_info(self, publisher_name, jwt, api_version, **kwargs):  # noqa: E501
        """Options for metadata for a publisher  # noqa: E501

        Returns the methods that are supported by this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.catalogs_bbg_publishers_publisher_name_options_with_http_info(publisher_name, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str publisher_name: Publisher name (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['publisher_name', 'jwt', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method catalogs_bbg_publishers_publisher_name_options" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'publisher_name' is set
        if ('publisher_name' not in params or
                params['publisher_name'] is None):
            raise ValueError("Missing the required parameter `publisher_name` when calling `catalogs_bbg_publishers_publisher_name_options`")  # noqa: E501
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `catalogs_bbg_publishers_publisher_name_options`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `catalogs_bbg_publishers_publisher_name_options`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'publisher_name' in params:
            path_params['publisherName'] = params['publisher_name']  # noqa: E501

        query_params = []

        header_params = {}
        if 'jwt' in params:
            header_params['JWT'] = params['jwt']  # noqa: E501
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/ld+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/catalogs/bbg/publishers/{publisherName}/', 'OPTIONS',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def head_archive(self, catalog, dataset, archive_name, jwt, api_version, **kwargs):  # noqa: E501
        """Headers for a downloadable historical file.  # noqa: E501

        Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_archive(catalog, dataset, archive_name, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str dataset: Dataset identifier (required)
        :param str archive_name: Archive name (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.head_archive_with_http_info(catalog, dataset, archive_name, jwt, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.head_archive_with_http_info(catalog, dataset, archive_name, jwt, api_version, **kwargs)  # noqa: E501
            return data

    def head_archive_with_http_info(self, catalog, dataset, archive_name, jwt, api_version, **kwargs):  # noqa: E501
        """Headers for a downloadable historical file.  # noqa: E501

        Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_archive_with_http_info(catalog, dataset, archive_name, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str dataset: Dataset identifier (required)
        :param str archive_name: Archive name (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['catalog', 'dataset', 'archive_name', 'jwt', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method head_archive" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog' is set
        if ('catalog' not in params or
                params['catalog'] is None):
            raise ValueError("Missing the required parameter `catalog` when calling `head_archive`")  # noqa: E501
        # verify the required parameter 'dataset' is set
        if ('dataset' not in params or
                params['dataset'] is None):
            raise ValueError("Missing the required parameter `dataset` when calling `head_archive`")  # noqa: E501
        # verify the required parameter 'archive_name' is set
        if ('archive_name' not in params or
                params['archive_name'] is None):
            raise ValueError("Missing the required parameter `archive_name` when calling `head_archive`")  # noqa: E501
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `head_archive`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `head_archive`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'catalog' in params:
            path_params['catalog'] = params['catalog']  # noqa: E501
        if 'dataset' in params:
            path_params['dataset'] = params['dataset']  # noqa: E501
        if 'archive_name' in params:
            path_params['archiveName'] = params['archive_name']  # noqa: E501

        query_params = []

        header_params = {}
        if 'jwt' in params:
            header_params['JWT'] = params['jwt']  # noqa: E501
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/catalogs/{catalog}/datasets/{dataset}/archives/{archiveName}', 'HEAD',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def head_archives(self, jwt, api_version, catalog, dataset, **kwargs):  # noqa: E501
        """Headers for collection of historical records.  # noqa: E501

        Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_archives(jwt, api_version, catalog, dataset, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str dataset: Dataset identifier (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.head_archives_with_http_info(jwt, api_version, catalog, dataset, **kwargs)  # noqa: E501
        else:
            (data) = self.head_archives_with_http_info(jwt, api_version, catalog, dataset, **kwargs)  # noqa: E501
            return data

    def head_archives_with_http_info(self, jwt, api_version, catalog, dataset, **kwargs):  # noqa: E501
        """Headers for collection of historical records.  # noqa: E501

        Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_archives_with_http_info(jwt, api_version, catalog, dataset, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str dataset: Dataset identifier (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['jwt', 'api_version', 'catalog', 'dataset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method head_archives" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `head_archives`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `head_archives`")  # noqa: E501
        # verify the required parameter 'catalog' is set
        if ('catalog' not in params or
                params['catalog'] is None):
            raise ValueError("Missing the required parameter `catalog` when calling `head_archives`")  # noqa: E501
        # verify the required parameter 'dataset' is set
        if ('dataset' not in params or
                params['dataset'] is None):
            raise ValueError("Missing the required parameter `dataset` when calling `head_archives`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'catalog' in params:
            path_params['catalog'] = params['catalog']  # noqa: E501
        if 'dataset' in params:
            path_params['dataset'] = params['dataset']  # noqa: E501

        query_params = []

        header_params = {}
        if 'jwt' in params:
            header_params['JWT'] = params['jwt']  # noqa: E501
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/catalogs/{catalog}/datasets/{dataset}/archives/', 'HEAD',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def head_catalog(self, jwt, api_version, catalog, **kwargs):  # noqa: E501
        """Headers for available data resources in this catalog  # noqa: E501

        Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_catalog(jwt, api_version, catalog, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.head_catalog_with_http_info(jwt, api_version, catalog, **kwargs)  # noqa: E501
        else:
            (data) = self.head_catalog_with_http_info(jwt, api_version, catalog, **kwargs)  # noqa: E501
            return data

    def head_catalog_with_http_info(self, jwt, api_version, catalog, **kwargs):  # noqa: E501
        """Headers for available data resources in this catalog  # noqa: E501

        Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_catalog_with_http_info(jwt, api_version, catalog, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['jwt', 'api_version', 'catalog']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method head_catalog" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `head_catalog`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `head_catalog`")  # noqa: E501
        # verify the required parameter 'catalog' is set
        if ('catalog' not in params or
                params['catalog'] is None):
            raise ValueError("Missing the required parameter `catalog` when calling `head_catalog`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'catalog' in params:
            path_params['catalog'] = params['catalog']  # noqa: E501

        query_params = []

        header_params = {}
        if 'jwt' in params:
            header_params['JWT'] = params['jwt']  # noqa: E501
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/catalogs/{catalog}/', 'HEAD',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def head_catalogs(self, jwt, api_version, **kwargs):  # noqa: E501
        """Headers for collection of available catalogs   # noqa: E501

        Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_catalogs(jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.head_catalogs_with_http_info(jwt, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.head_catalogs_with_http_info(jwt, api_version, **kwargs)  # noqa: E501
            return data

    def head_catalogs_with_http_info(self, jwt, api_version, **kwargs):  # noqa: E501
        """Headers for collection of available catalogs   # noqa: E501

        Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_catalogs_with_http_info(jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['jwt', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method head_catalogs" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `head_catalogs`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `head_catalogs`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'jwt' in params:
            header_params['JWT'] = params['jwt']  # noqa: E501
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/catalogs/', 'HEAD',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def head_dataset(self, jwt, api_version, catalog, dataset, **kwargs):  # noqa: E501
        """Headers for dataset definition and available snapshot resources  # noqa: E501

        Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_dataset(jwt, api_version, catalog, dataset, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str dataset: Dataset identifier (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.head_dataset_with_http_info(jwt, api_version, catalog, dataset, **kwargs)  # noqa: E501
        else:
            (data) = self.head_dataset_with_http_info(jwt, api_version, catalog, dataset, **kwargs)  # noqa: E501
            return data

    def head_dataset_with_http_info(self, jwt, api_version, catalog, dataset, **kwargs):  # noqa: E501
        """Headers for dataset definition and available snapshot resources  # noqa: E501

        Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_dataset_with_http_info(jwt, api_version, catalog, dataset, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str dataset: Dataset identifier (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['jwt', 'api_version', 'catalog', 'dataset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method head_dataset" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `head_dataset`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `head_dataset`")  # noqa: E501
        # verify the required parameter 'catalog' is set
        if ('catalog' not in params or
                params['catalog'] is None):
            raise ValueError("Missing the required parameter `catalog` when calling `head_dataset`")  # noqa: E501
        # verify the required parameter 'dataset' is set
        if ('dataset' not in params or
                params['dataset'] is None):
            raise ValueError("Missing the required parameter `dataset` when calling `head_dataset`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'catalog' in params:
            path_params['catalog'] = params['catalog']  # noqa: E501
        if 'dataset' in params:
            path_params['dataset'] = params['dataset']  # noqa: E501

        query_params = []

        header_params = {}
        if 'jwt' in params:
            header_params['JWT'] = params['jwt']  # noqa: E501
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/catalogs/{catalog}/datasets/{dataset}/', 'HEAD',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def head_datasets(self, catalog, jwt, api_version, **kwargs):  # noqa: E501
        """Headers for available datasets in this catalog  # noqa: E501

        Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_datasets(catalog, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param int page: Page number to view
        :param str q: Search terms. This is only applicable when catalog is `bbg`.
        :param bool subscribed: Subscription status. This is only applicable when catalog is `bbg`.
        :param str module_level1: Filter by module level 1. This is only applicable when catalog is `bbg`.
        :param str module_level2: Filter by module level 2. This is only applicable when catalog is `bbg`.
        :param str module_level3: Filter by module level 3. This is only applicable when catalog is `bbg`.
        :param str universe_label: Filter by universe label. This is only applicable when catalog is `bbg`.
        :param str universe_subset_label: Filter by universe subset label. This is only applicable when catalog is `bbg`.
        :param str publisher: Filter by the publisher. This is only applicable when catalog is `bbg`.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.head_datasets_with_http_info(catalog, jwt, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.head_datasets_with_http_info(catalog, jwt, api_version, **kwargs)  # noqa: E501
            return data

    def head_datasets_with_http_info(self, catalog, jwt, api_version, **kwargs):  # noqa: E501
        """Headers for available datasets in this catalog  # noqa: E501

        Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_datasets_with_http_info(catalog, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param int page: Page number to view
        :param str q: Search terms. This is only applicable when catalog is `bbg`.
        :param bool subscribed: Subscription status. This is only applicable when catalog is `bbg`.
        :param str module_level1: Filter by module level 1. This is only applicable when catalog is `bbg`.
        :param str module_level2: Filter by module level 2. This is only applicable when catalog is `bbg`.
        :param str module_level3: Filter by module level 3. This is only applicable when catalog is `bbg`.
        :param str universe_label: Filter by universe label. This is only applicable when catalog is `bbg`.
        :param str universe_subset_label: Filter by universe subset label. This is only applicable when catalog is `bbg`.
        :param str publisher: Filter by the publisher. This is only applicable when catalog is `bbg`.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['catalog', 'jwt', 'api_version', 'page', 'q', 'subscribed', 'module_level1', 'module_level2', 'module_level3', 'universe_label', 'universe_subset_label', 'publisher']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method head_datasets" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog' is set
        if ('catalog' not in params or
                params['catalog'] is None):
            raise ValueError("Missing the required parameter `catalog` when calling `head_datasets`")  # noqa: E501
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `head_datasets`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `head_datasets`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'catalog' in params:
            path_params['catalog'] = params['catalog']  # noqa: E501

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'q' in params:
            query_params.append(('q', params['q']))  # noqa: E501
        if 'subscribed' in params:
            query_params.append(('subscribed', params['subscribed']))  # noqa: E501
        if 'module_level1' in params:
            query_params.append(('moduleLevel1', params['module_level1']))  # noqa: E501
        if 'module_level2' in params:
            query_params.append(('moduleLevel2', params['module_level2']))  # noqa: E501
        if 'module_level3' in params:
            query_params.append(('moduleLevel3', params['module_level3']))  # noqa: E501
        if 'universe_label' in params:
            query_params.append(('universeLabel', params['universe_label']))  # noqa: E501
        if 'universe_subset_label' in params:
            query_params.append(('universeSubsetLabel', params['universe_subset_label']))  # noqa: E501
        if 'publisher' in params:
            query_params.append(('publisher', params['publisher']))  # noqa: E501

        header_params = {}
        if 'jwt' in params:
            header_params['JWT'] = params['jwt']  # noqa: E501
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/catalogs/{catalog}/datasets/', 'HEAD',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def head_distribution(self, catalog, dataset, snapshot, distribution_name, jwt, api_version, **kwargs):  # noqa: E501
        """Headers for a downloadable distribution of a snapshot  # noqa: E501

        Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_distribution(catalog, dataset, snapshot, distribution_name, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str dataset: Dataset identifier (required)
        :param str snapshot: Dataset snapshot identifier (required)
        :param str distribution_name: Distribution name (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.head_distribution_with_http_info(catalog, dataset, snapshot, distribution_name, jwt, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.head_distribution_with_http_info(catalog, dataset, snapshot, distribution_name, jwt, api_version, **kwargs)  # noqa: E501
            return data

    def head_distribution_with_http_info(self, catalog, dataset, snapshot, distribution_name, jwt, api_version, **kwargs):  # noqa: E501
        """Headers for a downloadable distribution of a snapshot  # noqa: E501

        Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_distribution_with_http_info(catalog, dataset, snapshot, distribution_name, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str dataset: Dataset identifier (required)
        :param str snapshot: Dataset snapshot identifier (required)
        :param str distribution_name: Distribution name (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['catalog', 'dataset', 'snapshot', 'distribution_name', 'jwt', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method head_distribution" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog' is set
        if ('catalog' not in params or
                params['catalog'] is None):
            raise ValueError("Missing the required parameter `catalog` when calling `head_distribution`")  # noqa: E501
        # verify the required parameter 'dataset' is set
        if ('dataset' not in params or
                params['dataset'] is None):
            raise ValueError("Missing the required parameter `dataset` when calling `head_distribution`")  # noqa: E501
        # verify the required parameter 'snapshot' is set
        if ('snapshot' not in params or
                params['snapshot'] is None):
            raise ValueError("Missing the required parameter `snapshot` when calling `head_distribution`")  # noqa: E501
        # verify the required parameter 'distribution_name' is set
        if ('distribution_name' not in params or
                params['distribution_name'] is None):
            raise ValueError("Missing the required parameter `distribution_name` when calling `head_distribution`")  # noqa: E501
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `head_distribution`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `head_distribution`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'catalog' in params:
            path_params['catalog'] = params['catalog']  # noqa: E501
        if 'dataset' in params:
            path_params['dataset'] = params['dataset']  # noqa: E501
        if 'snapshot' in params:
            path_params['snapshot'] = params['snapshot']  # noqa: E501
        if 'distribution_name' in params:
            path_params['distributionName'] = params['distribution_name']  # noqa: E501

        query_params = []

        header_params = {}
        if 'jwt' in params:
            header_params['JWT'] = params['jwt']  # noqa: E501
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/catalogs/{catalog}/datasets/{dataset}/snapshots/{snapshot}/distributions/{distributionName}', 'HEAD',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def head_distributions(self, catalog, dataset, snapshot, jwt, api_version, **kwargs):  # noqa: E501
        """Headers for list of available distributions of a snapshot  # noqa: E501

        Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_distributions(catalog, dataset, snapshot, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str dataset: Dataset identifier (required)
        :param str snapshot: Dataset snapshot identifier (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.head_distributions_with_http_info(catalog, dataset, snapshot, jwt, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.head_distributions_with_http_info(catalog, dataset, snapshot, jwt, api_version, **kwargs)  # noqa: E501
            return data

    def head_distributions_with_http_info(self, catalog, dataset, snapshot, jwt, api_version, **kwargs):  # noqa: E501
        """Headers for list of available distributions of a snapshot  # noqa: E501

        Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_distributions_with_http_info(catalog, dataset, snapshot, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str dataset: Dataset identifier (required)
        :param str snapshot: Dataset snapshot identifier (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['catalog', 'dataset', 'snapshot', 'jwt', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method head_distributions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog' is set
        if ('catalog' not in params or
                params['catalog'] is None):
            raise ValueError("Missing the required parameter `catalog` when calling `head_distributions`")  # noqa: E501
        # verify the required parameter 'dataset' is set
        if ('dataset' not in params or
                params['dataset'] is None):
            raise ValueError("Missing the required parameter `dataset` when calling `head_distributions`")  # noqa: E501
        # verify the required parameter 'snapshot' is set
        if ('snapshot' not in params or
                params['snapshot'] is None):
            raise ValueError("Missing the required parameter `snapshot` when calling `head_distributions`")  # noqa: E501
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `head_distributions`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `head_distributions`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'catalog' in params:
            path_params['catalog'] = params['catalog']  # noqa: E501
        if 'dataset' in params:
            path_params['dataset'] = params['dataset']  # noqa: E501
        if 'snapshot' in params:
            path_params['snapshot'] = params['snapshot']  # noqa: E501

        query_params = []

        header_params = {}
        if 'jwt' in params:
            header_params['JWT'] = params['jwt']  # noqa: E501
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/catalogs/{catalog}/datasets/{dataset}/snapshots/{snapshot}/distributions/', 'HEAD',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def head_field(self, jwt, api_version, field, **kwargs):  # noqa: E501
        """Headers for metadata describing a Bloomberg field  # noqa: E501

        Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_field(jwt, api_version, field, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param str field: Field identifier (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.head_field_with_http_info(jwt, api_version, field, **kwargs)  # noqa: E501
        else:
            (data) = self.head_field_with_http_info(jwt, api_version, field, **kwargs)  # noqa: E501
            return data

    def head_field_with_http_info(self, jwt, api_version, field, **kwargs):  # noqa: E501
        """Headers for metadata describing a Bloomberg field  # noqa: E501

        Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_field_with_http_info(jwt, api_version, field, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param str field: Field identifier (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['jwt', 'api_version', 'field']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method head_field" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `head_field`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `head_field`")  # noqa: E501
        # verify the required parameter 'field' is set
        if ('field' not in params or
                params['field'] is None):
            raise ValueError("Missing the required parameter `field` when calling `head_field`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'field' in params:
            path_params['field'] = params['field']  # noqa: E501

        query_params = []

        header_params = {}
        if 'jwt' in params:
            header_params['JWT'] = params['jwt']  # noqa: E501
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/catalogs/bbg/fields/{field}/', 'HEAD',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def head_field_list(self, catalog, field_list_name, jwt, api_version, **kwargs):  # noqa: E501
        """Headers for a field list  # noqa: E501

        Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_field_list(catalog, field_list_name, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str field_list_name: Field list name. (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.head_field_list_with_http_info(catalog, field_list_name, jwt, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.head_field_list_with_http_info(catalog, field_list_name, jwt, api_version, **kwargs)  # noqa: E501
            return data

    def head_field_list_with_http_info(self, catalog, field_list_name, jwt, api_version, **kwargs):  # noqa: E501
        """Headers for a field list  # noqa: E501

        Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_field_list_with_http_info(catalog, field_list_name, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str field_list_name: Field list name. (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['catalog', 'field_list_name', 'jwt', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method head_field_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog' is set
        if ('catalog' not in params or
                params['catalog'] is None):
            raise ValueError("Missing the required parameter `catalog` when calling `head_field_list`")  # noqa: E501
        # verify the required parameter 'field_list_name' is set
        if ('field_list_name' not in params or
                params['field_list_name'] is None):
            raise ValueError("Missing the required parameter `field_list_name` when calling `head_field_list`")  # noqa: E501
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `head_field_list`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `head_field_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'catalog' in params:
            path_params['catalog'] = params['catalog']  # noqa: E501
        if 'field_list_name' in params:
            path_params['fieldListName'] = params['field_list_name']  # noqa: E501

        query_params = []

        header_params = {}
        if 'jwt' in params:
            header_params['JWT'] = params['jwt']  # noqa: E501
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/catalogs/{catalog}/fieldLists/{fieldListName}/', 'HEAD',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def head_field_lists(self, catalog, jwt, api_version, **kwargs):  # noqa: E501
        """Headers for a collection of field lists  # noqa: E501

        Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_field_lists(catalog, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param int page: Page number to view
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.head_field_lists_with_http_info(catalog, jwt, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.head_field_lists_with_http_info(catalog, jwt, api_version, **kwargs)  # noqa: E501
            return data

    def head_field_lists_with_http_info(self, catalog, jwt, api_version, **kwargs):  # noqa: E501
        """Headers for a collection of field lists  # noqa: E501

        Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_field_lists_with_http_info(catalog, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param int page: Page number to view
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['catalog', 'jwt', 'api_version', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method head_field_lists" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog' is set
        if ('catalog' not in params or
                params['catalog'] is None):
            raise ValueError("Missing the required parameter `catalog` when calling `head_field_lists`")  # noqa: E501
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `head_field_lists`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `head_field_lists`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'catalog' in params:
            path_params['catalog'] = params['catalog']  # noqa: E501

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}
        if 'jwt' in params:
            header_params['JWT'] = params['jwt']  # noqa: E501
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/catalogs/{catalog}/fieldLists/', 'HEAD',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def head_fields(self, jwt, api_version, **kwargs):  # noqa: E501
        """Headers for list of all fields  # noqa: E501

        Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_fields(jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param int page: Page number to view
        :param str q: Search terms. This is only applicable when catalog is `bbg`.
        :param str dl_bulk: Filter by DL:Bulk. This is only applicable when catalog is `bbg`.
        :param str data_license: Filter by Data License. This is only applicable when catalog is `bbg`.
        :param str platform_static: Filter by Platform: Static. This is only applicable when catalog is `bbg`.
        :param str platform_streaming: Filter by Platform: Streaming. This is only applicable when catalog is `bbg`.
        :param str platform_terminal_required: Filter by Platform: Terminal Required. This is only applicable when catalog is `bbg`.
        :param str xsdtype: Filter by xsd:type. This is only applicable when catalog is `bbg`.
        :param str yk_commodity: Filter by the YK: Commodity. This is only applicable when catalog is `bbg`.
        :param str yk_corporate: Filter by the YK: Corporate. This is only applicable when catalog is `bbg`.
        :param str yk_currency: Filter by the YK: Currency. This is only applicable when catalog is `bbg`.
        :param str yk_equity: Filter by the YK: Equity. This is only applicable when catalog is `bbg`.
        :param str yk_index: Filter by the YK: Index. This is only applicable when catalog is `bbg`.
        :param str yk_mortgage: Filter by the YK: Mortgage. This is only applicable when catalog is `bbg`.
        :param str yk_money_market: Filter by the YK: Money Market. This is only applicable when catalog is `bbg`.
        :param str yk_municipal: Filter by the YK: Municipal. This is only applicable when catalog is `bbg`.
        :param str yk_preferred: Filter by the YK: Preferred. This is only applicable when catalog is `bbg`.
        :param str yk_us_government: Filter by the YK: US Government. This is only applicable when catalog is `bbg`.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.head_fields_with_http_info(jwt, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.head_fields_with_http_info(jwt, api_version, **kwargs)  # noqa: E501
            return data

    def head_fields_with_http_info(self, jwt, api_version, **kwargs):  # noqa: E501
        """Headers for list of all fields  # noqa: E501

        Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_fields_with_http_info(jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param int page: Page number to view
        :param str q: Search terms. This is only applicable when catalog is `bbg`.
        :param str dl_bulk: Filter by DL:Bulk. This is only applicable when catalog is `bbg`.
        :param str data_license: Filter by Data License. This is only applicable when catalog is `bbg`.
        :param str platform_static: Filter by Platform: Static. This is only applicable when catalog is `bbg`.
        :param str platform_streaming: Filter by Platform: Streaming. This is only applicable when catalog is `bbg`.
        :param str platform_terminal_required: Filter by Platform: Terminal Required. This is only applicable when catalog is `bbg`.
        :param str xsdtype: Filter by xsd:type. This is only applicable when catalog is `bbg`.
        :param str yk_commodity: Filter by the YK: Commodity. This is only applicable when catalog is `bbg`.
        :param str yk_corporate: Filter by the YK: Corporate. This is only applicable when catalog is `bbg`.
        :param str yk_currency: Filter by the YK: Currency. This is only applicable when catalog is `bbg`.
        :param str yk_equity: Filter by the YK: Equity. This is only applicable when catalog is `bbg`.
        :param str yk_index: Filter by the YK: Index. This is only applicable when catalog is `bbg`.
        :param str yk_mortgage: Filter by the YK: Mortgage. This is only applicable when catalog is `bbg`.
        :param str yk_money_market: Filter by the YK: Money Market. This is only applicable when catalog is `bbg`.
        :param str yk_municipal: Filter by the YK: Municipal. This is only applicable when catalog is `bbg`.
        :param str yk_preferred: Filter by the YK: Preferred. This is only applicable when catalog is `bbg`.
        :param str yk_us_government: Filter by the YK: US Government. This is only applicable when catalog is `bbg`.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['jwt', 'api_version', 'page', 'q', 'dl_bulk', 'data_license', 'platform_static', 'platform_streaming', 'platform_terminal_required', 'xsdtype', 'yk_commodity', 'yk_corporate', 'yk_currency', 'yk_equity', 'yk_index', 'yk_mortgage', 'yk_money_market', 'yk_municipal', 'yk_preferred', 'yk_us_government']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method head_fields" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `head_fields`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `head_fields`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'q' in params:
            query_params.append(('q', params['q']))  # noqa: E501
        if 'dl_bulk' in params:
            query_params.append(('DL:Bulk', params['dl_bulk']))  # noqa: E501
        if 'data_license' in params:
            query_params.append(('Data License', params['data_license']))  # noqa: E501
        if 'platform_static' in params:
            query_params.append(('Platform: Static', params['platform_static']))  # noqa: E501
        if 'platform_streaming' in params:
            query_params.append(('Platform: Streaming', params['platform_streaming']))  # noqa: E501
        if 'platform_terminal_required' in params:
            query_params.append(('Platform: Terminal Required', params['platform_terminal_required']))  # noqa: E501
        if 'xsdtype' in params:
            query_params.append(('xsd:type', params['xsdtype']))  # noqa: E501
        if 'yk_commodity' in params:
            query_params.append(('YK: Commodity', params['yk_commodity']))  # noqa: E501
        if 'yk_corporate' in params:
            query_params.append(('YK: Corporate', params['yk_corporate']))  # noqa: E501
        if 'yk_currency' in params:
            query_params.append(('YK: Currency', params['yk_currency']))  # noqa: E501
        if 'yk_equity' in params:
            query_params.append(('YK: Equity', params['yk_equity']))  # noqa: E501
        if 'yk_index' in params:
            query_params.append(('YK: Index', params['yk_index']))  # noqa: E501
        if 'yk_mortgage' in params:
            query_params.append(('YK: Mortgage', params['yk_mortgage']))  # noqa: E501
        if 'yk_money_market' in params:
            query_params.append(('YK: Money Market', params['yk_money_market']))  # noqa: E501
        if 'yk_municipal' in params:
            query_params.append(('YK: Municipal', params['yk_municipal']))  # noqa: E501
        if 'yk_preferred' in params:
            query_params.append(('YK: Preferred', params['yk_preferred']))  # noqa: E501
        if 'yk_us_government' in params:
            query_params.append(('YK: US Government', params['yk_us_government']))  # noqa: E501

        header_params = {}
        if 'jwt' in params:
            header_params['JWT'] = params['jwt']  # noqa: E501
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/catalogs/bbg/fields/', 'HEAD',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def head_ontology(self, jwt, api_version, **kwargs):  # noqa: E501
        """Headers for the DATA<GO> Ontology  # noqa: E501

        Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_ontology(jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.head_ontology_with_http_info(jwt, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.head_ontology_with_http_info(jwt, api_version, **kwargs)  # noqa: E501
            return data

    def head_ontology_with_http_info(self, jwt, api_version, **kwargs):  # noqa: E501
        """Headers for the DATA<GO> Ontology  # noqa: E501

        Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_ontology_with_http_info(jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['jwt', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method head_ontology" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `head_ontology`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `head_ontology`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'jwt' in params:
            header_params['JWT'] = params['jwt']  # noqa: E501
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/ontology', 'HEAD',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def head_request(self, catalog, request_name, jwt, api_version, **kwargs):  # noqa: E501
        """Headers for a request resource  # noqa: E501

        Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_request(catalog, request_name, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str request_name: Request name (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.head_request_with_http_info(catalog, request_name, jwt, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.head_request_with_http_info(catalog, request_name, jwt, api_version, **kwargs)  # noqa: E501
            return data

    def head_request_with_http_info(self, catalog, request_name, jwt, api_version, **kwargs):  # noqa: E501
        """Headers for a request resource  # noqa: E501

        Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_request_with_http_info(catalog, request_name, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str request_name: Request name (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['catalog', 'request_name', 'jwt', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method head_request" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog' is set
        if ('catalog' not in params or
                params['catalog'] is None):
            raise ValueError("Missing the required parameter `catalog` when calling `head_request`")  # noqa: E501
        # verify the required parameter 'request_name' is set
        if ('request_name' not in params or
                params['request_name'] is None):
            raise ValueError("Missing the required parameter `request_name` when calling `head_request`")  # noqa: E501
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `head_request`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `head_request`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'catalog' in params:
            path_params['catalog'] = params['catalog']  # noqa: E501
        if 'request_name' in params:
            path_params['requestName'] = params['request_name']  # noqa: E501

        query_params = []

        header_params = {}
        if 'jwt' in params:
            header_params['JWT'] = params['jwt']  # noqa: E501
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/catalogs/{catalog}/requests/{requestName}/', 'HEAD',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def head_request_field_list(self, catalog, request_name, jwt, api_version, **kwargs):  # noqa: E501
        """Headers for a field list resource  # noqa: E501

        Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_request_field_list(catalog, request_name, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str request_name: Request name (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param int page: Page number to view
        :param int page_size: Number of items per page. Defaults to 20 if not supplied.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.head_request_field_list_with_http_info(catalog, request_name, jwt, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.head_request_field_list_with_http_info(catalog, request_name, jwt, api_version, **kwargs)  # noqa: E501
            return data

    def head_request_field_list_with_http_info(self, catalog, request_name, jwt, api_version, **kwargs):  # noqa: E501
        """Headers for a field list resource  # noqa: E501

        Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_request_field_list_with_http_info(catalog, request_name, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str request_name: Request name (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param int page: Page number to view
        :param int page_size: Number of items per page. Defaults to 20 if not supplied.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['catalog', 'request_name', 'jwt', 'api_version', 'page', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method head_request_field_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog' is set
        if ('catalog' not in params or
                params['catalog'] is None):
            raise ValueError("Missing the required parameter `catalog` when calling `head_request_field_list`")  # noqa: E501
        # verify the required parameter 'request_name' is set
        if ('request_name' not in params or
                params['request_name'] is None):
            raise ValueError("Missing the required parameter `request_name` when calling `head_request_field_list`")  # noqa: E501
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `head_request_field_list`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `head_request_field_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'catalog' in params:
            path_params['catalog'] = params['catalog']  # noqa: E501
        if 'request_name' in params:
            path_params['requestName'] = params['request_name']  # noqa: E501

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501

        header_params = {}
        if 'jwt' in params:
            header_params['JWT'] = params['jwt']  # noqa: E501
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/catalogs/{catalog}/requests/{requestName}/fieldList/', 'HEAD',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def head_request_trigger(self, catalog, request_name, jwt, api_version, **kwargs):  # noqa: E501
        """Headers for a trigger resource  # noqa: E501

        Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_request_trigger(catalog, request_name, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str request_name: Request name (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.head_request_trigger_with_http_info(catalog, request_name, jwt, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.head_request_trigger_with_http_info(catalog, request_name, jwt, api_version, **kwargs)  # noqa: E501
            return data

    def head_request_trigger_with_http_info(self, catalog, request_name, jwt, api_version, **kwargs):  # noqa: E501
        """Headers for a trigger resource  # noqa: E501

        Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_request_trigger_with_http_info(catalog, request_name, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str request_name: Request name (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['catalog', 'request_name', 'jwt', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method head_request_trigger" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog' is set
        if ('catalog' not in params or
                params['catalog'] is None):
            raise ValueError("Missing the required parameter `catalog` when calling `head_request_trigger`")  # noqa: E501
        # verify the required parameter 'request_name' is set
        if ('request_name' not in params or
                params['request_name'] is None):
            raise ValueError("Missing the required parameter `request_name` when calling `head_request_trigger`")  # noqa: E501
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `head_request_trigger`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `head_request_trigger`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'catalog' in params:
            path_params['catalog'] = params['catalog']  # noqa: E501
        if 'request_name' in params:
            path_params['requestName'] = params['request_name']  # noqa: E501

        query_params = []

        header_params = {}
        if 'jwt' in params:
            header_params['JWT'] = params['jwt']  # noqa: E501
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/catalogs/{catalog}/requests/{requestName}/trigger/', 'HEAD',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def head_request_universe_list(self, catalog, request_name, jwt, api_version, **kwargs):  # noqa: E501
        """Headers for a universe resource  # noqa: E501

        Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_request_universe_list(catalog, request_name, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str request_name: Request name (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param int page: Page number to view
        :param int page_size: Number of items per page. Defaults to 20 if not supplied.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.head_request_universe_list_with_http_info(catalog, request_name, jwt, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.head_request_universe_list_with_http_info(catalog, request_name, jwt, api_version, **kwargs)  # noqa: E501
            return data

    def head_request_universe_list_with_http_info(self, catalog, request_name, jwt, api_version, **kwargs):  # noqa: E501
        """Headers for a universe resource  # noqa: E501

        Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_request_universe_list_with_http_info(catalog, request_name, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str request_name: Request name (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param int page: Page number to view
        :param int page_size: Number of items per page. Defaults to 20 if not supplied.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['catalog', 'request_name', 'jwt', 'api_version', 'page', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method head_request_universe_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog' is set
        if ('catalog' not in params or
                params['catalog'] is None):
            raise ValueError("Missing the required parameter `catalog` when calling `head_request_universe_list`")  # noqa: E501
        # verify the required parameter 'request_name' is set
        if ('request_name' not in params or
                params['request_name'] is None):
            raise ValueError("Missing the required parameter `request_name` when calling `head_request_universe_list`")  # noqa: E501
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `head_request_universe_list`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `head_request_universe_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'catalog' in params:
            path_params['catalog'] = params['catalog']  # noqa: E501
        if 'request_name' in params:
            path_params['requestName'] = params['request_name']  # noqa: E501

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501

        header_params = {}
        if 'jwt' in params:
            header_params['JWT'] = params['jwt']  # noqa: E501
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/catalogs/{catalog}/requests/{requestName}/universe/', 'HEAD',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def head_requests(self, catalog, jwt, api_version, **kwargs):  # noqa: E501
        """Headers for a collection of requests  # noqa: E501

        Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_requests(catalog, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param int page: Page number to view
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.head_requests_with_http_info(catalog, jwt, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.head_requests_with_http_info(catalog, jwt, api_version, **kwargs)  # noqa: E501
            return data

    def head_requests_with_http_info(self, catalog, jwt, api_version, **kwargs):  # noqa: E501
        """Headers for a collection of requests  # noqa: E501

        Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_requests_with_http_info(catalog, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param int page: Page number to view
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['catalog', 'jwt', 'api_version', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method head_requests" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog' is set
        if ('catalog' not in params or
                params['catalog'] is None):
            raise ValueError("Missing the required parameter `catalog` when calling `head_requests`")  # noqa: E501
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `head_requests`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `head_requests`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'catalog' in params:
            path_params['catalog'] = params['catalog']  # noqa: E501

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}
        if 'jwt' in params:
            header_params['JWT'] = params['jwt']  # noqa: E501
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/catalogs/{catalog}/requests/', 'HEAD',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def head_root(self, jwt, api_version, **kwargs):  # noqa: E501
        """Headers for entry point  # noqa: E501

        Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_root(jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.head_root_with_http_info(jwt, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.head_root_with_http_info(jwt, api_version, **kwargs)  # noqa: E501
            return data

    def head_root_with_http_info(self, jwt, api_version, **kwargs):  # noqa: E501
        """Headers for entry point  # noqa: E501

        Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_root_with_http_info(jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['jwt', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method head_root" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `head_root`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `head_root`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'jwt' in params:
            header_params['JWT'] = params['jwt']  # noqa: E501
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/', 'HEAD',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def head_snapshot(self, catalog, dataset, snapshot, jwt, api_version, **kwargs):  # noqa: E501
        """Headers for snapshot metadata and available distributions  # noqa: E501

        Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_snapshot(catalog, dataset, snapshot, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str dataset: Dataset identifier (required)
        :param str snapshot: Dataset snapshot identifier (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.head_snapshot_with_http_info(catalog, dataset, snapshot, jwt, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.head_snapshot_with_http_info(catalog, dataset, snapshot, jwt, api_version, **kwargs)  # noqa: E501
            return data

    def head_snapshot_with_http_info(self, catalog, dataset, snapshot, jwt, api_version, **kwargs):  # noqa: E501
        """Headers for snapshot metadata and available distributions  # noqa: E501

        Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_snapshot_with_http_info(catalog, dataset, snapshot, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str dataset: Dataset identifier (required)
        :param str snapshot: Dataset snapshot identifier (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['catalog', 'dataset', 'snapshot', 'jwt', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method head_snapshot" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog' is set
        if ('catalog' not in params or
                params['catalog'] is None):
            raise ValueError("Missing the required parameter `catalog` when calling `head_snapshot`")  # noqa: E501
        # verify the required parameter 'dataset' is set
        if ('dataset' not in params or
                params['dataset'] is None):
            raise ValueError("Missing the required parameter `dataset` when calling `head_snapshot`")  # noqa: E501
        # verify the required parameter 'snapshot' is set
        if ('snapshot' not in params or
                params['snapshot'] is None):
            raise ValueError("Missing the required parameter `snapshot` when calling `head_snapshot`")  # noqa: E501
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `head_snapshot`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `head_snapshot`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'catalog' in params:
            path_params['catalog'] = params['catalog']  # noqa: E501
        if 'dataset' in params:
            path_params['dataset'] = params['dataset']  # noqa: E501
        if 'snapshot' in params:
            path_params['snapshot'] = params['snapshot']  # noqa: E501

        query_params = []

        header_params = {}
        if 'jwt' in params:
            header_params['JWT'] = params['jwt']  # noqa: E501
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/catalogs/{catalog}/datasets/{dataset}/snapshots/{snapshot}/', 'HEAD',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def head_snapshots(self, catalog, dataset, jwt, api_version, **kwargs):  # noqa: E501
        """Headers for list of available snapshots for a dataset  # noqa: E501

        Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_snapshots(catalog, dataset, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str dataset: Dataset identifier (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param int page: Page number to view
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.head_snapshots_with_http_info(catalog, dataset, jwt, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.head_snapshots_with_http_info(catalog, dataset, jwt, api_version, **kwargs)  # noqa: E501
            return data

    def head_snapshots_with_http_info(self, catalog, dataset, jwt, api_version, **kwargs):  # noqa: E501
        """Headers for list of available snapshots for a dataset  # noqa: E501

        Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_snapshots_with_http_info(catalog, dataset, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str dataset: Dataset identifier (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param int page: Page number to view
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['catalog', 'dataset', 'jwt', 'api_version', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method head_snapshots" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog' is set
        if ('catalog' not in params or
                params['catalog'] is None):
            raise ValueError("Missing the required parameter `catalog` when calling `head_snapshots`")  # noqa: E501
        # verify the required parameter 'dataset' is set
        if ('dataset' not in params or
                params['dataset'] is None):
            raise ValueError("Missing the required parameter `dataset` when calling `head_snapshots`")  # noqa: E501
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `head_snapshots`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `head_snapshots`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'catalog' in params:
            path_params['catalog'] = params['catalog']  # noqa: E501
        if 'dataset' in params:
            path_params['dataset'] = params['dataset']  # noqa: E501

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}
        if 'jwt' in params:
            header_params['JWT'] = params['jwt']  # noqa: E501
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/catalogs/{catalog}/datasets/{dataset}/snapshots/', 'HEAD',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def head_trigger(self, catalog, trigger_name, jwt, api_version, **kwargs):  # noqa: E501
        """Headers for a trigger resource  # noqa: E501

        Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_trigger(catalog, trigger_name, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str trigger_name: Trigger name. (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.head_trigger_with_http_info(catalog, trigger_name, jwt, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.head_trigger_with_http_info(catalog, trigger_name, jwt, api_version, **kwargs)  # noqa: E501
            return data

    def head_trigger_with_http_info(self, catalog, trigger_name, jwt, api_version, **kwargs):  # noqa: E501
        """Headers for a trigger resource  # noqa: E501

        Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_trigger_with_http_info(catalog, trigger_name, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str trigger_name: Trigger name. (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['catalog', 'trigger_name', 'jwt', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method head_trigger" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog' is set
        if ('catalog' not in params or
                params['catalog'] is None):
            raise ValueError("Missing the required parameter `catalog` when calling `head_trigger`")  # noqa: E501
        # verify the required parameter 'trigger_name' is set
        if ('trigger_name' not in params or
                params['trigger_name'] is None):
            raise ValueError("Missing the required parameter `trigger_name` when calling `head_trigger`")  # noqa: E501
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `head_trigger`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `head_trigger`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'catalog' in params:
            path_params['catalog'] = params['catalog']  # noqa: E501
        if 'trigger_name' in params:
            path_params['triggerName'] = params['trigger_name']  # noqa: E501

        query_params = []

        header_params = {}
        if 'jwt' in params:
            header_params['JWT'] = params['jwt']  # noqa: E501
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/catalogs/{catalog}/triggers/{triggerName}/', 'HEAD',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def head_triggers(self, catalog, jwt, api_version, **kwargs):  # noqa: E501
        """Headers for a collection of triggers  # noqa: E501

        Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_triggers(catalog, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param int page: Page number to view
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.head_triggers_with_http_info(catalog, jwt, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.head_triggers_with_http_info(catalog, jwt, api_version, **kwargs)  # noqa: E501
            return data

    def head_triggers_with_http_info(self, catalog, jwt, api_version, **kwargs):  # noqa: E501
        """Headers for a collection of triggers  # noqa: E501

        Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_triggers_with_http_info(catalog, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param int page: Page number to view
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['catalog', 'jwt', 'api_version', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method head_triggers" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog' is set
        if ('catalog' not in params or
                params['catalog'] is None):
            raise ValueError("Missing the required parameter `catalog` when calling `head_triggers`")  # noqa: E501
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `head_triggers`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `head_triggers`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'catalog' in params:
            path_params['catalog'] = params['catalog']  # noqa: E501

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}
        if 'jwt' in params:
            header_params['JWT'] = params['jwt']  # noqa: E501
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/catalogs/{catalog}/triggers/', 'HEAD',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def head_universe(self, catalog, universe_name, jwt, api_version, **kwargs):  # noqa: E501
        """Headers for a universe resource  # noqa: E501

        Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_universe(catalog, universe_name, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str universe_name: Universe name. (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.head_universe_with_http_info(catalog, universe_name, jwt, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.head_universe_with_http_info(catalog, universe_name, jwt, api_version, **kwargs)  # noqa: E501
            return data

    def head_universe_with_http_info(self, catalog, universe_name, jwt, api_version, **kwargs):  # noqa: E501
        """Headers for a universe resource  # noqa: E501

        Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_universe_with_http_info(catalog, universe_name, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str universe_name: Universe name. (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['catalog', 'universe_name', 'jwt', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method head_universe" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog' is set
        if ('catalog' not in params or
                params['catalog'] is None):
            raise ValueError("Missing the required parameter `catalog` when calling `head_universe`")  # noqa: E501
        # verify the required parameter 'universe_name' is set
        if ('universe_name' not in params or
                params['universe_name'] is None):
            raise ValueError("Missing the required parameter `universe_name` when calling `head_universe`")  # noqa: E501
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `head_universe`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `head_universe`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'catalog' in params:
            path_params['catalog'] = params['catalog']  # noqa: E501
        if 'universe_name' in params:
            path_params['universeName'] = params['universe_name']  # noqa: E501

        query_params = []

        header_params = {}
        if 'jwt' in params:
            header_params['JWT'] = params['jwt']  # noqa: E501
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/catalogs/{catalog}/universes/{universeName}/', 'HEAD',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def head_universes(self, catalog, jwt, api_version, **kwargs):  # noqa: E501
        """Headers for a collection of universes  # noqa: E501

        Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_universes(catalog, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param int page: Page number to view
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.head_universes_with_http_info(catalog, jwt, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.head_universes_with_http_info(catalog, jwt, api_version, **kwargs)  # noqa: E501
            return data

    def head_universes_with_http_info(self, catalog, jwt, api_version, **kwargs):  # noqa: E501
        """Headers for a collection of universes  # noqa: E501

        Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.head_universes_with_http_info(catalog, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param int page: Page number to view
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['catalog', 'jwt', 'api_version', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method head_universes" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog' is set
        if ('catalog' not in params or
                params['catalog'] is None):
            raise ValueError("Missing the required parameter `catalog` when calling `head_universes`")  # noqa: E501
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `head_universes`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `head_universes`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'catalog' in params:
            path_params['catalog'] = params['catalog']  # noqa: E501

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}
        if 'jwt' in params:
            header_params['JWT'] = params['jwt']  # noqa: E501
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/catalogs/{catalog}/universes/', 'HEAD',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def options_archive(self, catalog, dataset, archive_name, jwt, api_version, **kwargs):  # noqa: E501
        """Options for a downloadable historical file.  # noqa: E501

        Returns the methods that are supported by this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_archive(catalog, dataset, archive_name, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str dataset: Dataset identifier (required)
        :param str archive_name: Archive name (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.options_archive_with_http_info(catalog, dataset, archive_name, jwt, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.options_archive_with_http_info(catalog, dataset, archive_name, jwt, api_version, **kwargs)  # noqa: E501
            return data

    def options_archive_with_http_info(self, catalog, dataset, archive_name, jwt, api_version, **kwargs):  # noqa: E501
        """Options for a downloadable historical file.  # noqa: E501

        Returns the methods that are supported by this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_archive_with_http_info(catalog, dataset, archive_name, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str dataset: Dataset identifier (required)
        :param str archive_name: Archive name (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['catalog', 'dataset', 'archive_name', 'jwt', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method options_archive" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog' is set
        if ('catalog' not in params or
                params['catalog'] is None):
            raise ValueError("Missing the required parameter `catalog` when calling `options_archive`")  # noqa: E501
        # verify the required parameter 'dataset' is set
        if ('dataset' not in params or
                params['dataset'] is None):
            raise ValueError("Missing the required parameter `dataset` when calling `options_archive`")  # noqa: E501
        # verify the required parameter 'archive_name' is set
        if ('archive_name' not in params or
                params['archive_name'] is None):
            raise ValueError("Missing the required parameter `archive_name` when calling `options_archive`")  # noqa: E501
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `options_archive`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `options_archive`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'catalog' in params:
            path_params['catalog'] = params['catalog']  # noqa: E501
        if 'dataset' in params:
            path_params['dataset'] = params['dataset']  # noqa: E501
        if 'archive_name' in params:
            path_params['archiveName'] = params['archive_name']  # noqa: E501

        query_params = []

        header_params = {}
        if 'jwt' in params:
            header_params['JWT'] = params['jwt']  # noqa: E501
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/ld+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/catalogs/{catalog}/datasets/{dataset}/archives/{archiveName}', 'OPTIONS',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def options_archives(self, jwt, api_version, catalog, dataset, **kwargs):  # noqa: E501
        """Options for dataset archive collection.  # noqa: E501

        Returns the methods that are supported by this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_archives(jwt, api_version, catalog, dataset, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str dataset: Dataset identifier (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.options_archives_with_http_info(jwt, api_version, catalog, dataset, **kwargs)  # noqa: E501
        else:
            (data) = self.options_archives_with_http_info(jwt, api_version, catalog, dataset, **kwargs)  # noqa: E501
            return data

    def options_archives_with_http_info(self, jwt, api_version, catalog, dataset, **kwargs):  # noqa: E501
        """Options for dataset archive collection.  # noqa: E501

        Returns the methods that are supported by this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_archives_with_http_info(jwt, api_version, catalog, dataset, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str dataset: Dataset identifier (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['jwt', 'api_version', 'catalog', 'dataset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method options_archives" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `options_archives`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `options_archives`")  # noqa: E501
        # verify the required parameter 'catalog' is set
        if ('catalog' not in params or
                params['catalog'] is None):
            raise ValueError("Missing the required parameter `catalog` when calling `options_archives`")  # noqa: E501
        # verify the required parameter 'dataset' is set
        if ('dataset' not in params or
                params['dataset'] is None):
            raise ValueError("Missing the required parameter `dataset` when calling `options_archives`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'catalog' in params:
            path_params['catalog'] = params['catalog']  # noqa: E501
        if 'dataset' in params:
            path_params['dataset'] = params['dataset']  # noqa: E501

        query_params = []

        header_params = {}
        if 'jwt' in params:
            header_params['JWT'] = params['jwt']  # noqa: E501
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/ld+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/catalogs/{catalog}/datasets/{dataset}/archives/', 'OPTIONS',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def options_catalog(self, jwt, api_version, catalog, **kwargs):  # noqa: E501
        """Options for data resources in this catalog  # noqa: E501

        Returns the methods that are supported by this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_catalog(jwt, api_version, catalog, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.options_catalog_with_http_info(jwt, api_version, catalog, **kwargs)  # noqa: E501
        else:
            (data) = self.options_catalog_with_http_info(jwt, api_version, catalog, **kwargs)  # noqa: E501
            return data

    def options_catalog_with_http_info(self, jwt, api_version, catalog, **kwargs):  # noqa: E501
        """Options for data resources in this catalog  # noqa: E501

        Returns the methods that are supported by this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_catalog_with_http_info(jwt, api_version, catalog, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['jwt', 'api_version', 'catalog']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method options_catalog" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `options_catalog`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `options_catalog`")  # noqa: E501
        # verify the required parameter 'catalog' is set
        if ('catalog' not in params or
                params['catalog'] is None):
            raise ValueError("Missing the required parameter `catalog` when calling `options_catalog`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'catalog' in params:
            path_params['catalog'] = params['catalog']  # noqa: E501

        query_params = []

        header_params = {}
        if 'jwt' in params:
            header_params['JWT'] = params['jwt']  # noqa: E501
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/ld+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/catalogs/{catalog}/', 'OPTIONS',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def options_catalogs(self, jwt, api_version, **kwargs):  # noqa: E501
        """Options for collection of available catalogs  # noqa: E501

        Returns the methods that are supported by this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_catalogs(jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.options_catalogs_with_http_info(jwt, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.options_catalogs_with_http_info(jwt, api_version, **kwargs)  # noqa: E501
            return data

    def options_catalogs_with_http_info(self, jwt, api_version, **kwargs):  # noqa: E501
        """Options for collection of available catalogs  # noqa: E501

        Returns the methods that are supported by this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_catalogs_with_http_info(jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['jwt', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method options_catalogs" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `options_catalogs`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `options_catalogs`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'jwt' in params:
            header_params['JWT'] = params['jwt']  # noqa: E501
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/ld+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/catalogs/', 'OPTIONS',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def options_dataset(self, jwt, api_version, catalog, dataset, **kwargs):  # noqa: E501
        """Options for dataset definition and available snapshot resources  # noqa: E501

        Returns the methods that are supported by this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_dataset(jwt, api_version, catalog, dataset, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str dataset: Dataset identifier (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.options_dataset_with_http_info(jwt, api_version, catalog, dataset, **kwargs)  # noqa: E501
        else:
            (data) = self.options_dataset_with_http_info(jwt, api_version, catalog, dataset, **kwargs)  # noqa: E501
            return data

    def options_dataset_with_http_info(self, jwt, api_version, catalog, dataset, **kwargs):  # noqa: E501
        """Options for dataset definition and available snapshot resources  # noqa: E501

        Returns the methods that are supported by this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_dataset_with_http_info(jwt, api_version, catalog, dataset, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str dataset: Dataset identifier (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['jwt', 'api_version', 'catalog', 'dataset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method options_dataset" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `options_dataset`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `options_dataset`")  # noqa: E501
        # verify the required parameter 'catalog' is set
        if ('catalog' not in params or
                params['catalog'] is None):
            raise ValueError("Missing the required parameter `catalog` when calling `options_dataset`")  # noqa: E501
        # verify the required parameter 'dataset' is set
        if ('dataset' not in params or
                params['dataset'] is None):
            raise ValueError("Missing the required parameter `dataset` when calling `options_dataset`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'catalog' in params:
            path_params['catalog'] = params['catalog']  # noqa: E501
        if 'dataset' in params:
            path_params['dataset'] = params['dataset']  # noqa: E501

        query_params = []

        header_params = {}
        if 'jwt' in params:
            header_params['JWT'] = params['jwt']  # noqa: E501
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/ld+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/catalogs/{catalog}/datasets/{dataset}/', 'OPTIONS',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def options_datasets(self, catalog, jwt, api_version, **kwargs):  # noqa: E501
        """Options for available datasets in this catalog  # noqa: E501

        Returns the methods that are supported by this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_datasets(catalog, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param int page: Page number to view
        :param str q: Search terms. This is only applicable when catalog is `bbg`.
        :param bool subscribed: Subscription status. This is only applicable when catalog is `bbg`.
        :param str module_level1: Filter by module level 1. This is only applicable when catalog is `bbg`.
        :param str module_level2: Filter by module level 2. This is only applicable when catalog is `bbg`.
        :param str module_level3: Filter by module level 3. This is only applicable when catalog is `bbg`.
        :param str universe_label: Filter by universe label. This is only applicable when catalog is `bbg`.
        :param str universe_subset_label: Filter by universe subset label. This is only applicable when catalog is `bbg`.
        :param str publisher: Filter by the publisher. This is only applicable when catalog is `bbg`.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.options_datasets_with_http_info(catalog, jwt, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.options_datasets_with_http_info(catalog, jwt, api_version, **kwargs)  # noqa: E501
            return data

    def options_datasets_with_http_info(self, catalog, jwt, api_version, **kwargs):  # noqa: E501
        """Options for available datasets in this catalog  # noqa: E501

        Returns the methods that are supported by this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_datasets_with_http_info(catalog, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param int page: Page number to view
        :param str q: Search terms. This is only applicable when catalog is `bbg`.
        :param bool subscribed: Subscription status. This is only applicable when catalog is `bbg`.
        :param str module_level1: Filter by module level 1. This is only applicable when catalog is `bbg`.
        :param str module_level2: Filter by module level 2. This is only applicable when catalog is `bbg`.
        :param str module_level3: Filter by module level 3. This is only applicable when catalog is `bbg`.
        :param str universe_label: Filter by universe label. This is only applicable when catalog is `bbg`.
        :param str universe_subset_label: Filter by universe subset label. This is only applicable when catalog is `bbg`.
        :param str publisher: Filter by the publisher. This is only applicable when catalog is `bbg`.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['catalog', 'jwt', 'api_version', 'page', 'q', 'subscribed', 'module_level1', 'module_level2', 'module_level3', 'universe_label', 'universe_subset_label', 'publisher']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method options_datasets" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog' is set
        if ('catalog' not in params or
                params['catalog'] is None):
            raise ValueError("Missing the required parameter `catalog` when calling `options_datasets`")  # noqa: E501
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `options_datasets`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `options_datasets`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'catalog' in params:
            path_params['catalog'] = params['catalog']  # noqa: E501

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'q' in params:
            query_params.append(('q', params['q']))  # noqa: E501
        if 'subscribed' in params:
            query_params.append(('subscribed', params['subscribed']))  # noqa: E501
        if 'module_level1' in params:
            query_params.append(('moduleLevel1', params['module_level1']))  # noqa: E501
        if 'module_level2' in params:
            query_params.append(('moduleLevel2', params['module_level2']))  # noqa: E501
        if 'module_level3' in params:
            query_params.append(('moduleLevel3', params['module_level3']))  # noqa: E501
        if 'universe_label' in params:
            query_params.append(('universeLabel', params['universe_label']))  # noqa: E501
        if 'universe_subset_label' in params:
            query_params.append(('universeSubsetLabel', params['universe_subset_label']))  # noqa: E501
        if 'publisher' in params:
            query_params.append(('publisher', params['publisher']))  # noqa: E501

        header_params = {}
        if 'jwt' in params:
            header_params['JWT'] = params['jwt']  # noqa: E501
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/ld+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/catalogs/{catalog}/datasets/', 'OPTIONS',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def options_distribution(self, catalog, dataset, snapshot, distribution_name, jwt, api_version, **kwargs):  # noqa: E501
        """Options for a downloadable distribution of a snapshot  # noqa: E501

        Returns the methods that are supported by this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_distribution(catalog, dataset, snapshot, distribution_name, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str dataset: Dataset identifier (required)
        :param str snapshot: Dataset snapshot identifier (required)
        :param str distribution_name: Distribution name (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.options_distribution_with_http_info(catalog, dataset, snapshot, distribution_name, jwt, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.options_distribution_with_http_info(catalog, dataset, snapshot, distribution_name, jwt, api_version, **kwargs)  # noqa: E501
            return data

    def options_distribution_with_http_info(self, catalog, dataset, snapshot, distribution_name, jwt, api_version, **kwargs):  # noqa: E501
        """Options for a downloadable distribution of a snapshot  # noqa: E501

        Returns the methods that are supported by this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_distribution_with_http_info(catalog, dataset, snapshot, distribution_name, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str dataset: Dataset identifier (required)
        :param str snapshot: Dataset snapshot identifier (required)
        :param str distribution_name: Distribution name (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['catalog', 'dataset', 'snapshot', 'distribution_name', 'jwt', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method options_distribution" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog' is set
        if ('catalog' not in params or
                params['catalog'] is None):
            raise ValueError("Missing the required parameter `catalog` when calling `options_distribution`")  # noqa: E501
        # verify the required parameter 'dataset' is set
        if ('dataset' not in params or
                params['dataset'] is None):
            raise ValueError("Missing the required parameter `dataset` when calling `options_distribution`")  # noqa: E501
        # verify the required parameter 'snapshot' is set
        if ('snapshot' not in params or
                params['snapshot'] is None):
            raise ValueError("Missing the required parameter `snapshot` when calling `options_distribution`")  # noqa: E501
        # verify the required parameter 'distribution_name' is set
        if ('distribution_name' not in params or
                params['distribution_name'] is None):
            raise ValueError("Missing the required parameter `distribution_name` when calling `options_distribution`")  # noqa: E501
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `options_distribution`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `options_distribution`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'catalog' in params:
            path_params['catalog'] = params['catalog']  # noqa: E501
        if 'dataset' in params:
            path_params['dataset'] = params['dataset']  # noqa: E501
        if 'snapshot' in params:
            path_params['snapshot'] = params['snapshot']  # noqa: E501
        if 'distribution_name' in params:
            path_params['distributionName'] = params['distribution_name']  # noqa: E501

        query_params = []

        header_params = {}
        if 'jwt' in params:
            header_params['JWT'] = params['jwt']  # noqa: E501
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/ld+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/catalogs/{catalog}/datasets/{dataset}/snapshots/{snapshot}/distributions/{distributionName}', 'OPTIONS',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def options_distributions(self, catalog, dataset, snapshot, jwt, api_version, **kwargs):  # noqa: E501
        """Options for list of available distributions of a snapshot  # noqa: E501

        Returns the methods that are supported by this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_distributions(catalog, dataset, snapshot, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str dataset: Dataset identifier (required)
        :param str snapshot: Dataset snapshot identifier (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.options_distributions_with_http_info(catalog, dataset, snapshot, jwt, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.options_distributions_with_http_info(catalog, dataset, snapshot, jwt, api_version, **kwargs)  # noqa: E501
            return data

    def options_distributions_with_http_info(self, catalog, dataset, snapshot, jwt, api_version, **kwargs):  # noqa: E501
        """Options for list of available distributions of a snapshot  # noqa: E501

        Returns the methods that are supported by this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_distributions_with_http_info(catalog, dataset, snapshot, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str dataset: Dataset identifier (required)
        :param str snapshot: Dataset snapshot identifier (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['catalog', 'dataset', 'snapshot', 'jwt', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method options_distributions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog' is set
        if ('catalog' not in params or
                params['catalog'] is None):
            raise ValueError("Missing the required parameter `catalog` when calling `options_distributions`")  # noqa: E501
        # verify the required parameter 'dataset' is set
        if ('dataset' not in params or
                params['dataset'] is None):
            raise ValueError("Missing the required parameter `dataset` when calling `options_distributions`")  # noqa: E501
        # verify the required parameter 'snapshot' is set
        if ('snapshot' not in params or
                params['snapshot'] is None):
            raise ValueError("Missing the required parameter `snapshot` when calling `options_distributions`")  # noqa: E501
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `options_distributions`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `options_distributions`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'catalog' in params:
            path_params['catalog'] = params['catalog']  # noqa: E501
        if 'dataset' in params:
            path_params['dataset'] = params['dataset']  # noqa: E501
        if 'snapshot' in params:
            path_params['snapshot'] = params['snapshot']  # noqa: E501

        query_params = []

        header_params = {}
        if 'jwt' in params:
            header_params['JWT'] = params['jwt']  # noqa: E501
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/ld+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/catalogs/{catalog}/datasets/{dataset}/snapshots/{snapshot}/distributions/', 'OPTIONS',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def options_field(self, jwt, api_version, field, **kwargs):  # noqa: E501
        """Options for metadata describing a Bloomberg field  # noqa: E501

        Returns the methods that are supported by this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_field(jwt, api_version, field, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param str field: Field identifier (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.options_field_with_http_info(jwt, api_version, field, **kwargs)  # noqa: E501
        else:
            (data) = self.options_field_with_http_info(jwt, api_version, field, **kwargs)  # noqa: E501
            return data

    def options_field_with_http_info(self, jwt, api_version, field, **kwargs):  # noqa: E501
        """Options for metadata describing a Bloomberg field  # noqa: E501

        Returns the methods that are supported by this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_field_with_http_info(jwt, api_version, field, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param str field: Field identifier (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['jwt', 'api_version', 'field']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method options_field" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `options_field`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `options_field`")  # noqa: E501
        # verify the required parameter 'field' is set
        if ('field' not in params or
                params['field'] is None):
            raise ValueError("Missing the required parameter `field` when calling `options_field`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'field' in params:
            path_params['field'] = params['field']  # noqa: E501

        query_params = []

        header_params = {}
        if 'jwt' in params:
            header_params['JWT'] = params['jwt']  # noqa: E501
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/ld+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/catalogs/bbg/fields/{field}/', 'OPTIONS',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def options_field_list(self, catalog, field_list_name, jwt, api_version, **kwargs):  # noqa: E501
        """Options for a field list resource  # noqa: E501

        Returns the methods that are supported by this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_field_list(catalog, field_list_name, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str field_list_name: Field list name. (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.options_field_list_with_http_info(catalog, field_list_name, jwt, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.options_field_list_with_http_info(catalog, field_list_name, jwt, api_version, **kwargs)  # noqa: E501
            return data

    def options_field_list_with_http_info(self, catalog, field_list_name, jwt, api_version, **kwargs):  # noqa: E501
        """Options for a field list resource  # noqa: E501

        Returns the methods that are supported by this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_field_list_with_http_info(catalog, field_list_name, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str field_list_name: Field list name. (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['catalog', 'field_list_name', 'jwt', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method options_field_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog' is set
        if ('catalog' not in params or
                params['catalog'] is None):
            raise ValueError("Missing the required parameter `catalog` when calling `options_field_list`")  # noqa: E501
        # verify the required parameter 'field_list_name' is set
        if ('field_list_name' not in params or
                params['field_list_name'] is None):
            raise ValueError("Missing the required parameter `field_list_name` when calling `options_field_list`")  # noqa: E501
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `options_field_list`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `options_field_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'catalog' in params:
            path_params['catalog'] = params['catalog']  # noqa: E501
        if 'field_list_name' in params:
            path_params['fieldListName'] = params['field_list_name']  # noqa: E501

        query_params = []

        header_params = {}
        if 'jwt' in params:
            header_params['JWT'] = params['jwt']  # noqa: E501
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/ld+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/catalogs/{catalog}/fieldLists/{fieldListName}/', 'OPTIONS',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def options_field_lists(self, catalog, jwt, api_version, **kwargs):  # noqa: E501
        """Options for a collection of field lists  # noqa: E501

        Returns the methods that are supported by this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_field_lists(catalog, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param int page: Page number to view
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.options_field_lists_with_http_info(catalog, jwt, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.options_field_lists_with_http_info(catalog, jwt, api_version, **kwargs)  # noqa: E501
            return data

    def options_field_lists_with_http_info(self, catalog, jwt, api_version, **kwargs):  # noqa: E501
        """Options for a collection of field lists  # noqa: E501

        Returns the methods that are supported by this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_field_lists_with_http_info(catalog, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param int page: Page number to view
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['catalog', 'jwt', 'api_version', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method options_field_lists" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog' is set
        if ('catalog' not in params or
                params['catalog'] is None):
            raise ValueError("Missing the required parameter `catalog` when calling `options_field_lists`")  # noqa: E501
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `options_field_lists`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `options_field_lists`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'catalog' in params:
            path_params['catalog'] = params['catalog']  # noqa: E501

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}
        if 'jwt' in params:
            header_params['JWT'] = params['jwt']  # noqa: E501
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/ld+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/catalogs/{catalog}/fieldLists/', 'OPTIONS',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def options_fields(self, jwt, api_version, **kwargs):  # noqa: E501
        """Options for list of all fields  # noqa: E501

        Returns the methods that are supported by this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_fields(jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param int page: Page number to view
        :param str q: Search terms. This is only applicable when catalog is `bbg`.
        :param str dl_bulk: Filter by DL:Bulk. This is only applicable when catalog is `bbg`.
        :param str data_license: Filter by Data License. This is only applicable when catalog is `bbg`.
        :param str platform_static: Filter by Platform: Static. This is only applicable when catalog is `bbg`.
        :param str platform_streaming: Filter by Platform: Streaming. This is only applicable when catalog is `bbg`.
        :param str platform_terminal_required: Filter by Platform: Terminal Required. This is only applicable when catalog is `bbg`.
        :param str xsdtype: Filter by xsd:type. This is only applicable when catalog is `bbg`.
        :param str yk_commodity: Filter by the YK: Commodity. This is only applicable when catalog is `bbg`.
        :param str yk_corporate: Filter by the YK: Corporate. This is only applicable when catalog is `bbg`.
        :param str yk_currency: Filter by the YK: Currency. This is only applicable when catalog is `bbg`.
        :param str yk_equity: Filter by the YK: Equity. This is only applicable when catalog is `bbg`.
        :param str yk_index: Filter by the YK: Index. This is only applicable when catalog is `bbg`.
        :param str yk_mortgage: Filter by the YK: Mortgage. This is only applicable when catalog is `bbg`.
        :param str yk_money_market: Filter by the YK: Money Market. This is only applicable when catalog is `bbg`.
        :param str yk_municipal: Filter by the YK: Municipal. This is only applicable when catalog is `bbg`.
        :param str yk_preferred: Filter by the YK: Preferred. This is only applicable when catalog is `bbg`.
        :param str yk_us_government: Filter by the YK: US Government. This is only applicable when catalog is `bbg`.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.options_fields_with_http_info(jwt, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.options_fields_with_http_info(jwt, api_version, **kwargs)  # noqa: E501
            return data

    def options_fields_with_http_info(self, jwt, api_version, **kwargs):  # noqa: E501
        """Options for list of all fields  # noqa: E501

        Returns the methods that are supported by this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_fields_with_http_info(jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param int page: Page number to view
        :param str q: Search terms. This is only applicable when catalog is `bbg`.
        :param str dl_bulk: Filter by DL:Bulk. This is only applicable when catalog is `bbg`.
        :param str data_license: Filter by Data License. This is only applicable when catalog is `bbg`.
        :param str platform_static: Filter by Platform: Static. This is only applicable when catalog is `bbg`.
        :param str platform_streaming: Filter by Platform: Streaming. This is only applicable when catalog is `bbg`.
        :param str platform_terminal_required: Filter by Platform: Terminal Required. This is only applicable when catalog is `bbg`.
        :param str xsdtype: Filter by xsd:type. This is only applicable when catalog is `bbg`.
        :param str yk_commodity: Filter by the YK: Commodity. This is only applicable when catalog is `bbg`.
        :param str yk_corporate: Filter by the YK: Corporate. This is only applicable when catalog is `bbg`.
        :param str yk_currency: Filter by the YK: Currency. This is only applicable when catalog is `bbg`.
        :param str yk_equity: Filter by the YK: Equity. This is only applicable when catalog is `bbg`.
        :param str yk_index: Filter by the YK: Index. This is only applicable when catalog is `bbg`.
        :param str yk_mortgage: Filter by the YK: Mortgage. This is only applicable when catalog is `bbg`.
        :param str yk_money_market: Filter by the YK: Money Market. This is only applicable when catalog is `bbg`.
        :param str yk_municipal: Filter by the YK: Municipal. This is only applicable when catalog is `bbg`.
        :param str yk_preferred: Filter by the YK: Preferred. This is only applicable when catalog is `bbg`.
        :param str yk_us_government: Filter by the YK: US Government. This is only applicable when catalog is `bbg`.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['jwt', 'api_version', 'page', 'q', 'dl_bulk', 'data_license', 'platform_static', 'platform_streaming', 'platform_terminal_required', 'xsdtype', 'yk_commodity', 'yk_corporate', 'yk_currency', 'yk_equity', 'yk_index', 'yk_mortgage', 'yk_money_market', 'yk_municipal', 'yk_preferred', 'yk_us_government']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method options_fields" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `options_fields`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `options_fields`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'q' in params:
            query_params.append(('q', params['q']))  # noqa: E501
        if 'dl_bulk' in params:
            query_params.append(('DL:Bulk', params['dl_bulk']))  # noqa: E501
        if 'data_license' in params:
            query_params.append(('Data License', params['data_license']))  # noqa: E501
        if 'platform_static' in params:
            query_params.append(('Platform: Static', params['platform_static']))  # noqa: E501
        if 'platform_streaming' in params:
            query_params.append(('Platform: Streaming', params['platform_streaming']))  # noqa: E501
        if 'platform_terminal_required' in params:
            query_params.append(('Platform: Terminal Required', params['platform_terminal_required']))  # noqa: E501
        if 'xsdtype' in params:
            query_params.append(('xsd:type', params['xsdtype']))  # noqa: E501
        if 'yk_commodity' in params:
            query_params.append(('YK: Commodity', params['yk_commodity']))  # noqa: E501
        if 'yk_corporate' in params:
            query_params.append(('YK: Corporate', params['yk_corporate']))  # noqa: E501
        if 'yk_currency' in params:
            query_params.append(('YK: Currency', params['yk_currency']))  # noqa: E501
        if 'yk_equity' in params:
            query_params.append(('YK: Equity', params['yk_equity']))  # noqa: E501
        if 'yk_index' in params:
            query_params.append(('YK: Index', params['yk_index']))  # noqa: E501
        if 'yk_mortgage' in params:
            query_params.append(('YK: Mortgage', params['yk_mortgage']))  # noqa: E501
        if 'yk_money_market' in params:
            query_params.append(('YK: Money Market', params['yk_money_market']))  # noqa: E501
        if 'yk_municipal' in params:
            query_params.append(('YK: Municipal', params['yk_municipal']))  # noqa: E501
        if 'yk_preferred' in params:
            query_params.append(('YK: Preferred', params['yk_preferred']))  # noqa: E501
        if 'yk_us_government' in params:
            query_params.append(('YK: US Government', params['yk_us_government']))  # noqa: E501

        header_params = {}
        if 'jwt' in params:
            header_params['JWT'] = params['jwt']  # noqa: E501
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/ld+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/catalogs/bbg/fields/', 'OPTIONS',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def options_ontology(self, jwt, api_version, **kwargs):  # noqa: E501
        """Options for the DATA<GO> Ontology  # noqa: E501

        Returns the methods that are supported by this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_ontology(jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.options_ontology_with_http_info(jwt, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.options_ontology_with_http_info(jwt, api_version, **kwargs)  # noqa: E501
            return data

    def options_ontology_with_http_info(self, jwt, api_version, **kwargs):  # noqa: E501
        """Options for the DATA<GO> Ontology  # noqa: E501

        Returns the methods that are supported by this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_ontology_with_http_info(jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['jwt', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method options_ontology" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `options_ontology`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `options_ontology`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'jwt' in params:
            header_params['JWT'] = params['jwt']  # noqa: E501
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/ld+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/ontology', 'OPTIONS',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def options_request(self, catalog, request_name, jwt, api_version, **kwargs):  # noqa: E501
        """Options for a request resource  # noqa: E501

        Returns the methods that are supported by this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_request(catalog, request_name, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str request_name: Request name (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.options_request_with_http_info(catalog, request_name, jwt, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.options_request_with_http_info(catalog, request_name, jwt, api_version, **kwargs)  # noqa: E501
            return data

    def options_request_with_http_info(self, catalog, request_name, jwt, api_version, **kwargs):  # noqa: E501
        """Options for a request resource  # noqa: E501

        Returns the methods that are supported by this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_request_with_http_info(catalog, request_name, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str request_name: Request name (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['catalog', 'request_name', 'jwt', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method options_request" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog' is set
        if ('catalog' not in params or
                params['catalog'] is None):
            raise ValueError("Missing the required parameter `catalog` when calling `options_request`")  # noqa: E501
        # verify the required parameter 'request_name' is set
        if ('request_name' not in params or
                params['request_name'] is None):
            raise ValueError("Missing the required parameter `request_name` when calling `options_request`")  # noqa: E501
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `options_request`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `options_request`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'catalog' in params:
            path_params['catalog'] = params['catalog']  # noqa: E501
        if 'request_name' in params:
            path_params['requestName'] = params['request_name']  # noqa: E501

        query_params = []

        header_params = {}
        if 'jwt' in params:
            header_params['JWT'] = params['jwt']  # noqa: E501
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/ld+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/catalogs/{catalog}/requests/{requestName}/', 'OPTIONS',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def options_request_field_list(self, catalog, request_name, jwt, api_version, **kwargs):  # noqa: E501
        """Options for a field list resource  # noqa: E501

        Returns the methods that are supported by this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_request_field_list(catalog, request_name, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str request_name: Request name (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param int page: Page number to view
        :param int page_size: Number of items per page. Defaults to 20 if not supplied.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.options_request_field_list_with_http_info(catalog, request_name, jwt, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.options_request_field_list_with_http_info(catalog, request_name, jwt, api_version, **kwargs)  # noqa: E501
            return data

    def options_request_field_list_with_http_info(self, catalog, request_name, jwt, api_version, **kwargs):  # noqa: E501
        """Options for a field list resource  # noqa: E501

        Returns the methods that are supported by this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_request_field_list_with_http_info(catalog, request_name, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str request_name: Request name (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param int page: Page number to view
        :param int page_size: Number of items per page. Defaults to 20 if not supplied.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['catalog', 'request_name', 'jwt', 'api_version', 'page', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method options_request_field_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog' is set
        if ('catalog' not in params or
                params['catalog'] is None):
            raise ValueError("Missing the required parameter `catalog` when calling `options_request_field_list`")  # noqa: E501
        # verify the required parameter 'request_name' is set
        if ('request_name' not in params or
                params['request_name'] is None):
            raise ValueError("Missing the required parameter `request_name` when calling `options_request_field_list`")  # noqa: E501
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `options_request_field_list`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `options_request_field_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'catalog' in params:
            path_params['catalog'] = params['catalog']  # noqa: E501
        if 'request_name' in params:
            path_params['requestName'] = params['request_name']  # noqa: E501

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501

        header_params = {}
        if 'jwt' in params:
            header_params['JWT'] = params['jwt']  # noqa: E501
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/ld+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/catalogs/{catalog}/requests/{requestName}/fieldList/', 'OPTIONS',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def options_request_trigger(self, catalog, request_name, jwt, api_version, **kwargs):  # noqa: E501
        """Options for a trigger resource  # noqa: E501

        Returns the methods that are supported by this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_request_trigger(catalog, request_name, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str request_name: Request name (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.options_request_trigger_with_http_info(catalog, request_name, jwt, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.options_request_trigger_with_http_info(catalog, request_name, jwt, api_version, **kwargs)  # noqa: E501
            return data

    def options_request_trigger_with_http_info(self, catalog, request_name, jwt, api_version, **kwargs):  # noqa: E501
        """Options for a trigger resource  # noqa: E501

        Returns the methods that are supported by this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_request_trigger_with_http_info(catalog, request_name, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str request_name: Request name (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['catalog', 'request_name', 'jwt', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method options_request_trigger" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog' is set
        if ('catalog' not in params or
                params['catalog'] is None):
            raise ValueError("Missing the required parameter `catalog` when calling `options_request_trigger`")  # noqa: E501
        # verify the required parameter 'request_name' is set
        if ('request_name' not in params or
                params['request_name'] is None):
            raise ValueError("Missing the required parameter `request_name` when calling `options_request_trigger`")  # noqa: E501
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `options_request_trigger`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `options_request_trigger`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'catalog' in params:
            path_params['catalog'] = params['catalog']  # noqa: E501
        if 'request_name' in params:
            path_params['requestName'] = params['request_name']  # noqa: E501

        query_params = []

        header_params = {}
        if 'jwt' in params:
            header_params['JWT'] = params['jwt']  # noqa: E501
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/ld+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/catalogs/{catalog}/requests/{requestName}/trigger/', 'OPTIONS',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def options_request_universe(self, catalog, request_name, jwt, api_version, **kwargs):  # noqa: E501
        """Options for a universe resource  # noqa: E501

        Returns the methods that are supported by this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_request_universe(catalog, request_name, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str request_name: Request name (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param int page: Page number to view
        :param int page_size: Number of items per page. Defaults to 20 if not supplied.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.options_request_universe_with_http_info(catalog, request_name, jwt, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.options_request_universe_with_http_info(catalog, request_name, jwt, api_version, **kwargs)  # noqa: E501
            return data

    def options_request_universe_with_http_info(self, catalog, request_name, jwt, api_version, **kwargs):  # noqa: E501
        """Options for a universe resource  # noqa: E501

        Returns the methods that are supported by this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_request_universe_with_http_info(catalog, request_name, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str request_name: Request name (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param int page: Page number to view
        :param int page_size: Number of items per page. Defaults to 20 if not supplied.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['catalog', 'request_name', 'jwt', 'api_version', 'page', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method options_request_universe" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog' is set
        if ('catalog' not in params or
                params['catalog'] is None):
            raise ValueError("Missing the required parameter `catalog` when calling `options_request_universe`")  # noqa: E501
        # verify the required parameter 'request_name' is set
        if ('request_name' not in params or
                params['request_name'] is None):
            raise ValueError("Missing the required parameter `request_name` when calling `options_request_universe`")  # noqa: E501
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `options_request_universe`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `options_request_universe`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'catalog' in params:
            path_params['catalog'] = params['catalog']  # noqa: E501
        if 'request_name' in params:
            path_params['requestName'] = params['request_name']  # noqa: E501

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501

        header_params = {}
        if 'jwt' in params:
            header_params['JWT'] = params['jwt']  # noqa: E501
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/ld+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/catalogs/{catalog}/requests/{requestName}/universe/', 'OPTIONS',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def options_requests(self, catalog, jwt, api_version, **kwargs):  # noqa: E501
        """Options for a collection of requests  # noqa: E501

        Returns the methods that are supported by this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_requests(catalog, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param int page: Page number to view
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.options_requests_with_http_info(catalog, jwt, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.options_requests_with_http_info(catalog, jwt, api_version, **kwargs)  # noqa: E501
            return data

    def options_requests_with_http_info(self, catalog, jwt, api_version, **kwargs):  # noqa: E501
        """Options for a collection of requests  # noqa: E501

        Returns the methods that are supported by this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_requests_with_http_info(catalog, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param int page: Page number to view
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['catalog', 'jwt', 'api_version', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method options_requests" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog' is set
        if ('catalog' not in params or
                params['catalog'] is None):
            raise ValueError("Missing the required parameter `catalog` when calling `options_requests`")  # noqa: E501
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `options_requests`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `options_requests`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'catalog' in params:
            path_params['catalog'] = params['catalog']  # noqa: E501

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}
        if 'jwt' in params:
            header_params['JWT'] = params['jwt']  # noqa: E501
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/ld+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/catalogs/{catalog}/requests/', 'OPTIONS',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def options_root(self, jwt, api_version, **kwargs):  # noqa: E501
        """Options for entry point  # noqa: E501

        Returns the methods that are supported by this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_root(jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.options_root_with_http_info(jwt, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.options_root_with_http_info(jwt, api_version, **kwargs)  # noqa: E501
            return data

    def options_root_with_http_info(self, jwt, api_version, **kwargs):  # noqa: E501
        """Options for entry point  # noqa: E501

        Returns the methods that are supported by this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_root_with_http_info(jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['jwt', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method options_root" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `options_root`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `options_root`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'jwt' in params:
            header_params['JWT'] = params['jwt']  # noqa: E501
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/ld+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/', 'OPTIONS',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def options_snapshot(self, catalog, dataset, snapshot, jwt, api_version, **kwargs):  # noqa: E501
        """Options for snapshot metadata and available distributions  # noqa: E501

        Returns the methods that are supported by this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_snapshot(catalog, dataset, snapshot, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str dataset: Dataset identifier (required)
        :param str snapshot: Dataset snapshot identifier (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.options_snapshot_with_http_info(catalog, dataset, snapshot, jwt, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.options_snapshot_with_http_info(catalog, dataset, snapshot, jwt, api_version, **kwargs)  # noqa: E501
            return data

    def options_snapshot_with_http_info(self, catalog, dataset, snapshot, jwt, api_version, **kwargs):  # noqa: E501
        """Options for snapshot metadata and available distributions  # noqa: E501

        Returns the methods that are supported by this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_snapshot_with_http_info(catalog, dataset, snapshot, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str dataset: Dataset identifier (required)
        :param str snapshot: Dataset snapshot identifier (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['catalog', 'dataset', 'snapshot', 'jwt', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method options_snapshot" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog' is set
        if ('catalog' not in params or
                params['catalog'] is None):
            raise ValueError("Missing the required parameter `catalog` when calling `options_snapshot`")  # noqa: E501
        # verify the required parameter 'dataset' is set
        if ('dataset' not in params or
                params['dataset'] is None):
            raise ValueError("Missing the required parameter `dataset` when calling `options_snapshot`")  # noqa: E501
        # verify the required parameter 'snapshot' is set
        if ('snapshot' not in params or
                params['snapshot'] is None):
            raise ValueError("Missing the required parameter `snapshot` when calling `options_snapshot`")  # noqa: E501
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `options_snapshot`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `options_snapshot`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'catalog' in params:
            path_params['catalog'] = params['catalog']  # noqa: E501
        if 'dataset' in params:
            path_params['dataset'] = params['dataset']  # noqa: E501
        if 'snapshot' in params:
            path_params['snapshot'] = params['snapshot']  # noqa: E501

        query_params = []

        header_params = {}
        if 'jwt' in params:
            header_params['JWT'] = params['jwt']  # noqa: E501
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/ld+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/catalogs/{catalog}/datasets/{dataset}/snapshots/{snapshot}/', 'OPTIONS',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def options_snapshots(self, catalog, dataset, jwt, api_version, **kwargs):  # noqa: E501
        """Options for list of available snapshots for a dataset  # noqa: E501

        Returns the methods that are supported by this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_snapshots(catalog, dataset, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str dataset: Dataset identifier (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param int page: Page number to view
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.options_snapshots_with_http_info(catalog, dataset, jwt, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.options_snapshots_with_http_info(catalog, dataset, jwt, api_version, **kwargs)  # noqa: E501
            return data

    def options_snapshots_with_http_info(self, catalog, dataset, jwt, api_version, **kwargs):  # noqa: E501
        """Options for list of available snapshots for a dataset  # noqa: E501

        Returns the methods that are supported by this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_snapshots_with_http_info(catalog, dataset, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str dataset: Dataset identifier (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param int page: Page number to view
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['catalog', 'dataset', 'jwt', 'api_version', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method options_snapshots" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog' is set
        if ('catalog' not in params or
                params['catalog'] is None):
            raise ValueError("Missing the required parameter `catalog` when calling `options_snapshots`")  # noqa: E501
        # verify the required parameter 'dataset' is set
        if ('dataset' not in params or
                params['dataset'] is None):
            raise ValueError("Missing the required parameter `dataset` when calling `options_snapshots`")  # noqa: E501
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `options_snapshots`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `options_snapshots`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'catalog' in params:
            path_params['catalog'] = params['catalog']  # noqa: E501
        if 'dataset' in params:
            path_params['dataset'] = params['dataset']  # noqa: E501

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}
        if 'jwt' in params:
            header_params['JWT'] = params['jwt']  # noqa: E501
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/ld+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/catalogs/{catalog}/datasets/{dataset}/snapshots/', 'OPTIONS',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def options_trigger(self, catalog, trigger_name, jwt, api_version, **kwargs):  # noqa: E501
        """Options for a trigger resource  # noqa: E501

        Returns the methods that are supported by this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_trigger(catalog, trigger_name, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str trigger_name: Trigger name. (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.options_trigger_with_http_info(catalog, trigger_name, jwt, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.options_trigger_with_http_info(catalog, trigger_name, jwt, api_version, **kwargs)  # noqa: E501
            return data

    def options_trigger_with_http_info(self, catalog, trigger_name, jwt, api_version, **kwargs):  # noqa: E501
        """Options for a trigger resource  # noqa: E501

        Returns the methods that are supported by this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_trigger_with_http_info(catalog, trigger_name, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str trigger_name: Trigger name. (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['catalog', 'trigger_name', 'jwt', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method options_trigger" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog' is set
        if ('catalog' not in params or
                params['catalog'] is None):
            raise ValueError("Missing the required parameter `catalog` when calling `options_trigger`")  # noqa: E501
        # verify the required parameter 'trigger_name' is set
        if ('trigger_name' not in params or
                params['trigger_name'] is None):
            raise ValueError("Missing the required parameter `trigger_name` when calling `options_trigger`")  # noqa: E501
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `options_trigger`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `options_trigger`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'catalog' in params:
            path_params['catalog'] = params['catalog']  # noqa: E501
        if 'trigger_name' in params:
            path_params['triggerName'] = params['trigger_name']  # noqa: E501

        query_params = []

        header_params = {}
        if 'jwt' in params:
            header_params['JWT'] = params['jwt']  # noqa: E501
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/ld+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/catalogs/{catalog}/triggers/{triggerName}/', 'OPTIONS',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def options_triggers(self, catalog, jwt, api_version, **kwargs):  # noqa: E501
        """Options for a collection of triggers  # noqa: E501

        Returns the methods that are supported by this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_triggers(catalog, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param int page: Page number to view
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.options_triggers_with_http_info(catalog, jwt, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.options_triggers_with_http_info(catalog, jwt, api_version, **kwargs)  # noqa: E501
            return data

    def options_triggers_with_http_info(self, catalog, jwt, api_version, **kwargs):  # noqa: E501
        """Options for a collection of triggers  # noqa: E501

        Returns the methods that are supported by this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_triggers_with_http_info(catalog, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param int page: Page number to view
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['catalog', 'jwt', 'api_version', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method options_triggers" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog' is set
        if ('catalog' not in params or
                params['catalog'] is None):
            raise ValueError("Missing the required parameter `catalog` when calling `options_triggers`")  # noqa: E501
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `options_triggers`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `options_triggers`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'catalog' in params:
            path_params['catalog'] = params['catalog']  # noqa: E501

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}
        if 'jwt' in params:
            header_params['JWT'] = params['jwt']  # noqa: E501
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/ld+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/catalogs/{catalog}/triggers/', 'OPTIONS',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def options_universe(self, catalog, universe_name, jwt, api_version, **kwargs):  # noqa: E501
        """Options for a universe resource  # noqa: E501

        Returns the methods that are supported by this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_universe(catalog, universe_name, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str universe_name: Universe name. (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.options_universe_with_http_info(catalog, universe_name, jwt, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.options_universe_with_http_info(catalog, universe_name, jwt, api_version, **kwargs)  # noqa: E501
            return data

    def options_universe_with_http_info(self, catalog, universe_name, jwt, api_version, **kwargs):  # noqa: E501
        """Options for a universe resource  # noqa: E501

        Returns the methods that are supported by this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_universe_with_http_info(catalog, universe_name, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str universe_name: Universe name. (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['catalog', 'universe_name', 'jwt', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method options_universe" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog' is set
        if ('catalog' not in params or
                params['catalog'] is None):
            raise ValueError("Missing the required parameter `catalog` when calling `options_universe`")  # noqa: E501
        # verify the required parameter 'universe_name' is set
        if ('universe_name' not in params or
                params['universe_name'] is None):
            raise ValueError("Missing the required parameter `universe_name` when calling `options_universe`")  # noqa: E501
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `options_universe`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `options_universe`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'catalog' in params:
            path_params['catalog'] = params['catalog']  # noqa: E501
        if 'universe_name' in params:
            path_params['universeName'] = params['universe_name']  # noqa: E501

        query_params = []

        header_params = {}
        if 'jwt' in params:
            header_params['JWT'] = params['jwt']  # noqa: E501
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/ld+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/catalogs/{catalog}/universes/{universeName}/', 'OPTIONS',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def options_universes(self, catalog, jwt, api_version, **kwargs):  # noqa: E501
        """Options for a collection of universes  # noqa: E501

        Returns the methods that are supported by this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_universes(catalog, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param int page: Page number to view
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.options_universes_with_http_info(catalog, jwt, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.options_universes_with_http_info(catalog, jwt, api_version, **kwargs)  # noqa: E501
            return data

    def options_universes_with_http_info(self, catalog, jwt, api_version, **kwargs):  # noqa: E501
        """Options for a collection of universes  # noqa: E501

        Returns the methods that are supported by this endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.options_universes_with_http_info(catalog, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param int page: Page number to view
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['catalog', 'jwt', 'api_version', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method options_universes" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog' is set
        if ('catalog' not in params or
                params['catalog'] is None):
            raise ValueError("Missing the required parameter `catalog` when calling `options_universes`")  # noqa: E501
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `options_universes`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `options_universes`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'catalog' in params:
            path_params['catalog'] = params['catalog']  # noqa: E501

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}
        if 'jwt' in params:
            header_params['JWT'] = params['jwt']  # noqa: E501
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/ld+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/catalogs/{catalog}/universes/', 'OPTIONS',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
