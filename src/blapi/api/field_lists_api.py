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


class FieldListsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_field_list(self, catalog, field_list_name, jwt, api_version, **kwargs):  # noqa: E501
        """Delete a field list resource  # noqa: E501

        Field Lists that are referenced by active recurring requests CAN NOT be deleted and will return a status code of 400.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_field_list(catalog, field_list_name, jwt, api_version, async_req=True)
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
            return self.delete_field_list_with_http_info(catalog, field_list_name, jwt, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_field_list_with_http_info(catalog, field_list_name, jwt, api_version, **kwargs)  # noqa: E501
            return data

    def delete_field_list_with_http_info(self, catalog, field_list_name, jwt, api_version, **kwargs):  # noqa: E501
        """Delete a field list resource  # noqa: E501

        Field Lists that are referenced by active recurring requests CAN NOT be deleted and will return a status code of 400.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_field_list_with_http_info(catalog, field_list_name, jwt, api_version, async_req=True)
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
                    " to method delete_field_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog' is set
        if ('catalog' not in params or
                params['catalog'] is None):
            raise ValueError("Missing the required parameter `catalog` when calling `delete_field_list`")  # noqa: E501
        # verify the required parameter 'field_list_name' is set
        if ('field_list_name' not in params or
                params['field_list_name'] is None):
            raise ValueError("Missing the required parameter `field_list_name` when calling `delete_field_list`")  # noqa: E501
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `delete_field_list`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `delete_field_list`")  # noqa: E501

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
            '/catalogs/{catalog}/fieldLists/{fieldListName}/', 'DELETE',
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

    def get_deleted_field_list(self, catalog, field_list_uuid, jwt, api_version, **kwargs):  # noqa: E501
        """Deleted field list resource  # noqa: E501

        A field list that has been deleted.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_deleted_field_list(catalog, field_list_uuid, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str field_list_uuid: Field list unique identifier. (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param int page: Page number to view
        :param int page_size: Number of items per page. Defaults to 20 if not supplied.
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_deleted_field_list_with_http_info(catalog, field_list_uuid, jwt, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.get_deleted_field_list_with_http_info(catalog, field_list_uuid, jwt, api_version, **kwargs)  # noqa: E501
            return data

    def get_deleted_field_list_with_http_info(self, catalog, field_list_uuid, jwt, api_version, **kwargs):  # noqa: E501
        """Deleted field list resource  # noqa: E501

        A field list that has been deleted.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_deleted_field_list_with_http_info(catalog, field_list_uuid, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str field_list_uuid: Field list unique identifier. (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param int page: Page number to view
        :param int page_size: Number of items per page. Defaults to 20 if not supplied.
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['catalog', 'field_list_uuid', 'jwt', 'api_version', 'page', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_deleted_field_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog' is set
        if ('catalog' not in params or
                params['catalog'] is None):
            raise ValueError("Missing the required parameter `catalog` when calling `get_deleted_field_list`")  # noqa: E501
        # verify the required parameter 'field_list_uuid' is set
        if ('field_list_uuid' not in params or
                params['field_list_uuid'] is None):
            raise ValueError("Missing the required parameter `field_list_uuid` when calling `get_deleted_field_list`")  # noqa: E501
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `get_deleted_field_list`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `get_deleted_field_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'catalog' in params:
            path_params['catalog'] = params['catalog']  # noqa: E501
        if 'field_list_uuid' in params:
            path_params['fieldListUUID'] = params['field_list_uuid']  # noqa: E501

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
            '/catalogs/{catalog}/deleted/fieldLists/{fieldListUUID}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2002',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_field_list(self, catalog, field_list_name, jwt, api_version, **kwargs):  # noqa: E501
        """A field list resource  # noqa: E501

        A field list resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_field_list(catalog, field_list_name, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str field_list_name: Field list name. (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param int page: Page number to view
        :param int page_size: Number of items per page. Defaults to 20 if not supplied.
        :return: FieldList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_field_list_with_http_info(catalog, field_list_name, jwt, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.get_field_list_with_http_info(catalog, field_list_name, jwt, api_version, **kwargs)  # noqa: E501
            return data

    def get_field_list_with_http_info(self, catalog, field_list_name, jwt, api_version, **kwargs):  # noqa: E501
        """A field list resource  # noqa: E501

        A field list resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_field_list_with_http_info(catalog, field_list_name, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str field_list_name: Field list name. (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param int page: Page number to view
        :param int page_size: Number of items per page. Defaults to 20 if not supplied.
        :return: FieldList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['catalog', 'field_list_name', 'jwt', 'api_version', 'page', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_field_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog' is set
        if ('catalog' not in params or
                params['catalog'] is None):
            raise ValueError("Missing the required parameter `catalog` when calling `get_field_list`")  # noqa: E501
        # verify the required parameter 'field_list_name' is set
        if ('field_list_name' not in params or
                params['field_list_name'] is None):
            raise ValueError("Missing the required parameter `field_list_name` when calling `get_field_list`")  # noqa: E501
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `get_field_list`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `get_field_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'catalog' in params:
            path_params['catalog'] = params['catalog']  # noqa: E501
        if 'field_list_name' in params:
            path_params['fieldListName'] = params['field_list_name']  # noqa: E501

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
            '/catalogs/{catalog}/fieldLists/{fieldListName}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FieldList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_field_lists(self, catalog, jwt, api_version, **kwargs):  # noqa: E501
        """A collection of field lists  # noqa: E501

        A collection of field lists within a specific catalog.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_field_lists(catalog, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param int page: Page number to view
        :param int page_size: Number of items per page. Defaults to 20 if not supplied.
        :param FieldListType type: Filter field lists by @type. If not supplied, no filtering is applied.
        :return: FieldListCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_field_lists_with_http_info(catalog, jwt, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.get_field_lists_with_http_info(catalog, jwt, api_version, **kwargs)  # noqa: E501
            return data

    def get_field_lists_with_http_info(self, catalog, jwt, api_version, **kwargs):  # noqa: E501
        """A collection of field lists  # noqa: E501

        A collection of field lists within a specific catalog.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_field_lists_with_http_info(catalog, jwt, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param int page: Page number to view
        :param int page_size: Number of items per page. Defaults to 20 if not supplied.
        :param FieldListType type: Filter field lists by @type. If not supplied, no filtering is applied.
        :return: FieldListCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['catalog', 'jwt', 'api_version', 'page', 'page_size', 'type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_field_lists" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog' is set
        if ('catalog' not in params or
                params['catalog'] is None):
            raise ValueError("Missing the required parameter `catalog` when calling `get_field_lists`")  # noqa: E501
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `get_field_lists`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `get_field_lists`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'catalog' in params:
            path_params['catalog'] = params['catalog']  # noqa: E501

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501
        if 'type' in params:
            query_params.append(('type', params['type']))  # noqa: E501

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
            '/catalogs/{catalog}/fieldLists/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FieldListCollection',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def patch_field_list(self, body, jwt, api_version, content_type, catalog, field_list_name, **kwargs):  # noqa: E501
        """Update a field list resource  # noqa: E501

        Field lists that have active requests referencing them CAN NOT be updated and will return a 400 status code.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_field_list(body, jwt, api_version, content_type, catalog, field_list_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FieldListPatchPayload body: (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param str content_type: Media type (https://tools.ietf.org/html/rfc7231#section-3.1.1.5) of the POST/PATCH payload. Only 'application/json' is accepted. Any other format will result in a 400 (bad request). (required)
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str field_list_name: Field list name. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.patch_field_list_with_http_info(body, jwt, api_version, content_type, catalog, field_list_name, **kwargs)  # noqa: E501
        else:
            (data) = self.patch_field_list_with_http_info(body, jwt, api_version, content_type, catalog, field_list_name, **kwargs)  # noqa: E501
            return data

    def patch_field_list_with_http_info(self, body, jwt, api_version, content_type, catalog, field_list_name, **kwargs):  # noqa: E501
        """Update a field list resource  # noqa: E501

        Field lists that have active requests referencing them CAN NOT be updated and will return a 400 status code.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_field_list_with_http_info(body, jwt, api_version, content_type, catalog, field_list_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FieldListPatchPayload body: (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param str content_type: Media type (https://tools.ietf.org/html/rfc7231#section-3.1.1.5) of the POST/PATCH payload. Only 'application/json' is accepted. Any other format will result in a 400 (bad request). (required)
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :param str field_list_name: Field list name. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'jwt', 'api_version', 'content_type', 'catalog', 'field_list_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_field_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `patch_field_list`")  # noqa: E501
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `patch_field_list`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `patch_field_list`")  # noqa: E501
        # verify the required parameter 'content_type' is set
        if ('content_type' not in params or
                params['content_type'] is None):
            raise ValueError("Missing the required parameter `content_type` when calling `patch_field_list`")  # noqa: E501
        # verify the required parameter 'catalog' is set
        if ('catalog' not in params or
                params['catalog'] is None):
            raise ValueError("Missing the required parameter `catalog` when calling `patch_field_list`")  # noqa: E501
        # verify the required parameter 'field_list_name' is set
        if ('field_list_name' not in params or
                params['field_list_name'] is None):
            raise ValueError("Missing the required parameter `field_list_name` when calling `patch_field_list`")  # noqa: E501

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
        if 'content_type' in params:
            header_params['Content-Type'] = params['content_type']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/ld+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/catalogs/{catalog}/fieldLists/{fieldListName}/', 'PATCH',
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

    def post_field_list(self, body, jwt, api_version, content_type, catalog, **kwargs):  # noqa: E501
        """Create a new field list resource  # noqa: E501

        Create a new field list resource. Requires an identifier (the name, used to construct the URI, must begin with a letter and consist only of alphanumeric characters), title (short description) and the contents.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_field_list(body, jwt, api_version, content_type, catalog, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FieldListPostPayload body: (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param str content_type: Media type (https://tools.ietf.org/html/rfc7231#section-3.1.1.5) of the POST/PATCH payload. Only 'application/json' is accepted. Any other format will result in a 400 (bad request). (required)
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :return: Status
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_field_list_with_http_info(body, jwt, api_version, content_type, catalog, **kwargs)  # noqa: E501
        else:
            (data) = self.post_field_list_with_http_info(body, jwt, api_version, content_type, catalog, **kwargs)  # noqa: E501
            return data

    def post_field_list_with_http_info(self, body, jwt, api_version, content_type, catalog, **kwargs):  # noqa: E501
        """Create a new field list resource  # noqa: E501

        Create a new field list resource. Requires an identifier (the name, used to construct the URI, must begin with a letter and consist only of alphanumeric characters), title (short description) and the contents.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_field_list_with_http_info(body, jwt, api_version, content_type, catalog, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FieldListPostPayload body: (required)
        :param str jwt: JWT(https://tools.ietf.org/html/rfc7519) Authentication token (required)
        :param str api_version: Version of the API to access. The only valid value is 2. (required)
        :param str content_type: Media type (https://tools.ietf.org/html/rfc7231#section-3.1.1.5) of the POST/PATCH payload. Only 'application/json' is accepted. Any other format will result in a 400 (bad request). (required)
        :param str catalog: Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`). (required)
        :return: Status
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'jwt', 'api_version', 'content_type', 'catalog']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_field_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_field_list`")  # noqa: E501
        # verify the required parameter 'jwt' is set
        if ('jwt' not in params or
                params['jwt'] is None):
            raise ValueError("Missing the required parameter `jwt` when calling `post_field_list`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `post_field_list`")  # noqa: E501
        # verify the required parameter 'content_type' is set
        if ('content_type' not in params or
                params['content_type'] is None):
            raise ValueError("Missing the required parameter `content_type` when calling `post_field_list`")  # noqa: E501
        # verify the required parameter 'catalog' is set
        if ('catalog' not in params or
                params['catalog'] is None):
            raise ValueError("Missing the required parameter `catalog` when calling `post_field_list`")  # noqa: E501

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
        if 'content_type' in params:
            header_params['Content-Type'] = params['content_type']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/ld+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/catalogs/{catalog}/fieldLists/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Status',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
