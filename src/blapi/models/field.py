# coding: utf-8

"""
    DL REST API

    # Overview [DATA&lt;GO&gt;](https://data.bloomberg.com) and [DL REST API](https://api.bloomberg.com/eap) are the Web interfaces for the Bloomberg Data License Platform. The [Data License Platform Guide](https://data.bloomberg.com/docs/data-license/) provides a general overview of the platform and its capabilities. DL REST API is the REST API for the Bloomberg Data License Platform, which powers [DATA&lt;GO&gt;](https://data.bloomberg.com).  You can use [DL REST API](https://api.bloomberg.com/eap) to access any capability or data that is accessible through [DATA&lt;GO&gt;](https://data.bloomberg.com): For example, to automate the retrieval of bulk datasets and Bloomberg metadata or, to request, schedule and retrieve custom datasets using reusable resources.   # Getting Started To get started with DL REST API, you need to : * Register your application at https://console.bloomberg.com/ * Obtain a set of credentials for your application at https://console.bloomberg.com/ * Add your IP address to the allowlist for your application at https://console.bloomberg.com/ * Download sample code at https://developer.bloomberg.com/portal/downloads * Use the sample code to connect to the [entrypoint](#tag/entrypoint) at https://api.bloomberg.com/eap/ * Explore DATA&lt;GO&gt;, a WEB UI that is powered by DL REST API, to get familiar with DL REST API concepts. Login at https://data.bloomberg.com/  ## Authentication and Authorization Each request to DL REST API must include a [JSON Web Token (JWT)](https://jwt.io/) header, unique to and matching the request. The token must be signed with a valid Data License credential (see [sample code](#section/Getting-Started)). The Data License Platform verifies that the token corresponds to the endpoint being requested and is unique. The Platform also checks the credential used to sign the token, to verify access rights to the resource being requested.  Credentials and permitted IP address allowlists are managed through https://console.bloomberg.com/.  The credentials must be : 1. Issued by a Data License account with active Bloomberg Data License agreements. 2. Unexpired 3. Configured with a permitted IP allowlist entry for the address issuing the request.  DL REST API supports server mode Authentication Flow. Hybrid and device modes are not supported.  Navigate to [DL REST APIConsole > Develop > Developer Documentation > API References > Authentication & Authorization](https://console.bloomberg.com/) to learn more about DL REST API authentication. ## Version Headers Every request to DL REST API must include an `api-version` header (set to `api-version` to 2 for the version described by this specification).  This is the only supported value for `api-version`.  Requests that do not set the `api-version` header, and requests that provide an unsupported `api-version` header value will be rejected with a 400 response code. Response headers include a `latest-api-version` which returns the latest available version of the api. ## Search * Many collection endpoints provide search templates that can be used to query them, including full text search. These are provided using the [Hydra](https://www.hydra-cg.com/spec/latest/core/) [`search`](https://www.hydra-cg.com/spec/latest/core/#hydra:search) property. * Ordering of the returned results is controlled by the `sort` query parameter. * Other sort fields such as `title` can be used * The default sort order is ascending. If the sort field is prefixed with `-` it will return results in descending order, e.g. https://api.bloomberg.com/eap/catalogs/bbg/datasets/?sort=-title ## Pagination * Paging sequence bounds for paged collections will always be indicated with `first` and `last` links (either in the LDP-Paging headers or in the Hydra PartialCollectionView). * Within a paging sequence, a `next` link will be present on all pages except the last and a `prev` link will be present on all pages except the first, to aid sequential traversal. * Pages beyond the paging sequence bounds will return a response with an empty collection. * Pages beyond the paging sequence bounds will not have `next` or `prev` links. * Pages that support the `pageSize` query parameter permit a user defined `pageSize`. ## Redirects * `latest` represents the most recently created resource in a particular collection. It is currently applicable for the `snapshots` endpoints. Since \"latest\" changes meaning over time, this a convenience shortcut rather than a canonical resource. * While Bloomberg Data License makes every effort to maintain stable URLs, API users should receive and process HTTP redirect codes, and must specify a header to determine the version of the API to which they are coding (this document describes version 2) . ## Rate Limiting The number of requests is currently limited to 1000 requests per second per IP address, and 1200 requests per minute per application. An application in this context is defined as a [Bloomberg Enterprise Console Application](https://console.bloomberg.com/). Any request rate greater than this number will be rejected with an HTTP error code of `429`. ## Compression By default all datasets (excluding parquet archives which are already compact) are returned uncompressed. You can negotiate gzip compression by setting the \"Accept-Encoding\" request header to \"gzip\" as per [rfc2612](https://tools.ietf.org/html/rfc2616#section-14.3).  # New Features ## JSON Output You can now request DataRequest, BvalSnapshotRequest and PricingSnapshotRequest datasets in either JSON and CSV format.   ## Mnemonics in CSV and JSON You can now standardize all your workflows using mnemonics as field identifiers on input and output. CSV and JSON output is now available with mnemonics as field identifiers. Where you submit or schedule a request using previous (\"old\") mnemonics, the output file will return the mnemonics as you requested them, ensuring your workflow remains stable over time. You may continue to use clean names where you already do so, but Bloomberg recommends that where possible and compatible with your existing systems, new workflows are implemented using mnemonics rather than clean names, in both the `fieldList` and the `request` output format specification.  ## Bulk Format Fields A bulk format field defines a nested or embedded schema. Bloomberg represents rich content that cannot be encoded in a single scalar value using bulk format fields. Bulk Format fields are now available in JSON, CSV and Bloomberg file formats. See [here](https://developer.bloomberg.com/portal/documents/per_security/getting_started_with_rest_api/1185__distributions_and_file_formats#processing_bulk_fields) for more details to understand bulk format fields and how they are encoded in each of the file formats.  ## Inline Resources (Single POST Request) Implement a simple atomic request operation in your workflow: The DL REST API now allows you submit or schedule a per security request in a single HTTP POST that defines the universe, fieldlist and trigger, and submits or schedules the request for execution. Refer to the [sample code](https://developer.bloomberg.com/portal/downloads), or \"Inline Universe\", \"Inline FieldList\" and \"Inline Trigger\" properties in the [request POST](#operation/postRequest) section of this specification.   Re-usable resources continue to be fully supported for advanced workflows where you need to share universes or fieldlists.  ## Resource Deletion Manage the universes, fieldlists and triggers in your catalog: The DL REST API now supports archival of these resources, where they are not currently referenced by an active request. Remove resources with an HTTP DELETE, and retrieve or recover deleted resources through the [deleted `universe`](#operation/getDeletedUniverse), [deleted `fieldlist`](#operation/getDeletedFieldList), and [deleted `trigger`](#operation/getDeletedTrigger) endpoints.  Refer the sections in this specification on deleting a [`universe`](#operation/deleteUniverse), [`fieldlist`](#operation/deleteFieldList), or [`trigger`](#operation/deleteTrigger) for more information.  # Features ## Entity Data Requests Bloomberg's Entity Data provides legal entity data for public and private companies, funds, government agencies, and municipalities. You can request Entity Data through DL REST API by POSTing a resource of type EntityRequest to /catalogs/{catalog}/requests/. * Legal Entity Identifiers (LEI) are supported for Entity Requests. * Field lists are strongly typed to match the Entity Data request type. * Security level overrides are ignored by Entity Requests. ## CSV Output You can now request DataRequest and BvalSnapshotRequest datasets in a standard [CSV](https://www.ietf.org/rfc/rfc4180.txt) format. CSV output from DL REST API is normalized to [XSD 1.1 types](https://www.w3.org/TR/xmlschema11-2/) such as xsd:boolean and xsd:date to facilitate ingestion.\" ## History Archives DL REST API now offers parquet time-series archives for subscribers to Bulk History products. - The `archives` endpoint allows you to discover and request parquet \"archives\" representing a time-series of snapshots of a dataset. It supports bitemporal search by as-of snapshot dates and by as-at issued date-times). - `archives` are published in two different forms, so you can select a publication model to  meet your workflow needs. - The first publication model is intended for clients ingesting data into a data lake or data science platform: Download archives of status \"final\" and \"current\" (an archive becomes final when it reaches 1GB), replacing the most recent \"current\" archive each day in your system until this becomes \"final\". - The second model is designed to drive an ETL process feeding an ODS or data warehouse. Download \"ongoing\" daily parquet archives as they become available, appending the data to the data have already collected. - Since parquet is a compact format,  DL REST API does not further compress parquet archives, so downloads must set the `Accept-Encoding` header to `Identity`. ## Push Notifications To avoid polling the REST APIs for new distributions, DL REST API provides an API for receiving push notifications when `distributions` become available. We provide a [W3C Server Sent Event Stream](https://html.spec.whatwg.org/multipage/server-sent-events.html) to push notifications to connected clients over HTTP. Subscribe to the event stream at the [`/notifications/sse`](#tag/sse) endpoint to receive push notifications of `DistributionPublishedActivity` events for Bulk and Custom [`dataset`](#tag/dataset) publications immediately when they are available. ## BVAL Evaluated Pricing Bloomberg's BVAL evaluated pricing service provides accurate and defensible pricing of fixed income and derivatives instruments. If you are a subscriber to the BVAL service, you can request a BVAL Snapshot through DL REST API by POSTing a resource of type `BvalSnapshotRequest` to [/catalogs/{catalog}/requests/](#operation/postRequest). You can expect the response to be delivered according to the `snapshotTier` you select. You should expect a Tier 1 response within 45 minutes of the snapshot time, and a Tier 2 response within 3 hours. You can also request BVAL prices after the snapshot time, through a `DataRequest`, using the pricing sources indicated in the table below.  ### BVAL Snapshots  BVAL Snapshots are available at the following snapshot times and can be specified in a `BvalSnapshotRequest` or `DataRequest`. DL REST API provides a [push notification](#section/New-Features/Push-Notifications) immediately that the response is available.  New York Early Close pricing is available on SIFMA Recommended Early Close days. The New York 15:00 snapshot will run at 13:00, and the New York 16:00 at 14:00. Enabled clients will receive their datasets at earlier times if they follow the submission guidelines below. Please contact your BVAL Sales representative to get enabled for Early Close pricing.  |Snapshot Time|Snapshot Timezone|SIFMA Early Close Snapshot Time|T1 Request By|T2 Request By|T1 Response By|T2 Response By| | --- | --- | --- | --- | --- | --- | --- | |15:00|America/New_York|13:00|17:30|15:00|15:45|18:00| |16:00|America/New_York|14:00|18:30|16:00|16:45|19:00| |12:00|Europe/London| |14:30|12:00|12:45|15:00| |15:00|Europe/London| |17:30|15:00|15:45|18:00| |16:15|Europe/London| |18:45|16:15|17:00|19:15| |15:00|Asia/Tokyo| |17:30|15:00|15:45|18:00| |16:00|Asia/Tokyo| |18:30|16:00|16:45|19:00| |17:00|Asia/Tokyo| |19:30|17:00|17:45|20:00| |17:00|Asia/Shanghai| |19:30|17:00|17:45|20:00| |17:00|Australia/Sydney| |19:30|17:00|17:45|20:00|  BVAL snapshots are available up to a cutoff time: The cutoff time is defined as 2.5 hours after the snapshot for a Tier 1 Request, and the snapshot time itself for a Tier 2 request.  ### BVAL Pricing Source (PCS) Requests The following pricing sources can also be specified in a `DataRequest`.  |Pricing Source|Comments|Snapshot Time|Snapshot Timezone| | --- | --- | --- | --- | | BVN3 | | 15:00 | America/New_York | | BVN4 | | 16:00 | America/New_York | | BL12 | | 12:00 | Europe/London | | BLN3 | | 15:00 | Europe/London | | BLN4 | | 16:15 | Europe/London | | BVT3 | | 15:00 | Asia/Tokyo | | BVT4 | | 16:00 | Asia/Tokyo | | BVT5 | | 17:00 | Asia/Tokyo | | BSH5 | | 17:00 | Asia/Shanghai | | BVS5 | | 17:00 | Australia/Sydney | | BVAL | Latest available BVAL Evaluated Price. | latest | any | | BVIC | Latest available BVAL Index Convention Price |latest | any |  ## Pricing Snapshots Bloomberg's Pricing Snapshots provide a precise point in time snapshot of market prices for any instrument, available at 15 minute intervals throughout the day. You can request a Pricing Snapshot through DL REST API by POSTing a resource of type PricingSnapshotRequest to [/catalogs/{catalog}/requests/](#operation/postRequest) up to 15 minutes prior to the snapshot time. The response will be delivered shortly after the snapshot time, subject to an embargo period for the requested instruments (see [Exchange Delay](https://data.bloomberg.com/catalogs/bbg/fields/exchangeDelay/)). ## History Requests Request a historic time series over a specified date range and period through DL REST API by POSTing a resource of type `HistoryRequest` to [/catalogs/{catalog}/requests/](#operation/postRequest). - In DL REST API V2, fieldLists are strongly typed to match the request type. DL REST API V1 fieldLists are only supported for `requests` of type `DataRequest` - Security level overrides are ignored by history requests. ## Corporate Actions Requests Request current and future corporate actions through DL REST API by POSTing a resource of type `ActionsRequest` to [/catalogs/{catalog}/requests/](#operation/postRequest). - Request corporate actions that will become effective up to two years in the future or that were recorded by Bloomberg up to seven days prior to request execution. - Review the metadata at https://data.bloomberg.com/documents/actions/ to understand the layout and content of the dataset for an `ActionsRequest`. - Corporate action requests do not require a `FieldList` - all available actions for the security and for its issuer are returned. - Security level overrides are ignored by corporate actions requests. ## Parallel and Resumable Downloads DL REST API supports fast and resumable parallel downloads using the HTTP range requests. This capability is available for all [distributions](#operation/getDistribution), using gzip encoding (set Accept-Encoding to gzip). Refer to the sample code at https://service.bloomberg.com/ for an example of a parallel download from DL REST API using range headers. ## Show Subscribed Datasets Filter by datasets to which you have subscribed with query parameter `subscribed=true` when getting [/catalogs/bbg/datasets/](#operation/getDatasets). ## Extended Pagination Specify page size against supported endpoints with query parameter `pageSize`. ## Request References Where a resource is referenced by an active (scheduled) request, and updates to that resource are restricted, the boolean property `referencedByActiveRequests` will be set to `true`. ## Detailed Error messages Responses are now provided in [JSON-API](https://jsonapi.org/) response format, including an [RFC6901](https://tools.ietf.org/html/rfc6901) pointer to each section of the submitted document that could not be processed.  # API Specification This is the specification for the Bloomberg Data License DL REST API ([DL REST API](https://api.bloomberg.com/eap)).   # noqa: E501

    OpenAPI spec version: 2.8.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Field(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'context': 'Context',
        'id': 'Id',
        'type': 'Types',
        'title': 'Title',
        'description': 'ExtendedDescription',
        'identifier': 'Identifier',
        'dl_bulk': 'DlBulk',
        'data_license': 'DataLicense',
        'platform_static': 'PlatformStatic',
        'platform_streaming': 'PlatformStreaming',
        'platform_terminal_required': 'PlatformTerminalRequired',
        'xsdtype': 'XsdType',
        'yk_commodity': 'YkComdty',
        'yk_corporate': 'YkCorp',
        'yk_currency': 'YkCurncy',
        'yk_equity': 'YkEquity',
        'yk_index': 'YkIndex',
        'yk_mortgage': 'YkMtge',
        'yk_money_market': 'YkMMkt',
        'yk_municipal': 'YkMuni',
        'yk_preferred': 'YkPfd',
        'yk_us_government': 'YkGovt',
        'created': 'Created',
        'dl_category': 'DlCategory',
        'dl_commercial_model_category': 'DlCommercialModelCategory',
        'dl_extended_bulk': 'DlExtendedBulk',
        'field_id': 'FieldId',
        'field_type': 'FieldType',
        'iri': 'Iri',
        'is_abstract': 'IsAbstract',
        'loading_speed': 'LoadingSpeed',
        'mnemonic': 'Mnemonic',
        'old_mnemonic': 'OldMnemonic',
        'range': 'Range',
        'sapi_new_security_setup': 'SapiNewSecuritySetup',
        'standard_decimal_places': 'StandardDecimalPlaces',
        'standard_width': 'StandardWidth',
        'super_property_iri': 'SuperPropertyIRI',
        'rdflang_string': 'RdfLangString',
        'xsdfraction_digits': 'XsdFractionDigits',
        'xsdlength': 'XsdLength',
        'xsdmax_exclusive': 'XsdMaxExclusive',
        'xsdmax_inclusive': 'XsdMaxInclusive',
        'xsdmax_length': 'XsdMaxLength',
        'xsdmin_exclusive': 'XsdMinExclusive',
        'xsdmin_inclusive': 'XsdMinInclusive',
        'xsdmin_length': 'XsdMinLength',
        'xsdpattern': 'XsdPattern',
        'bulk_schema': 'BulkSchema'
    }

    attribute_map = {
        'context': '@context',
        'id': '@id',
        'type': '@type',
        'title': 'title',
        'description': 'description',
        'identifier': 'identifier',
        'dl_bulk': 'DL:Bulk',
        'data_license': 'Data License',
        'platform_static': 'Platform: Static',
        'platform_streaming': 'Platform: Streaming',
        'platform_terminal_required': 'Platform: Terminal Required',
        'xsdtype': 'xsd:type',
        'yk_commodity': 'YK: Commodity',
        'yk_corporate': 'YK: Corporate',
        'yk_currency': 'YK: Currency',
        'yk_equity': 'YK: Equity',
        'yk_index': 'YK: Index',
        'yk_mortgage': 'YK: Mortgage',
        'yk_money_market': 'YK: Money Market',
        'yk_municipal': 'YK: Municipal',
        'yk_preferred': 'YK: Preferred',
        'yk_us_government': 'YK: US Government',
        'created': 'Created',
        'dl_category': 'DL Category',
        'dl_commercial_model_category': 'DL Commercial Model Category',
        'dl_extended_bulk': 'DL: Extended Bulk',
        'field_id': 'Field Id',
        'field_type': 'Field Type',
        'iri': 'IRI',
        'is_abstract': 'Is Abstract',
        'loading_speed': 'Loading Speed',
        'mnemonic': 'Mnemonic',
        'old_mnemonic': 'Old Mnemonic',
        'range': 'Range',
        'sapi_new_security_setup': 'SAPI New Security Setup',
        'standard_decimal_places': 'Standard Decimal Places',
        'standard_width': 'Standard Width',
        'super_property_iri': 'SuperPropertyIRI',
        'rdflang_string': 'rdf:langString',
        'xsdfraction_digits': 'xsd:fractionDigits',
        'xsdlength': 'xsd:length',
        'xsdmax_exclusive': 'xsd:maxExclusive',
        'xsdmax_inclusive': 'xsd:maxInclusive',
        'xsdmax_length': 'xsd:maxLength',
        'xsdmin_exclusive': 'xsd:minExclusive',
        'xsdmin_inclusive': 'xsd:minInclusive',
        'xsdmin_length': 'xsd:minLength',
        'xsdpattern': 'xsd:pattern',
        'bulk_schema': 'bulkSchema'
    }

    def __init__(self, context=None, id=None, type=None, title=None, description=None, identifier=None, dl_bulk=None, data_license=None, platform_static=None, platform_streaming=None, platform_terminal_required=None, xsdtype=None, yk_commodity=None, yk_corporate=None, yk_currency=None, yk_equity=None, yk_index=None, yk_mortgage=None, yk_money_market=None, yk_municipal=None, yk_preferred=None, yk_us_government=None, created=None, dl_category=None, dl_commercial_model_category=None, dl_extended_bulk=None, field_id=None, field_type=None, iri=None, is_abstract=None, loading_speed=None, mnemonic=None, old_mnemonic=None, range=None, sapi_new_security_setup=None, standard_decimal_places=None, standard_width=None, super_property_iri=None, rdflang_string=None, xsdfraction_digits=None, xsdlength=None, xsdmax_exclusive=None, xsdmax_inclusive=None, xsdmax_length=None, xsdmin_exclusive=None, xsdmin_inclusive=None, xsdmin_length=None, xsdpattern=None, bulk_schema=None):  # noqa: E501
        """Field - a model defined in Swagger"""  # noqa: E501
        self._context = None
        self._id = None
        self._type = None
        self._title = None
        self._description = None
        self._identifier = None
        self._dl_bulk = None
        self._data_license = None
        self._platform_static = None
        self._platform_streaming = None
        self._platform_terminal_required = None
        self._xsdtype = None
        self._yk_commodity = None
        self._yk_corporate = None
        self._yk_currency = None
        self._yk_equity = None
        self._yk_index = None
        self._yk_mortgage = None
        self._yk_money_market = None
        self._yk_municipal = None
        self._yk_preferred = None
        self._yk_us_government = None
        self._created = None
        self._dl_category = None
        self._dl_commercial_model_category = None
        self._dl_extended_bulk = None
        self._field_id = None
        self._field_type = None
        self._iri = None
        self._is_abstract = None
        self._loading_speed = None
        self._mnemonic = None
        self._old_mnemonic = None
        self._range = None
        self._sapi_new_security_setup = None
        self._standard_decimal_places = None
        self._standard_width = None
        self._super_property_iri = None
        self._rdflang_string = None
        self._xsdfraction_digits = None
        self._xsdlength = None
        self._xsdmax_exclusive = None
        self._xsdmax_inclusive = None
        self._xsdmax_length = None
        self._xsdmin_exclusive = None
        self._xsdmin_inclusive = None
        self._xsdmin_length = None
        self._xsdpattern = None
        self._bulk_schema = None
        self.discriminator = None
        self.context = context
        self.id = id
        self.type = type
        self.title = title
        self.description = description
        self.identifier = identifier
        if dl_bulk is not None:
            self.dl_bulk = dl_bulk
        if data_license is not None:
            self.data_license = data_license
        if platform_static is not None:
            self.platform_static = platform_static
        if platform_streaming is not None:
            self.platform_streaming = platform_streaming
        if platform_terminal_required is not None:
            self.platform_terminal_required = platform_terminal_required
        if xsdtype is not None:
            self.xsdtype = xsdtype
        if yk_commodity is not None:
            self.yk_commodity = yk_commodity
        if yk_corporate is not None:
            self.yk_corporate = yk_corporate
        if yk_currency is not None:
            self.yk_currency = yk_currency
        if yk_equity is not None:
            self.yk_equity = yk_equity
        if yk_index is not None:
            self.yk_index = yk_index
        if yk_mortgage is not None:
            self.yk_mortgage = yk_mortgage
        if yk_money_market is not None:
            self.yk_money_market = yk_money_market
        if yk_municipal is not None:
            self.yk_municipal = yk_municipal
        if yk_preferred is not None:
            self.yk_preferred = yk_preferred
        if yk_us_government is not None:
            self.yk_us_government = yk_us_government
        if created is not None:
            self.created = created
        if dl_category is not None:
            self.dl_category = dl_category
        if dl_commercial_model_category is not None:
            self.dl_commercial_model_category = dl_commercial_model_category
        if dl_extended_bulk is not None:
            self.dl_extended_bulk = dl_extended_bulk
        if field_id is not None:
            self.field_id = field_id
        if field_type is not None:
            self.field_type = field_type
        if iri is not None:
            self.iri = iri
        if is_abstract is not None:
            self.is_abstract = is_abstract
        if loading_speed is not None:
            self.loading_speed = loading_speed
        if mnemonic is not None:
            self.mnemonic = mnemonic
        if old_mnemonic is not None:
            self.old_mnemonic = old_mnemonic
        if range is not None:
            self.range = range
        if sapi_new_security_setup is not None:
            self.sapi_new_security_setup = sapi_new_security_setup
        if standard_decimal_places is not None:
            self.standard_decimal_places = standard_decimal_places
        if standard_width is not None:
            self.standard_width = standard_width
        if super_property_iri is not None:
            self.super_property_iri = super_property_iri
        if rdflang_string is not None:
            self.rdflang_string = rdflang_string
        if xsdfraction_digits is not None:
            self.xsdfraction_digits = xsdfraction_digits
        if xsdlength is not None:
            self.xsdlength = xsdlength
        if xsdmax_exclusive is not None:
            self.xsdmax_exclusive = xsdmax_exclusive
        if xsdmax_inclusive is not None:
            self.xsdmax_inclusive = xsdmax_inclusive
        if xsdmax_length is not None:
            self.xsdmax_length = xsdmax_length
        if xsdmin_exclusive is not None:
            self.xsdmin_exclusive = xsdmin_exclusive
        if xsdmin_inclusive is not None:
            self.xsdmin_inclusive = xsdmin_inclusive
        if xsdmin_length is not None:
            self.xsdmin_length = xsdmin_length
        if xsdpattern is not None:
            self.xsdpattern = xsdpattern
        if bulk_schema is not None:
            self.bulk_schema = bulk_schema

    @property
    def context(self):
        """Gets the context of this Field.  # noqa: E501


        :return: The context of this Field.  # noqa: E501
        :rtype: Context
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this Field.


        :param context: The context of this Field.  # noqa: E501
        :type: Context
        """
        if context is None:
            raise ValueError("Invalid value for `context`, must not be `None`")  # noqa: E501

        self._context = context

    @property
    def id(self):
        """Gets the id of this Field.  # noqa: E501


        :return: The id of this Field.  # noqa: E501
        :rtype: Id
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Field.


        :param id: The id of this Field.  # noqa: E501
        :type: Id
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def type(self):
        """Gets the type of this Field.  # noqa: E501


        :return: The type of this Field.  # noqa: E501
        :rtype: Types
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Field.


        :param type: The type of this Field.  # noqa: E501
        :type: Types
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def title(self):
        """Gets the title of this Field.  # noqa: E501


        :return: The title of this Field.  # noqa: E501
        :rtype: Title
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Field.


        :param title: The title of this Field.  # noqa: E501
        :type: Title
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def description(self):
        """Gets the description of this Field.  # noqa: E501


        :return: The description of this Field.  # noqa: E501
        :rtype: ExtendedDescription
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Field.


        :param description: The description of this Field.  # noqa: E501
        :type: ExtendedDescription
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def identifier(self):
        """Gets the identifier of this Field.  # noqa: E501


        :return: The identifier of this Field.  # noqa: E501
        :rtype: Identifier
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this Field.


        :param identifier: The identifier of this Field.  # noqa: E501
        :type: Identifier
        """
        if identifier is None:
            raise ValueError("Invalid value for `identifier`, must not be `None`")  # noqa: E501

        self._identifier = identifier

    @property
    def dl_bulk(self):
        """Gets the dl_bulk of this Field.  # noqa: E501


        :return: The dl_bulk of this Field.  # noqa: E501
        :rtype: DlBulk
        """
        return self._dl_bulk

    @dl_bulk.setter
    def dl_bulk(self, dl_bulk):
        """Sets the dl_bulk of this Field.


        :param dl_bulk: The dl_bulk of this Field.  # noqa: E501
        :type: DlBulk
        """

        self._dl_bulk = dl_bulk

    @property
    def data_license(self):
        """Gets the data_license of this Field.  # noqa: E501


        :return: The data_license of this Field.  # noqa: E501
        :rtype: DataLicense
        """
        return self._data_license

    @data_license.setter
    def data_license(self, data_license):
        """Sets the data_license of this Field.


        :param data_license: The data_license of this Field.  # noqa: E501
        :type: DataLicense
        """

        self._data_license = data_license

    @property
    def platform_static(self):
        """Gets the platform_static of this Field.  # noqa: E501


        :return: The platform_static of this Field.  # noqa: E501
        :rtype: PlatformStatic
        """
        return self._platform_static

    @platform_static.setter
    def platform_static(self, platform_static):
        """Sets the platform_static of this Field.


        :param platform_static: The platform_static of this Field.  # noqa: E501
        :type: PlatformStatic
        """

        self._platform_static = platform_static

    @property
    def platform_streaming(self):
        """Gets the platform_streaming of this Field.  # noqa: E501


        :return: The platform_streaming of this Field.  # noqa: E501
        :rtype: PlatformStreaming
        """
        return self._platform_streaming

    @platform_streaming.setter
    def platform_streaming(self, platform_streaming):
        """Sets the platform_streaming of this Field.


        :param platform_streaming: The platform_streaming of this Field.  # noqa: E501
        :type: PlatformStreaming
        """

        self._platform_streaming = platform_streaming

    @property
    def platform_terminal_required(self):
        """Gets the platform_terminal_required of this Field.  # noqa: E501


        :return: The platform_terminal_required of this Field.  # noqa: E501
        :rtype: PlatformTerminalRequired
        """
        return self._platform_terminal_required

    @platform_terminal_required.setter
    def platform_terminal_required(self, platform_terminal_required):
        """Sets the platform_terminal_required of this Field.


        :param platform_terminal_required: The platform_terminal_required of this Field.  # noqa: E501
        :type: PlatformTerminalRequired
        """

        self._platform_terminal_required = platform_terminal_required

    @property
    def xsdtype(self):
        """Gets the xsdtype of this Field.  # noqa: E501


        :return: The xsdtype of this Field.  # noqa: E501
        :rtype: XsdType
        """
        return self._xsdtype

    @xsdtype.setter
    def xsdtype(self, xsdtype):
        """Sets the xsdtype of this Field.


        :param xsdtype: The xsdtype of this Field.  # noqa: E501
        :type: XsdType
        """

        self._xsdtype = xsdtype

    @property
    def yk_commodity(self):
        """Gets the yk_commodity of this Field.  # noqa: E501


        :return: The yk_commodity of this Field.  # noqa: E501
        :rtype: YkComdty
        """
        return self._yk_commodity

    @yk_commodity.setter
    def yk_commodity(self, yk_commodity):
        """Sets the yk_commodity of this Field.


        :param yk_commodity: The yk_commodity of this Field.  # noqa: E501
        :type: YkComdty
        """

        self._yk_commodity = yk_commodity

    @property
    def yk_corporate(self):
        """Gets the yk_corporate of this Field.  # noqa: E501


        :return: The yk_corporate of this Field.  # noqa: E501
        :rtype: YkCorp
        """
        return self._yk_corporate

    @yk_corporate.setter
    def yk_corporate(self, yk_corporate):
        """Sets the yk_corporate of this Field.


        :param yk_corporate: The yk_corporate of this Field.  # noqa: E501
        :type: YkCorp
        """

        self._yk_corporate = yk_corporate

    @property
    def yk_currency(self):
        """Gets the yk_currency of this Field.  # noqa: E501


        :return: The yk_currency of this Field.  # noqa: E501
        :rtype: YkCurncy
        """
        return self._yk_currency

    @yk_currency.setter
    def yk_currency(self, yk_currency):
        """Sets the yk_currency of this Field.


        :param yk_currency: The yk_currency of this Field.  # noqa: E501
        :type: YkCurncy
        """

        self._yk_currency = yk_currency

    @property
    def yk_equity(self):
        """Gets the yk_equity of this Field.  # noqa: E501


        :return: The yk_equity of this Field.  # noqa: E501
        :rtype: YkEquity
        """
        return self._yk_equity

    @yk_equity.setter
    def yk_equity(self, yk_equity):
        """Sets the yk_equity of this Field.


        :param yk_equity: The yk_equity of this Field.  # noqa: E501
        :type: YkEquity
        """

        self._yk_equity = yk_equity

    @property
    def yk_index(self):
        """Gets the yk_index of this Field.  # noqa: E501


        :return: The yk_index of this Field.  # noqa: E501
        :rtype: YkIndex
        """
        return self._yk_index

    @yk_index.setter
    def yk_index(self, yk_index):
        """Sets the yk_index of this Field.


        :param yk_index: The yk_index of this Field.  # noqa: E501
        :type: YkIndex
        """

        self._yk_index = yk_index

    @property
    def yk_mortgage(self):
        """Gets the yk_mortgage of this Field.  # noqa: E501


        :return: The yk_mortgage of this Field.  # noqa: E501
        :rtype: YkMtge
        """
        return self._yk_mortgage

    @yk_mortgage.setter
    def yk_mortgage(self, yk_mortgage):
        """Sets the yk_mortgage of this Field.


        :param yk_mortgage: The yk_mortgage of this Field.  # noqa: E501
        :type: YkMtge
        """

        self._yk_mortgage = yk_mortgage

    @property
    def yk_money_market(self):
        """Gets the yk_money_market of this Field.  # noqa: E501


        :return: The yk_money_market of this Field.  # noqa: E501
        :rtype: YkMMkt
        """
        return self._yk_money_market

    @yk_money_market.setter
    def yk_money_market(self, yk_money_market):
        """Sets the yk_money_market of this Field.


        :param yk_money_market: The yk_money_market of this Field.  # noqa: E501
        :type: YkMMkt
        """

        self._yk_money_market = yk_money_market

    @property
    def yk_municipal(self):
        """Gets the yk_municipal of this Field.  # noqa: E501


        :return: The yk_municipal of this Field.  # noqa: E501
        :rtype: YkMuni
        """
        return self._yk_municipal

    @yk_municipal.setter
    def yk_municipal(self, yk_municipal):
        """Sets the yk_municipal of this Field.


        :param yk_municipal: The yk_municipal of this Field.  # noqa: E501
        :type: YkMuni
        """

        self._yk_municipal = yk_municipal

    @property
    def yk_preferred(self):
        """Gets the yk_preferred of this Field.  # noqa: E501


        :return: The yk_preferred of this Field.  # noqa: E501
        :rtype: YkPfd
        """
        return self._yk_preferred

    @yk_preferred.setter
    def yk_preferred(self, yk_preferred):
        """Sets the yk_preferred of this Field.


        :param yk_preferred: The yk_preferred of this Field.  # noqa: E501
        :type: YkPfd
        """

        self._yk_preferred = yk_preferred

    @property
    def yk_us_government(self):
        """Gets the yk_us_government of this Field.  # noqa: E501


        :return: The yk_us_government of this Field.  # noqa: E501
        :rtype: YkGovt
        """
        return self._yk_us_government

    @yk_us_government.setter
    def yk_us_government(self, yk_us_government):
        """Sets the yk_us_government of this Field.


        :param yk_us_government: The yk_us_government of this Field.  # noqa: E501
        :type: YkGovt
        """

        self._yk_us_government = yk_us_government

    @property
    def created(self):
        """Gets the created of this Field.  # noqa: E501


        :return: The created of this Field.  # noqa: E501
        :rtype: Created
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Field.


        :param created: The created of this Field.  # noqa: E501
        :type: Created
        """

        self._created = created

    @property
    def dl_category(self):
        """Gets the dl_category of this Field.  # noqa: E501


        :return: The dl_category of this Field.  # noqa: E501
        :rtype: DlCategory
        """
        return self._dl_category

    @dl_category.setter
    def dl_category(self, dl_category):
        """Sets the dl_category of this Field.


        :param dl_category: The dl_category of this Field.  # noqa: E501
        :type: DlCategory
        """

        self._dl_category = dl_category

    @property
    def dl_commercial_model_category(self):
        """Gets the dl_commercial_model_category of this Field.  # noqa: E501


        :return: The dl_commercial_model_category of this Field.  # noqa: E501
        :rtype: DlCommercialModelCategory
        """
        return self._dl_commercial_model_category

    @dl_commercial_model_category.setter
    def dl_commercial_model_category(self, dl_commercial_model_category):
        """Sets the dl_commercial_model_category of this Field.


        :param dl_commercial_model_category: The dl_commercial_model_category of this Field.  # noqa: E501
        :type: DlCommercialModelCategory
        """

        self._dl_commercial_model_category = dl_commercial_model_category

    @property
    def dl_extended_bulk(self):
        """Gets the dl_extended_bulk of this Field.  # noqa: E501


        :return: The dl_extended_bulk of this Field.  # noqa: E501
        :rtype: DlExtendedBulk
        """
        return self._dl_extended_bulk

    @dl_extended_bulk.setter
    def dl_extended_bulk(self, dl_extended_bulk):
        """Sets the dl_extended_bulk of this Field.


        :param dl_extended_bulk: The dl_extended_bulk of this Field.  # noqa: E501
        :type: DlExtendedBulk
        """

        self._dl_extended_bulk = dl_extended_bulk

    @property
    def field_id(self):
        """Gets the field_id of this Field.  # noqa: E501


        :return: The field_id of this Field.  # noqa: E501
        :rtype: FieldId
        """
        return self._field_id

    @field_id.setter
    def field_id(self, field_id):
        """Sets the field_id of this Field.


        :param field_id: The field_id of this Field.  # noqa: E501
        :type: FieldId
        """

        self._field_id = field_id

    @property
    def field_type(self):
        """Gets the field_type of this Field.  # noqa: E501


        :return: The field_type of this Field.  # noqa: E501
        :rtype: FieldType
        """
        return self._field_type

    @field_type.setter
    def field_type(self, field_type):
        """Sets the field_type of this Field.


        :param field_type: The field_type of this Field.  # noqa: E501
        :type: FieldType
        """

        self._field_type = field_type

    @property
    def iri(self):
        """Gets the iri of this Field.  # noqa: E501


        :return: The iri of this Field.  # noqa: E501
        :rtype: Iri
        """
        return self._iri

    @iri.setter
    def iri(self, iri):
        """Sets the iri of this Field.


        :param iri: The iri of this Field.  # noqa: E501
        :type: Iri
        """

        self._iri = iri

    @property
    def is_abstract(self):
        """Gets the is_abstract of this Field.  # noqa: E501


        :return: The is_abstract of this Field.  # noqa: E501
        :rtype: IsAbstract
        """
        return self._is_abstract

    @is_abstract.setter
    def is_abstract(self, is_abstract):
        """Sets the is_abstract of this Field.


        :param is_abstract: The is_abstract of this Field.  # noqa: E501
        :type: IsAbstract
        """

        self._is_abstract = is_abstract

    @property
    def loading_speed(self):
        """Gets the loading_speed of this Field.  # noqa: E501


        :return: The loading_speed of this Field.  # noqa: E501
        :rtype: LoadingSpeed
        """
        return self._loading_speed

    @loading_speed.setter
    def loading_speed(self, loading_speed):
        """Sets the loading_speed of this Field.


        :param loading_speed: The loading_speed of this Field.  # noqa: E501
        :type: LoadingSpeed
        """

        self._loading_speed = loading_speed

    @property
    def mnemonic(self):
        """Gets the mnemonic of this Field.  # noqa: E501


        :return: The mnemonic of this Field.  # noqa: E501
        :rtype: Mnemonic
        """
        return self._mnemonic

    @mnemonic.setter
    def mnemonic(self, mnemonic):
        """Sets the mnemonic of this Field.


        :param mnemonic: The mnemonic of this Field.  # noqa: E501
        :type: Mnemonic
        """

        self._mnemonic = mnemonic

    @property
    def old_mnemonic(self):
        """Gets the old_mnemonic of this Field.  # noqa: E501


        :return: The old_mnemonic of this Field.  # noqa: E501
        :rtype: OldMnemonic
        """
        return self._old_mnemonic

    @old_mnemonic.setter
    def old_mnemonic(self, old_mnemonic):
        """Sets the old_mnemonic of this Field.


        :param old_mnemonic: The old_mnemonic of this Field.  # noqa: E501
        :type: OldMnemonic
        """

        self._old_mnemonic = old_mnemonic

    @property
    def range(self):
        """Gets the range of this Field.  # noqa: E501


        :return: The range of this Field.  # noqa: E501
        :rtype: Range
        """
        return self._range

    @range.setter
    def range(self, range):
        """Sets the range of this Field.


        :param range: The range of this Field.  # noqa: E501
        :type: Range
        """

        self._range = range

    @property
    def sapi_new_security_setup(self):
        """Gets the sapi_new_security_setup of this Field.  # noqa: E501


        :return: The sapi_new_security_setup of this Field.  # noqa: E501
        :rtype: SapiNewSecuritySetup
        """
        return self._sapi_new_security_setup

    @sapi_new_security_setup.setter
    def sapi_new_security_setup(self, sapi_new_security_setup):
        """Sets the sapi_new_security_setup of this Field.


        :param sapi_new_security_setup: The sapi_new_security_setup of this Field.  # noqa: E501
        :type: SapiNewSecuritySetup
        """

        self._sapi_new_security_setup = sapi_new_security_setup

    @property
    def standard_decimal_places(self):
        """Gets the standard_decimal_places of this Field.  # noqa: E501


        :return: The standard_decimal_places of this Field.  # noqa: E501
        :rtype: StandardDecimalPlaces
        """
        return self._standard_decimal_places

    @standard_decimal_places.setter
    def standard_decimal_places(self, standard_decimal_places):
        """Sets the standard_decimal_places of this Field.


        :param standard_decimal_places: The standard_decimal_places of this Field.  # noqa: E501
        :type: StandardDecimalPlaces
        """

        self._standard_decimal_places = standard_decimal_places

    @property
    def standard_width(self):
        """Gets the standard_width of this Field.  # noqa: E501


        :return: The standard_width of this Field.  # noqa: E501
        :rtype: StandardWidth
        """
        return self._standard_width

    @standard_width.setter
    def standard_width(self, standard_width):
        """Sets the standard_width of this Field.


        :param standard_width: The standard_width of this Field.  # noqa: E501
        :type: StandardWidth
        """

        self._standard_width = standard_width

    @property
    def super_property_iri(self):
        """Gets the super_property_iri of this Field.  # noqa: E501


        :return: The super_property_iri of this Field.  # noqa: E501
        :rtype: SuperPropertyIRI
        """
        return self._super_property_iri

    @super_property_iri.setter
    def super_property_iri(self, super_property_iri):
        """Sets the super_property_iri of this Field.


        :param super_property_iri: The super_property_iri of this Field.  # noqa: E501
        :type: SuperPropertyIRI
        """

        self._super_property_iri = super_property_iri

    @property
    def rdflang_string(self):
        """Gets the rdflang_string of this Field.  # noqa: E501


        :return: The rdflang_string of this Field.  # noqa: E501
        :rtype: RdfLangString
        """
        return self._rdflang_string

    @rdflang_string.setter
    def rdflang_string(self, rdflang_string):
        """Sets the rdflang_string of this Field.


        :param rdflang_string: The rdflang_string of this Field.  # noqa: E501
        :type: RdfLangString
        """

        self._rdflang_string = rdflang_string

    @property
    def xsdfraction_digits(self):
        """Gets the xsdfraction_digits of this Field.  # noqa: E501


        :return: The xsdfraction_digits of this Field.  # noqa: E501
        :rtype: XsdFractionDigits
        """
        return self._xsdfraction_digits

    @xsdfraction_digits.setter
    def xsdfraction_digits(self, xsdfraction_digits):
        """Sets the xsdfraction_digits of this Field.


        :param xsdfraction_digits: The xsdfraction_digits of this Field.  # noqa: E501
        :type: XsdFractionDigits
        """

        self._xsdfraction_digits = xsdfraction_digits

    @property
    def xsdlength(self):
        """Gets the xsdlength of this Field.  # noqa: E501


        :return: The xsdlength of this Field.  # noqa: E501
        :rtype: XsdLength
        """
        return self._xsdlength

    @xsdlength.setter
    def xsdlength(self, xsdlength):
        """Sets the xsdlength of this Field.


        :param xsdlength: The xsdlength of this Field.  # noqa: E501
        :type: XsdLength
        """

        self._xsdlength = xsdlength

    @property
    def xsdmax_exclusive(self):
        """Gets the xsdmax_exclusive of this Field.  # noqa: E501


        :return: The xsdmax_exclusive of this Field.  # noqa: E501
        :rtype: XsdMaxExclusive
        """
        return self._xsdmax_exclusive

    @xsdmax_exclusive.setter
    def xsdmax_exclusive(self, xsdmax_exclusive):
        """Sets the xsdmax_exclusive of this Field.


        :param xsdmax_exclusive: The xsdmax_exclusive of this Field.  # noqa: E501
        :type: XsdMaxExclusive
        """

        self._xsdmax_exclusive = xsdmax_exclusive

    @property
    def xsdmax_inclusive(self):
        """Gets the xsdmax_inclusive of this Field.  # noqa: E501


        :return: The xsdmax_inclusive of this Field.  # noqa: E501
        :rtype: XsdMaxInclusive
        """
        return self._xsdmax_inclusive

    @xsdmax_inclusive.setter
    def xsdmax_inclusive(self, xsdmax_inclusive):
        """Sets the xsdmax_inclusive of this Field.


        :param xsdmax_inclusive: The xsdmax_inclusive of this Field.  # noqa: E501
        :type: XsdMaxInclusive
        """

        self._xsdmax_inclusive = xsdmax_inclusive

    @property
    def xsdmax_length(self):
        """Gets the xsdmax_length of this Field.  # noqa: E501


        :return: The xsdmax_length of this Field.  # noqa: E501
        :rtype: XsdMaxLength
        """
        return self._xsdmax_length

    @xsdmax_length.setter
    def xsdmax_length(self, xsdmax_length):
        """Sets the xsdmax_length of this Field.


        :param xsdmax_length: The xsdmax_length of this Field.  # noqa: E501
        :type: XsdMaxLength
        """

        self._xsdmax_length = xsdmax_length

    @property
    def xsdmin_exclusive(self):
        """Gets the xsdmin_exclusive of this Field.  # noqa: E501


        :return: The xsdmin_exclusive of this Field.  # noqa: E501
        :rtype: XsdMinExclusive
        """
        return self._xsdmin_exclusive

    @xsdmin_exclusive.setter
    def xsdmin_exclusive(self, xsdmin_exclusive):
        """Sets the xsdmin_exclusive of this Field.


        :param xsdmin_exclusive: The xsdmin_exclusive of this Field.  # noqa: E501
        :type: XsdMinExclusive
        """

        self._xsdmin_exclusive = xsdmin_exclusive

    @property
    def xsdmin_inclusive(self):
        """Gets the xsdmin_inclusive of this Field.  # noqa: E501


        :return: The xsdmin_inclusive of this Field.  # noqa: E501
        :rtype: XsdMinInclusive
        """
        return self._xsdmin_inclusive

    @xsdmin_inclusive.setter
    def xsdmin_inclusive(self, xsdmin_inclusive):
        """Sets the xsdmin_inclusive of this Field.


        :param xsdmin_inclusive: The xsdmin_inclusive of this Field.  # noqa: E501
        :type: XsdMinInclusive
        """

        self._xsdmin_inclusive = xsdmin_inclusive

    @property
    def xsdmin_length(self):
        """Gets the xsdmin_length of this Field.  # noqa: E501


        :return: The xsdmin_length of this Field.  # noqa: E501
        :rtype: XsdMinLength
        """
        return self._xsdmin_length

    @xsdmin_length.setter
    def xsdmin_length(self, xsdmin_length):
        """Sets the xsdmin_length of this Field.


        :param xsdmin_length: The xsdmin_length of this Field.  # noqa: E501
        :type: XsdMinLength
        """

        self._xsdmin_length = xsdmin_length

    @property
    def xsdpattern(self):
        """Gets the xsdpattern of this Field.  # noqa: E501


        :return: The xsdpattern of this Field.  # noqa: E501
        :rtype: XsdPattern
        """
        return self._xsdpattern

    @xsdpattern.setter
    def xsdpattern(self, xsdpattern):
        """Sets the xsdpattern of this Field.


        :param xsdpattern: The xsdpattern of this Field.  # noqa: E501
        :type: XsdPattern
        """

        self._xsdpattern = xsdpattern

    @property
    def bulk_schema(self):
        """Gets the bulk_schema of this Field.  # noqa: E501


        :return: The bulk_schema of this Field.  # noqa: E501
        :rtype: BulkSchema
        """
        return self._bulk_schema

    @bulk_schema.setter
    def bulk_schema(self, bulk_schema):
        """Sets the bulk_schema of this Field.


        :param bulk_schema: The bulk_schema of this Field.  # noqa: E501
        :type: BulkSchema
        """

        self._bulk_schema = bulk_schema

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Field, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Field):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
