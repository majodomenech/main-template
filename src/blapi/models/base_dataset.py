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

class BaseDataset(object):
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
        'type': 'AnyOfBaseDatasetType',
        'title': 'Title',
        'description': 'ExtendedDescription',
        'identifier': 'Identifier',
        'contains': 'Contains',
        'earliest_delivery': 'DatasetDelivery',
        'latest_delivery': 'DatasetDelivery',
        'module_level1': 'ModuleLevel1',
        'module_level2': 'ModuleLevel2',
        'module_level3': 'ModuleLevel3',
        'universe_label': 'UniverseLabel',
        'universe_subset_label': 'UniverseSubsetLabel',
        'publisher': 'Publisher',
        'primary_key': 'PrimaryKey'
    }

    attribute_map = {
        'context': '@context',
        'id': '@id',
        'type': '@type',
        'title': 'title',
        'description': 'description',
        'identifier': 'identifier',
        'contains': 'contains',
        'earliest_delivery': 'earliestDelivery',
        'latest_delivery': 'latestDelivery',
        'module_level1': 'moduleLevel1',
        'module_level2': 'moduleLevel2',
        'module_level3': 'moduleLevel3',
        'universe_label': 'universeLabel',
        'universe_subset_label': 'universeSubsetLabel',
        'publisher': 'publisher',
        'primary_key': 'primaryKey'
    }

    def __init__(self, context=None, id=None, type=None, title=None, description=None, identifier=None, contains=None, earliest_delivery=None, latest_delivery=None, module_level1=None, module_level2=None, module_level3=None, universe_label=None, universe_subset_label=None, publisher=None, primary_key=None):  # noqa: E501
        """BaseDataset - a model defined in Swagger"""  # noqa: E501
        self._context = None
        self._id = None
        self._type = None
        self._title = None
        self._description = None
        self._identifier = None
        self._contains = None
        self._earliest_delivery = None
        self._latest_delivery = None
        self._module_level1 = None
        self._module_level2 = None
        self._module_level3 = None
        self._universe_label = None
        self._universe_subset_label = None
        self._publisher = None
        self._primary_key = None
        self.discriminator = None
        self.context = context
        self.id = id
        self.type = type
        self.title = title
        self.description = description
        self.identifier = identifier
        self.contains = contains
        if earliest_delivery is not None:
            self.earliest_delivery = earliest_delivery
        if latest_delivery is not None:
            self.latest_delivery = latest_delivery
        if module_level1 is not None:
            self.module_level1 = module_level1
        if module_level2 is not None:
            self.module_level2 = module_level2
        if module_level3 is not None:
            self.module_level3 = module_level3
        if universe_label is not None:
            self.universe_label = universe_label
        if universe_subset_label is not None:
            self.universe_subset_label = universe_subset_label
        if publisher is not None:
            self.publisher = publisher
        if primary_key is not None:
            self.primary_key = primary_key

    @property
    def context(self):
        """Gets the context of this BaseDataset.  # noqa: E501


        :return: The context of this BaseDataset.  # noqa: E501
        :rtype: Context
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this BaseDataset.


        :param context: The context of this BaseDataset.  # noqa: E501
        :type: Context
        """
        if context is None:
            raise ValueError("Invalid value for `context`, must not be `None`")  # noqa: E501

        self._context = context

    @property
    def id(self):
        """Gets the id of this BaseDataset.  # noqa: E501


        :return: The id of this BaseDataset.  # noqa: E501
        :rtype: Id
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BaseDataset.


        :param id: The id of this BaseDataset.  # noqa: E501
        :type: Id
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def type(self):
        """Gets the type of this BaseDataset.  # noqa: E501


        :return: The type of this BaseDataset.  # noqa: E501
        :rtype: AnyOfBaseDatasetType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BaseDataset.


        :param type: The type of this BaseDataset.  # noqa: E501
        :type: AnyOfBaseDatasetType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def title(self):
        """Gets the title of this BaseDataset.  # noqa: E501


        :return: The title of this BaseDataset.  # noqa: E501
        :rtype: Title
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this BaseDataset.


        :param title: The title of this BaseDataset.  # noqa: E501
        :type: Title
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def description(self):
        """Gets the description of this BaseDataset.  # noqa: E501


        :return: The description of this BaseDataset.  # noqa: E501
        :rtype: ExtendedDescription
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BaseDataset.


        :param description: The description of this BaseDataset.  # noqa: E501
        :type: ExtendedDescription
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def identifier(self):
        """Gets the identifier of this BaseDataset.  # noqa: E501


        :return: The identifier of this BaseDataset.  # noqa: E501
        :rtype: Identifier
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this BaseDataset.


        :param identifier: The identifier of this BaseDataset.  # noqa: E501
        :type: Identifier
        """
        if identifier is None:
            raise ValueError("Invalid value for `identifier`, must not be `None`")  # noqa: E501

        self._identifier = identifier

    @property
    def contains(self):
        """Gets the contains of this BaseDataset.  # noqa: E501


        :return: The contains of this BaseDataset.  # noqa: E501
        :rtype: Contains
        """
        return self._contains

    @contains.setter
    def contains(self, contains):
        """Sets the contains of this BaseDataset.


        :param contains: The contains of this BaseDataset.  # noqa: E501
        :type: Contains
        """
        if contains is None:
            raise ValueError("Invalid value for `contains`, must not be `None`")  # noqa: E501

        self._contains = contains

    @property
    def earliest_delivery(self):
        """Gets the earliest_delivery of this BaseDataset.  # noqa: E501


        :return: The earliest_delivery of this BaseDataset.  # noqa: E501
        :rtype: DatasetDelivery
        """
        return self._earliest_delivery

    @earliest_delivery.setter
    def earliest_delivery(self, earliest_delivery):
        """Sets the earliest_delivery of this BaseDataset.


        :param earliest_delivery: The earliest_delivery of this BaseDataset.  # noqa: E501
        :type: DatasetDelivery
        """

        self._earliest_delivery = earliest_delivery

    @property
    def latest_delivery(self):
        """Gets the latest_delivery of this BaseDataset.  # noqa: E501


        :return: The latest_delivery of this BaseDataset.  # noqa: E501
        :rtype: DatasetDelivery
        """
        return self._latest_delivery

    @latest_delivery.setter
    def latest_delivery(self, latest_delivery):
        """Sets the latest_delivery of this BaseDataset.


        :param latest_delivery: The latest_delivery of this BaseDataset.  # noqa: E501
        :type: DatasetDelivery
        """

        self._latest_delivery = latest_delivery

    @property
    def module_level1(self):
        """Gets the module_level1 of this BaseDataset.  # noqa: E501


        :return: The module_level1 of this BaseDataset.  # noqa: E501
        :rtype: ModuleLevel1
        """
        return self._module_level1

    @module_level1.setter
    def module_level1(self, module_level1):
        """Sets the module_level1 of this BaseDataset.


        :param module_level1: The module_level1 of this BaseDataset.  # noqa: E501
        :type: ModuleLevel1
        """

        self._module_level1 = module_level1

    @property
    def module_level2(self):
        """Gets the module_level2 of this BaseDataset.  # noqa: E501


        :return: The module_level2 of this BaseDataset.  # noqa: E501
        :rtype: ModuleLevel2
        """
        return self._module_level2

    @module_level2.setter
    def module_level2(self, module_level2):
        """Sets the module_level2 of this BaseDataset.


        :param module_level2: The module_level2 of this BaseDataset.  # noqa: E501
        :type: ModuleLevel2
        """

        self._module_level2 = module_level2

    @property
    def module_level3(self):
        """Gets the module_level3 of this BaseDataset.  # noqa: E501


        :return: The module_level3 of this BaseDataset.  # noqa: E501
        :rtype: ModuleLevel3
        """
        return self._module_level3

    @module_level3.setter
    def module_level3(self, module_level3):
        """Sets the module_level3 of this BaseDataset.


        :param module_level3: The module_level3 of this BaseDataset.  # noqa: E501
        :type: ModuleLevel3
        """

        self._module_level3 = module_level3

    @property
    def universe_label(self):
        """Gets the universe_label of this BaseDataset.  # noqa: E501


        :return: The universe_label of this BaseDataset.  # noqa: E501
        :rtype: UniverseLabel
        """
        return self._universe_label

    @universe_label.setter
    def universe_label(self, universe_label):
        """Sets the universe_label of this BaseDataset.


        :param universe_label: The universe_label of this BaseDataset.  # noqa: E501
        :type: UniverseLabel
        """

        self._universe_label = universe_label

    @property
    def universe_subset_label(self):
        """Gets the universe_subset_label of this BaseDataset.  # noqa: E501


        :return: The universe_subset_label of this BaseDataset.  # noqa: E501
        :rtype: UniverseSubsetLabel
        """
        return self._universe_subset_label

    @universe_subset_label.setter
    def universe_subset_label(self, universe_subset_label):
        """Sets the universe_subset_label of this BaseDataset.


        :param universe_subset_label: The universe_subset_label of this BaseDataset.  # noqa: E501
        :type: UniverseSubsetLabel
        """

        self._universe_subset_label = universe_subset_label

    @property
    def publisher(self):
        """Gets the publisher of this BaseDataset.  # noqa: E501


        :return: The publisher of this BaseDataset.  # noqa: E501
        :rtype: Publisher
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        """Sets the publisher of this BaseDataset.


        :param publisher: The publisher of this BaseDataset.  # noqa: E501
        :type: Publisher
        """

        self._publisher = publisher

    @property
    def primary_key(self):
        """Gets the primary_key of this BaseDataset.  # noqa: E501


        :return: The primary_key of this BaseDataset.  # noqa: E501
        :rtype: PrimaryKey
        """
        return self._primary_key

    @primary_key.setter
    def primary_key(self, primary_key):
        """Sets the primary_key of this BaseDataset.


        :param primary_key: The primary_key of this BaseDataset.  # noqa: E501
        :type: PrimaryKey
        """

        self._primary_key = primary_key

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
        if issubclass(BaseDataset, dict):
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
        if not isinstance(other, BaseDataset):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
