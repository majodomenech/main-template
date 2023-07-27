# coding: utf-8
"""
    DL REST API

    # Overview [DATA&lt;GO&gt;](https://data.bloomberg.com) and [DL REST API](https://api.bloomberg.com/eap) are the Web interfaces for the Bloomberg Data License Platform. The [Data License Platform Guide](https://data.bloomberg.com/docs/data-license/) provides a general overview of the platform and its capabilities. DL REST API is the REST API for the Bloomberg Data License Platform, which powers [DATA&lt;GO&gt;](https://data.bloomberg.com).  You can use [DL REST API](https://api.bloomberg.com/eap) to access any capability or data that is accessible through [DATA&lt;GO&gt;](https://data.bloomberg.com): For example, to automate the retrieval of bulk datasets and Bloomberg metadata or, to request, schedule and retrieve custom datasets using reusable resources.   # Getting Started To get started with DL REST API, you need to : * Register your application at https://console.bloomberg.com/ * Obtain a set of credentials for your application at https://console.bloomberg.com/ * Add your IP address to the allowlist for your application at https://console.bloomberg.com/ * Download sample code at https://developer.bloomberg.com/portal/downloads * Use the sample code to connect to the [entrypoint](#tag/entrypoint) at https://api.bloomberg.com/eap/ * Explore DATA&lt;GO&gt;, a WEB UI that is powered by DL REST API, to get familiar with DL REST API concepts. Login at https://data.bloomberg.com/  ## Authentication and Authorization Each request to DL REST API must include a [JSON Web Token (JWT)](https://jwt.io/) header, unique to and matching the request. The token must be signed with a valid Data License credential (see [sample code](#section/Getting-Started)). The Data License Platform verifies that the token corresponds to the endpoint being requested and is unique. The Platform also checks the credential used to sign the token, to verify access rights to the resource being requested.  Credentials and permitted IP address allowlists are managed through https://console.bloomberg.com/.  The credentials must be : 1. Issued by a Data License account with active Bloomberg Data License agreements. 2. Unexpired 3. Configured with a permitted IP allowlist entry for the address issuing the request.  DL REST API supports server mode Authentication Flow. Hybrid and device modes are not supported.  Navigate to [DL REST APIConsole > Develop > Developer Documentation > API References > Authentication & Authorization](https://console.bloomberg.com/) to learn more about DL REST API authentication. ## Version Headers Every request to DL REST API must include an `api-version` header (set to `api-version` to 2 for the version described by this specification).  This is the only supported value for `api-version`.  Requests that do not set the `api-version` header, and requests that provide an unsupported `api-version` header value will be rejected with a 400 response code. Response headers include a `latest-api-version` which returns the latest available version of the api. ## Search * Many collection endpoints provide search templates that can be used to query them, including full text search. These are provided using the [Hydra](https://www.hydra-cg.com/spec/latest/core/) [`search`](https://www.hydra-cg.com/spec/latest/core/#hydra:search) property. * Ordering of the returned results is controlled by the `sort` query parameter. * Other sort fields such as `title` can be used * The default sort order is ascending. If the sort field is prefixed with `-` it will return results in descending order, e.g. https://api.bloomberg.com/eap/catalogs/bbg/datasets/?sort=-title ## Pagination * Paging sequence bounds for paged collections will always be indicated with `first` and `last` links (either in the LDP-Paging headers or in the Hydra PartialCollectionView). * Within a paging sequence, a `next` link will be present on all pages except the last and a `prev` link will be present on all pages except the first, to aid sequential traversal. * Pages beyond the paging sequence bounds will return a response with an empty collection. * Pages beyond the paging sequence bounds will not have `next` or `prev` links. * Pages that support the `pageSize` query parameter permit a user defined `pageSize`. ## Redirects * `latest` represents the most recently created resource in a particular collection. It is currently applicable for the `snapshots` endpoints. Since \"latest\" changes meaning over time, this a convenience shortcut rather than a canonical resource. * While Bloomberg Data License makes every effort to maintain stable URLs, API users should receive and process HTTP redirect codes, and must specify a header to determine the version of the API to which they are coding (this document describes version 2) . ## Rate Limiting The number of requests is currently limited to 1000 requests per second per IP address, and 1200 requests per minute per application. An application in this context is defined as a [Bloomberg Enterprise Console Application](https://console.bloomberg.com/). Any request rate greater than this number will be rejected with an HTTP error code of `429`. ## Compression By default all datasets (excluding parquet archives which are already compact) are returned uncompressed. You can negotiate gzip compression by setting the \"Accept-Encoding\" request header to \"gzip\" as per [rfc2612](https://tools.ietf.org/html/rfc2616#section-14.3).  # New Features ## JSON Output You can now request DataRequest, BvalSnapshotRequest and PricingSnapshotRequest datasets in either JSON and CSV format.   ## Mnemonics in CSV and JSON You can now standardize all your workflows using mnemonics as field identifiers on input and output. CSV and JSON output is now available with mnemonics as field identifiers. Where you submit or schedule a request using previous (\"old\") mnemonics, the output file will return the mnemonics as you requested them, ensuring your workflow remains stable over time. You may continue to use clean names where you already do so, but Bloomberg recommends that where possible and compatible with your existing systems, new workflows are implemented using mnemonics rather than clean names, in both the `fieldList` and the `request` output format specification.  ## Bulk Format Fields A bulk format field defines a nested or embedded schema. Bloomberg represents rich content that cannot be encoded in a single scalar value using bulk format fields. Bulk Format fields are now available in JSON, CSV and Bloomberg file formats. See [here](https://developer.bloomberg.com/portal/documents/per_security/getting_started_with_rest_api/1185__distributions_and_file_formats#processing_bulk_fields) for more details to understand bulk format fields and how they are encoded in each of the file formats.  ## Inline Resources (Single POST Request) Implement a simple atomic request operation in your workflow: The DL REST API now allows you submit or schedule a per security request in a single HTTP POST that defines the universe, fieldlist and trigger, and submits or schedules the request for execution. Refer to the [sample code](https://developer.bloomberg.com/portal/downloads), or \"Inline Universe\", \"Inline FieldList\" and \"Inline Trigger\" properties in the [request POST](#operation/postRequest) section of this specification.   Re-usable resources continue to be fully supported for advanced workflows where you need to share universes or fieldlists.  ## Resource Deletion Manage the universes, fieldlists and triggers in your catalog: The DL REST API now supports archival of these resources, where they are not currently referenced by an active request. Remove resources with an HTTP DELETE, and retrieve or recover deleted resources through the [deleted `universe`](#operation/getDeletedUniverse), [deleted `fieldlist`](#operation/getDeletedFieldList), and [deleted `trigger`](#operation/getDeletedTrigger) endpoints.  Refer the sections in this specification on deleting a [`universe`](#operation/deleteUniverse), [`fieldlist`](#operation/deleteFieldList), or [`trigger`](#operation/deleteTrigger) for more information.  # Features ## Entity Data Requests Bloomberg's Entity Data provides legal entity data for public and private companies, funds, government agencies, and municipalities. You can request Entity Data through DL REST API by POSTing a resource of type EntityRequest to /catalogs/{catalog}/requests/. * Legal Entity Identifiers (LEI) are supported for Entity Requests. * Field lists are strongly typed to match the Entity Data request type. * Security level overrides are ignored by Entity Requests. ## CSV Output You can now request DataRequest and BvalSnapshotRequest datasets in a standard [CSV](https://www.ietf.org/rfc/rfc4180.txt) format. CSV output from DL REST API is normalized to [XSD 1.1 types](https://www.w3.org/TR/xmlschema11-2/) such as xsd:boolean and xsd:date to facilitate ingestion.\" ## History Archives DL REST API now offers parquet time-series archives for subscribers to Bulk History products. - The `archives` endpoint allows you to discover and request parquet \"archives\" representing a time-series of snapshots of a dataset. It supports bitemporal search by as-of snapshot dates and by as-at issued date-times). - `archives` are published in two different forms, so you can select a publication model to  meet your workflow needs. - The first publication model is intended for clients ingesting data into a data lake or data science platform: Download archives of status \"final\" and \"current\" (an archive becomes final when it reaches 1GB), replacing the most recent \"current\" archive each day in your system until this becomes \"final\". - The second model is designed to drive an ETL process feeding an ODS or data warehouse. Download \"ongoing\" daily parquet archives as they become available, appending the data to the data have already collected. - Since parquet is a compact format,  DL REST API does not further compress parquet archives, so downloads must set the `Accept-Encoding` header to `Identity`. ## Push Notifications To avoid polling the REST APIs for new distributions, DL REST API provides an API for receiving push notifications when `distributions` become available. We provide a [W3C Server Sent Event Stream](https://html.spec.whatwg.org/multipage/server-sent-events.html) to push notifications to connected clients over HTTP. Subscribe to the event stream at the [`/notifications/sse`](#tag/sse) endpoint to receive push notifications of `DistributionPublishedActivity` events for Bulk and Custom [`dataset`](#tag/dataset) publications immediately when they are available. ## BVAL Evaluated Pricing Bloomberg's BVAL evaluated pricing service provides accurate and defensible pricing of fixed income and derivatives instruments. If you are a subscriber to the BVAL service, you can request a BVAL Snapshot through DL REST API by POSTing a resource of type `BvalSnapshotRequest` to [/catalogs/{catalog}/requests/](#operation/postRequest). You can expect the response to be delivered according to the `snapshotTier` you select. You should expect a Tier 1 response within 45 minutes of the snapshot time, and a Tier 2 response within 3 hours. You can also request BVAL prices after the snapshot time, through a `DataRequest`, using the pricing sources indicated in the table below.  ### BVAL Snapshots  BVAL Snapshots are available at the following snapshot times and can be specified in a `BvalSnapshotRequest` or `DataRequest`. DL REST API provides a [push notification](#section/New-Features/Push-Notifications) immediately that the response is available.  New York Early Close pricing is available on SIFMA Recommended Early Close days. The New York 15:00 snapshot will run at 13:00, and the New York 16:00 at 14:00. Enabled clients will receive their datasets at earlier times if they follow the submission guidelines below. Please contact your BVAL Sales representative to get enabled for Early Close pricing.  |Snapshot Time|Snapshot Timezone|SIFMA Early Close Snapshot Time|T1 Request By|T2 Request By|T1 Response By|T2 Response By| | --- | --- | --- | --- | --- | --- | --- | |15:00|America/New_York|13:00|17:30|15:00|15:45|18:00| |16:00|America/New_York|14:00|18:30|16:00|16:45|19:00| |12:00|Europe/London| |14:30|12:00|12:45|15:00| |15:00|Europe/London| |17:30|15:00|15:45|18:00| |16:15|Europe/London| |18:45|16:15|17:00|19:15| |15:00|Asia/Tokyo| |17:30|15:00|15:45|18:00| |16:00|Asia/Tokyo| |18:30|16:00|16:45|19:00| |17:00|Asia/Tokyo| |19:30|17:00|17:45|20:00| |17:00|Asia/Shanghai| |19:30|17:00|17:45|20:00| |17:00|Australia/Sydney| |19:30|17:00|17:45|20:00|  BVAL snapshots are available up to a cutoff time: The cutoff time is defined as 2.5 hours after the snapshot for a Tier 1 Request, and the snapshot time itself for a Tier 2 request.  ### BVAL Pricing Source (PCS) Requests The following pricing sources can also be specified in a `DataRequest`.  |Pricing Source|Comments|Snapshot Time|Snapshot Timezone| | --- | --- | --- | --- | | BVN3 | | 15:00 | America/New_York | | BVN4 | | 16:00 | America/New_York | | BL12 | | 12:00 | Europe/London | | BLN3 | | 15:00 | Europe/London | | BLN4 | | 16:15 | Europe/London | | BVT3 | | 15:00 | Asia/Tokyo | | BVT4 | | 16:00 | Asia/Tokyo | | BVT5 | | 17:00 | Asia/Tokyo | | BSH5 | | 17:00 | Asia/Shanghai | | BVS5 | | 17:00 | Australia/Sydney | | BVAL | Latest available BVAL Evaluated Price. | latest | any | | BVIC | Latest available BVAL Index Convention Price |latest | any |  ## Pricing Snapshots Bloomberg's Pricing Snapshots provide a precise point in time snapshot of market prices for any instrument, available at 15 minute intervals throughout the day. You can request a Pricing Snapshot through DL REST API by POSTing a resource of type PricingSnapshotRequest to [/catalogs/{catalog}/requests/](#operation/postRequest) up to 15 minutes prior to the snapshot time. The response will be delivered shortly after the snapshot time, subject to an embargo period for the requested instruments (see [Exchange Delay](https://data.bloomberg.com/catalogs/bbg/fields/exchangeDelay/)). ## History Requests Request a historic time series over a specified date range and period through DL REST API by POSTing a resource of type `HistoryRequest` to [/catalogs/{catalog}/requests/](#operation/postRequest). - In DL REST API V2, fieldLists are strongly typed to match the request type. DL REST API V1 fieldLists are only supported for `requests` of type `DataRequest` - Security level overrides are ignored by history requests. ## Corporate Actions Requests Request current and future corporate actions through DL REST API by POSTing a resource of type `ActionsRequest` to [/catalogs/{catalog}/requests/](#operation/postRequest). - Request corporate actions that will become effective up to two years in the future or that were recorded by Bloomberg up to seven days prior to request execution. - Review the metadata at https://data.bloomberg.com/documents/actions/ to understand the layout and content of the dataset for an `ActionsRequest`. - Corporate action requests do not require a `FieldList` - all available actions for the security and for its issuer are returned. - Security level overrides are ignored by corporate actions requests. ## Parallel and Resumable Downloads DL REST API supports fast and resumable parallel downloads using the HTTP range requests. This capability is available for all [distributions](#operation/getDistribution), using gzip encoding (set Accept-Encoding to gzip). Refer to the sample code at https://service.bloomberg.com/ for an example of a parallel download from DL REST API using range headers. ## Show Subscribed Datasets Filter by datasets to which you have subscribed with query parameter `subscribed=true` when getting [/catalogs/bbg/datasets/](#operation/getDatasets). ## Extended Pagination Specify page size against supported endpoints with query parameter `pageSize`. ## Request References Where a resource is referenced by an active (scheduled) request, and updates to that resource are restricted, the boolean property `referencedByActiveRequests` will be set to `true`. ## Detailed Error messages Responses are now provided in [JSON-API](https://jsonapi.org/) response format, including an [RFC6901](https://tools.ietf.org/html/rfc6901) pointer to each section of the submitted document that could not be processed.  # API Specification This is the specification for the Bloomberg Data License DL REST API ([DL REST API](https://api.bloomberg.com/eap)).   # noqa: E501

    OpenAPI spec version: 2.8.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""
from __future__ import absolute_import

import datetime
import json
import mimetypes
from multiprocessing.pool import ThreadPool
import os
import re
import tempfile

# python 2 and python 3 compatibility library
import six
from six.moves.urllib.parse import quote

from blapi.configuration import Configuration
import blapi.models
from blapi import rest


class ApiClient(object):
    """Generic API client for Swagger client library builds.

    Swagger generic API client. This client handles the client-
    server communication, and is invariant across implementations. Specifics of
    the methods and models for each application are generated from the Swagger
    templates.

    NOTE: This class is auto generated by the swagger code generator program.
    Ref: https://github.com/swagger-api/swagger-codegen
    Do not edit the class manually.

    :param configuration: .Configuration object for this client
    :param header_name: a header to pass when making calls to the API.
    :param header_value: a header value to pass when making calls to
        the API.
    :param cookie: a cookie to include in the header when making calls
        to the API
    """

    PRIMITIVE_TYPES = (float, bool, bytes, six.text_type) + six.integer_types
    NATIVE_TYPES_MAPPING = {
        'int': int,
        'long': int if six.PY3 else long,  # noqa: F821
        'float': float,
        'str': str,
        'bool': bool,
        'date': datetime.date,
        'datetime': datetime.datetime,
        'object': object,
    }

    def __init__(self, configuration=None, header_name=None, header_value=None,
                 cookie=None):
        if configuration is None:
            configuration = Configuration()
        self.configuration = configuration

        self.pool = ThreadPool()
        self.rest_client = rest.RESTClientObject(configuration)
        self.default_headers = {}
        if header_name is not None:
            self.default_headers[header_name] = header_value
        self.cookie = cookie
        # Set default User-Agent.
        self.user_agent = 'Swagger-Codegen/0.0.1/python'

    def __del__(self):
        self.pool.close()
        self.pool.join()

    @property
    def user_agent(self):
        """User agent for this API client"""
        return self.default_headers['User-Agent']

    @user_agent.setter
    def user_agent(self, value):
        self.default_headers['User-Agent'] = value

    def set_default_header(self, header_name, header_value):
        self.default_headers[header_name] = header_value

    def __call_api(
            self, resource_path, method, path_params=None,
            query_params=None, header_params=None, body=None, post_params=None,
            files=None, response_type=None, auth_settings=None,
            _return_http_data_only=None, collection_formats=None,
            _preload_content=True, _request_timeout=None):

        config = self.configuration

        # header parameters
        header_params = header_params or {}
        header_params.update(self.default_headers)
        if self.cookie:
            header_params['Cookie'] = self.cookie
        if header_params:
            header_params = self.sanitize_for_serialization(header_params)
            header_params = dict(self.parameters_to_tuples(header_params,
                                                           collection_formats))

        # path parameters
        if path_params:
            path_params = self.sanitize_for_serialization(path_params)
            path_params = self.parameters_to_tuples(path_params,
                                                    collection_formats)
            for k, v in path_params:
                # specified safe chars, encode everything
                resource_path = resource_path.replace(
                    '{%s}' % k,
                    quote(str(v), safe=config.safe_chars_for_path_param)
                )

        # query parameters
        if query_params:
            query_params = self.sanitize_for_serialization(query_params)
            query_params = self.parameters_to_tuples(query_params,
                                                     collection_formats)

        # post parameters
        if post_params or files:
            post_params = self.prepare_post_parameters(post_params, files)
            post_params = self.sanitize_for_serialization(post_params)
            post_params = self.parameters_to_tuples(post_params,
                                                    collection_formats)

        # auth setting
        self.update_params_for_auth(header_params, query_params, auth_settings)

        # body
        if body:
            body = self.sanitize_for_serialization(body)

        # request url
        url = self.configuration.host + resource_path

        # perform request and return response
        response_data = self.request(
            method, url, query_params=query_params, headers=header_params,
            post_params=post_params, body=body,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout)

        self.last_response = response_data

        return_data = response_data
        if _preload_content:
            # deserialize response data
            if response_type:
                return_data = self.deserialize(response_data, response_type)
            else:
                return_data = None

        if _return_http_data_only:
            return (return_data)
        else:
            return (return_data, response_data.status,
                    response_data.getheaders())

    def sanitize_for_serialization(self, obj):
        """Builds a JSON POST object.

        If obj is None, return None.
        If obj is str, int, long, float, bool, return directly.
        If obj is datetime.datetime, datetime.date
            convert to string in iso8601 format.
        If obj is list, sanitize each element in the list.
        If obj is dict, return the dict.
        If obj is swagger model, return the properties dict.

        :param obj: The data to serialize.
        :return: The serialized form of data.
        """
        if obj is None:
            return None
        elif isinstance(obj, self.PRIMITIVE_TYPES):
            return obj
        elif isinstance(obj, list):
            return [self.sanitize_for_serialization(sub_obj)
                    for sub_obj in obj]
        elif isinstance(obj, tuple):
            return tuple(self.sanitize_for_serialization(sub_obj)
                         for sub_obj in obj)
        elif isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()

        if isinstance(obj, dict):
            obj_dict = obj
        else:
            # Convert model obj to dict except
            # attributes `swagger_types`, `attribute_map`
            # and attributes which value is not None.
            # Convert attribute name to json key in
            # model definition for request.
            obj_dict = {obj.attribute_map[attr]: getattr(obj, attr)
                        for attr, _ in six.iteritems(obj.swagger_types)
                        if getattr(obj, attr) is not None}

        return {key: self.sanitize_for_serialization(val)
                for key, val in six.iteritems(obj_dict)}

    def deserialize(self, response, response_type):
        """Deserializes response into an object.

        :param response: RESTResponse object to be deserialized.
        :param response_type: class literal for
            deserialized object, or string of class name.

        :return: deserialized object.
        """
        # handle file downloading
        # save response body into a tmp file and return the instance
        if response_type == "file":
            return self.__deserialize_file(response)

        # fetch data from response object
        try:
            data = json.loads(response.data)
        except ValueError:
            data = response.data

        return self.__deserialize(data, response_type)

    def __deserialize(self, data, klass):
        """Deserializes dict, list, str into an object.

        :param data: dict, list or str.
        :param klass: class literal, or string of class name.

        :return: object.
        """
        if data is None:
            return None

        if type(klass) == str:
            if klass.startswith('list['):
                sub_kls = re.match(r'list\[(.*)\]', klass).group(1)
                return [self.__deserialize(sub_data, sub_kls)
                        for sub_data in data]

            if klass.startswith('dict('):
                sub_kls = re.match(r'dict\(([^,]*), (.*)\)', klass).group(2)
                return {k: self.__deserialize(v, sub_kls)
                        for k, v in six.iteritems(data)}

            # convert str to class
            if klass in self.NATIVE_TYPES_MAPPING:
                klass = self.NATIVE_TYPES_MAPPING[klass]
            else:
                klass = getattr(blapi.models, klass)

        if klass in self.PRIMITIVE_TYPES:
            return self.__deserialize_primitive(data, klass)
        elif klass == object:
            return self.__deserialize_object(data)
        elif klass == datetime.date:
            return self.__deserialize_date(data)
        elif klass == datetime.datetime:
            return self.__deserialize_datatime(data)
        else:
            return self.__deserialize_model(data, klass)

    def call_api(self, resource_path, method,
                 path_params=None, query_params=None, header_params=None,
                 body=None, post_params=None, files=None,
                 response_type=None, auth_settings=None, async_req=None,
                 _return_http_data_only=None, collection_formats=None,
                 _preload_content=True, _request_timeout=None):
        """Makes the HTTP request (synchronous) and returns deserialized data.

        To make an async request, set the async_req parameter.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be
            placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param auth_settings list: Auth Settings names for the request.
        :param response: Response data type.
        :param files dict: key -> filename, value -> filepath,
            for `multipart/form-data`.
        :param async_req bool: execute request asynchronously
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param collection_formats: dict of collection formats for path, query,
            header, and post parameters.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return:
            If async_req parameter is True,
            the request will be called asynchronously.
            The method will return the request thread.
            If parameter async_req is False or missing,
            then the method will return the response directly.
        """
        if not async_req:
            return self.__call_api(resource_path, method,
                                   path_params, query_params, header_params,
                                   body, post_params, files,
                                   response_type, auth_settings,
                                   _return_http_data_only, collection_formats,
                                   _preload_content, _request_timeout)
        else:
            thread = self.pool.apply_async(self.__call_api, (resource_path,
                                           method, path_params, query_params,
                                           header_params, body,
                                           post_params, files,
                                           response_type, auth_settings,
                                           _return_http_data_only,
                                           collection_formats,
                                           _preload_content, _request_timeout))
        return thread

    def request(self, method, url, query_params=None, headers=None,
                post_params=None, body=None, _preload_content=True,
                _request_timeout=None):
        """Makes the HTTP request using RESTClient."""
        if method == "GET":
            return self.rest_client.GET(url,
                                        query_params=query_params,
                                        _preload_content=_preload_content,
                                        _request_timeout=_request_timeout,
                                        headers=headers)
        elif method == "HEAD":
            return self.rest_client.HEAD(url,
                                         query_params=query_params,
                                         _preload_content=_preload_content,
                                         _request_timeout=_request_timeout,
                                         headers=headers)
        elif method == "OPTIONS":
            return self.rest_client.OPTIONS(url,
                                            query_params=query_params,
                                            headers=headers,
                                            post_params=post_params,
                                            _preload_content=_preload_content,
                                            _request_timeout=_request_timeout,
                                            body=body)
        elif method == "POST":
            return self.rest_client.POST(url,
                                         query_params=query_params,
                                         headers=headers,
                                         post_params=post_params,
                                         _preload_content=_preload_content,
                                         _request_timeout=_request_timeout,
                                         body=body)
        elif method == "PUT":
            return self.rest_client.PUT(url,
                                        query_params=query_params,
                                        headers=headers,
                                        post_params=post_params,
                                        _preload_content=_preload_content,
                                        _request_timeout=_request_timeout,
                                        body=body)
        elif method == "PATCH":
            return self.rest_client.PATCH(url,
                                          query_params=query_params,
                                          headers=headers,
                                          post_params=post_params,
                                          _preload_content=_preload_content,
                                          _request_timeout=_request_timeout,
                                          body=body)
        elif method == "DELETE":
            return self.rest_client.DELETE(url,
                                           query_params=query_params,
                                           headers=headers,
                                           _preload_content=_preload_content,
                                           _request_timeout=_request_timeout,
                                           body=body)
        else:
            raise ValueError(
                "http method must be `GET`, `HEAD`, `OPTIONS`,"
                " `POST`, `PATCH`, `PUT` or `DELETE`."
            )

    def parameters_to_tuples(self, params, collection_formats):
        """Get parameters as list of tuples, formatting collections.

        :param params: Parameters as dict or list of two-tuples
        :param dict collection_formats: Parameter collection formats
        :return: Parameters as list of tuples, collections formatted
        """
        new_params = []
        if collection_formats is None:
            collection_formats = {}
        for k, v in six.iteritems(params) if isinstance(params, dict) else params:  # noqa: E501
            if k in collection_formats:
                collection_format = collection_formats[k]
                if collection_format == 'multi':
                    new_params.extend((k, value) for value in v)
                else:
                    if collection_format == 'ssv':
                        delimiter = ' '
                    elif collection_format == 'tsv':
                        delimiter = '\t'
                    elif collection_format == 'pipes':
                        delimiter = '|'
                    else:  # csv is the default
                        delimiter = ','
                    new_params.append(
                        (k, delimiter.join(str(value) for value in v)))
            else:
                new_params.append((k, v))
        return new_params

    def prepare_post_parameters(self, post_params=None, files=None):
        """Builds form parameters.

        :param post_params: Normal form parameters.
        :param files: File parameters.
        :return: Form parameters with files.
        """
        params = []

        if post_params:
            params = post_params

        if files:
            for k, v in six.iteritems(files):
                if not v:
                    continue
                file_names = v if type(v) is list else [v]
                for n in file_names:
                    with open(n, 'rb') as f:
                        filename = os.path.basename(f.name)
                        filedata = f.read()
                        mimetype = (mimetypes.guess_type(filename)[0] or
                                    'application/octet-stream')
                        params.append(
                            tuple([k, tuple([filename, filedata, mimetype])]))

        return params

    def select_header_accept(self, accepts):
        """Returns `Accept` based on an array of accepts provided.

        :param accepts: List of headers.
        :return: Accept (e.g. application/json).
        """
        if not accepts:
            return

        accepts = [x.lower() for x in accepts]

        if 'application/json' in accepts:
            return 'application/json'
        else:
            return ', '.join(accepts)

    def select_header_content_type(self, content_types):
        """Returns `Content-Type` based on an array of content_types provided.

        :param content_types: List of content-types.
        :return: Content-Type (e.g. application/json).
        """
        if not content_types:
            return 'application/json'

        content_types = [x.lower() for x in content_types]

        if 'application/json' in content_types or '*/*' in content_types:
            return 'application/json'
        else:
            return content_types[0]

    def update_params_for_auth(self, headers, querys, auth_settings):
        """Updates header and query params based on authentication setting.

        :param headers: Header parameters dict to be updated.
        :param querys: Query parameters tuple list to be updated.
        :param auth_settings: Authentication setting identifiers list.
        """
        if not auth_settings:
            return

        for auth in auth_settings:
            auth_setting = self.configuration.auth_settings().get(auth)
            if auth_setting:
                if not auth_setting['value']:
                    continue
                elif auth_setting['in'] == 'header':
                    headers[auth_setting['key']] = auth_setting['value']
                elif auth_setting['in'] == 'query':
                    querys.append((auth_setting['key'], auth_setting['value']))
                else:
                    raise ValueError(
                        'Authentication token must be in `query` or `header`'
                    )

    def __deserialize_file(self, response):
        """Deserializes body to file

        Saves response body into a file in a temporary folder,
        using the filename from the `Content-Disposition` header if provided.

        :param response:  RESTResponse.
        :return: file path.
        """
        fd, path = tempfile.mkstemp(dir=self.configuration.temp_folder_path)
        os.close(fd)
        os.remove(path)

        content_disposition = response.getheader("Content-Disposition")
        if content_disposition:
            filename = re.search(r'filename=[\'"]?([^\'"\s]+)[\'"]?',
                                 content_disposition).group(1)
            path = os.path.join(os.path.dirname(path), filename)
            response_data = response.data
            with open(path, "wb") as f:
                if isinstance(response_data, str):
                    # change str to bytes so we can write it
                    response_data = response_data.encode('utf-8')
                    f.write(response_data)
                else:
                    f.write(response_data)
        return path

    def __deserialize_primitive(self, data, klass):
        """Deserializes string to primitive type.

        :param data: str.
        :param klass: class literal.

        :return: int, long, float, str, bool.
        """
        try:
            return klass(data)
        except UnicodeEncodeError:
            return six.text_type(data)
        except TypeError:
            return data

    def __deserialize_object(self, value):
        """Return a original value.

        :return: object.
        """
        return value

    def __deserialize_date(self, string):
        """Deserializes string to date.

        :param string: str.
        :return: date.
        """
        try:
            from dateutil.parser import parse
            return parse(string).date()
        except ImportError:
            return string
        except ValueError:
            raise rest.ApiException(
                status=0,
                reason="Failed to parse `{0}` as date object".format(string)
            )

    def __deserialize_datatime(self, string):
        """Deserializes string to datetime.

        The string should be in iso8601 datetime format.

        :param string: str.
        :return: datetime.
        """
        try:
            from dateutil.parser import parse
            return parse(string)
        except ImportError:
            return string
        except ValueError:
            raise rest.ApiException(
                status=0,
                reason=(
                    "Failed to parse `{0}` as datetime object"
                    .format(string)
                )
            )

    def __hasattr(self, object, name):
            return name in object.__class__.__dict__

    def __deserialize_model(self, data, klass):
        """Deserializes list or dict to model.

        :param data: dict, list.
        :param klass: class literal.
        :return: model object.
        """

        if not klass.swagger_types and not self.__hasattr(klass, 'get_real_child_model'):
            return data

        kwargs = {}
        if klass.swagger_types is not None:
            for attr, attr_type in six.iteritems(klass.swagger_types):
                if (data is not None and
                        klass.attribute_map[attr] in data and
                        isinstance(data, (list, dict))):
                    value = data[klass.attribute_map[attr]]
                    kwargs[attr] = self.__deserialize(value, attr_type)

        instance = klass(**kwargs)

        if (isinstance(instance, dict) and
                klass.swagger_types is not None and
                isinstance(data, dict)):
            for key, value in data.items():
                if key not in klass.swagger_types:
                    instance[key] = value
        if self.__hasattr(instance, 'get_real_child_model'):
            klass_name = instance.get_real_child_model(data)
            if klass_name:
                instance = self.__deserialize(data, klass_name)
        return instance
