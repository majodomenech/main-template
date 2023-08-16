# blapi.RequestsApi

All URIs are relative to *https://api.bloomberg.com/eap*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_field_list_by_request**](RequestsApi.md#get_field_list_by_request) | **GET** /catalogs/{catalog}/requests/{requestName}/fieldList/ | Get the field list for a specific Per Security request
[**get_request**](RequestsApi.md#get_request) | **GET** /catalogs/{catalog}/requests/{requestName}/ | Get a Per Security request
[**get_requests**](RequestsApi.md#get_requests) | **GET** /catalogs/{catalog}/requests/ | List all Per Security requests
[**get_trigger_by_request**](RequestsApi.md#get_trigger_by_request) | **GET** /catalogs/{catalog}/requests/{requestName}/trigger/ | Get the trigger for a specific Per Security request
[**get_universe_by_request**](RequestsApi.md#get_universe_by_request) | **GET** /catalogs/{catalog}/requests/{requestName}/universe/ | Get the universe for a specific Per Security request
[**patch_request**](RequestsApi.md#patch_request) | **PATCH** /catalogs/{catalog}/requests/{requestName}/ | Update a Per Security request (e.g. cancel)
[**post_request**](RequestsApi.md#post_request) | **POST** /catalogs/{catalog}/requests/ | Create a new Per Security request

# **get_field_list_by_request**
> FieldList get_field_list_by_request(catalog, request_name, jwt, api_version, page=page, page_size=page_size)

Get the field list for a specific Per Security request

The field list for a specific Per Security request

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.RequestsApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
request_name = 'request_name_example' # str | Request name
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.
page = 56 # int | Page number to view (optional)
page_size = 56 # int | Number of items per page. Defaults to 20 if not supplied. (optional)

try:
    # Get the field list for a specific Per Security request
    api_response = api_instance.get_field_list_by_request(catalog, request_name, jwt, api_version, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RequestsApi->get_field_list_by_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 
 **request_name** | **str**| Request name | 
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 
 **page** | **int**| Page number to view | [optional] 
 **page_size** | **int**| Number of items per page. Defaults to 20 if not supplied. | [optional] 

### Return type

[**FieldList**](FieldList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_request**
> InlineResponse2003 get_request(catalog, request_name, jwt, api_version)

Get a Per Security request

A request resource

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.RequestsApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
request_name = 'request_name_example' # str | Request name
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.

try:
    # Get a Per Security request
    api_response = api_instance.get_request(catalog, request_name, jwt, api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RequestsApi->get_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 
 **request_name** | **str**| Request name | 
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_requests**
> RequestCollection get_requests(catalog, jwt, api_version, page=page, page_size=page_size)

List all Per Security requests

A collection of dataset requests within a catalog

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.RequestsApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.
page = 56 # int | Page number to view (optional)
page_size = 56 # int | Number of items per page. Defaults to 20 if not supplied. (optional)

try:
    # List all Per Security requests
    api_response = api_instance.get_requests(catalog, jwt, api_version, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RequestsApi->get_requests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 
 **page** | **int**| Page number to view | [optional] 
 **page_size** | **int**| Number of items per page. Defaults to 20 if not supplied. | [optional] 

### Return type

[**RequestCollection**](RequestCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trigger_by_request**
> InlineResponse2004 get_trigger_by_request(catalog, request_name, jwt, api_version)

Get the trigger for a specific Per Security request

The trigger for a specific Per Security request

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.RequestsApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
request_name = 'request_name_example' # str | Request name
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.

try:
    # Get the trigger for a specific Per Security request
    api_response = api_instance.get_trigger_by_request(catalog, request_name, jwt, api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RequestsApi->get_trigger_by_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 
 **request_name** | **str**| Request name | 
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_universe_by_request**
> Universe get_universe_by_request(catalog, request_name, jwt, api_version, page=page, page_size=page_size)

Get the universe for a specific Per Security request

The universe for a specific Per Security request

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.RequestsApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
request_name = 'request_name_example' # str | Request name
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.
page = 56 # int | Page number to view (optional)
page_size = 56 # int | Number of items per page. Defaults to 20 if not supplied. (optional)

try:
    # Get the universe for a specific Per Security request
    api_response = api_instance.get_universe_by_request(catalog, request_name, jwt, api_version, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RequestsApi->get_universe_by_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 
 **request_name** | **str**| Request name | 
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 
 **page** | **int**| Page number to view | [optional] 
 **page_size** | **int**| Number of items per page. Defaults to 20 if not supplied. | [optional] 

### Return type

[**Universe**](Universe.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_request**
> patch_request(body, jwt, api_version, content_type, catalog, request_name)

Update a Per Security request (e.g. cancel)

Update or disable a request.<p>The request's universe can be patched here; if, and only if, the request's universe is not a universe resource and then, can only be patched to another request level universe.</p>

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.RequestsApi()
body = blapi.RequestPatchPayload() # RequestPatchPayload | 
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.
content_type = 'content_type_example' # str | Media type (https://tools.ietf.org/html/rfc7231#section-3.1.1.5) of the POST/PATCH payload. Only 'application/json' is accepted. Any other format will result in a 400 (bad request).
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
request_name = 'request_name_example' # str | Request name

try:
    # Update a Per Security request (e.g. cancel)
    api_instance.patch_request(body, jwt, api_version, content_type, catalog, request_name)
except ApiException as e:
    print("Exception when calling RequestsApi->patch_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestPatchPayload**](RequestPatchPayload.md)|  | 
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 
 **content_type** | **str**| Media type (https://tools.ietf.org/html/rfc7231#section-3.1.1.5) of the POST/PATCH payload. Only &#x27;application/json&#x27; is accepted. Any other format will result in a 400 (bad request). | 
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 
 **request_name** | **str**| Request name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/ld+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_request**
> RequestCreatedStatus post_request(body, jwt, api_version, content_type, catalog)

Create a new Per Security request

A custom dataset request requires an identifier (the name, used to construct the URI, must begin with a letter and consist only of alphanumeric characters), title (short description) and the contents for a request.</p>  A request can define all dataset configuration including `universe`, `fieldList` and `trigger` details inside a single POST body. In this scenario these elements are not reusable and are available to the new request only. Optionally a request can be linked using IRIs to reusable [universe](#tag/universes), [fieldList](#tag/fieldLists) and [trigger](#tag/triggers) resources in either the `bbg` or client catalog.  Bloomberg provides lists of curated reusable universe and fieldList resources, a client can also define their own custom resources for reuse (see \"with linked resource\" examples for further context).  | Request @type | Description | Universe Evaluation | Security Level Overrides | Required FieldList @type | Required Trigger @type | | --- | --- | --- | --- | -- | -- | | DataRequest | A DataRequest generates output at a point in time for a Universe and FieldList on an ad-hoc or scheduled basis. | Execution time | Supported | DataFieldList | SubmitTrigger, ScheduledTrigger | | HistoryRequest | A HistoryRequest retrieves historical data fields for a Universe and FieldList within the given date range on an ad-hoc or scheduled basis. | Execution time |Not supported | HistoryFieldList | SubmitTrigger, ScheduledTrigger | | ActionsRequest | An ActionsRequest retrieves corporate actions for a Universe, within a specified range of dates. | Execution time | Not supported | Not applicable | SubmitTrigger, ScheduledTrigger | | BvalSnapshotRequest | A BvalSnapshotRequest schedules the snapshot and delivery of BVAL Evaluated Prices for a Universe. You can request a snapshot for [these times](/#section/Features/BVAL-Evaluated-Pricing). Response delivery times depend upon the `snapshotTier` you select.| BVAL securities are validated at approximately 00:00 (midnight) NY time. For BVAL (tier-1 and tier-2) scheduled requests, if users want to update the universe of securities, they will need to PATCH the saved universe prior to 00:00 (midnight) NY time in order for the changes to be reflected in the next scheduled BVAL snapshot runtime. | Pricing Source only | BvalSnapshotFieldList | BvalSnapshotTrigger | | PricingSnapshotRequest | A PricingSnapshotRequest provides a precise point in time snapshot of market prices for any instrument, available at 15 minute intervals throughout the day. The response will be delivered shortly after the snapshot time requested, subject to an embargo period for the requested instruments (see [Exchange Delay](https://data.bloomberg.com/catalogs/bbg/fields/exchangeDelay/)). | For requests submitted on `snapshotDate`, universe is evaluated at snapshot [cutoff](/#section/Features/Pricing-Snapshots). For requests submitted for a future `snapshotDate`, the universe is evaluated at midnight EDST on that `snapshotDate`. | Pricing Source Only | Not applicable | PricingSnapshotTrigger | | TickHistoryRequest | A TickHistoryRequest retrieves timestamped intraday execution prices, along with matching ask and bid prices, within the given date range on an ad-hoc basis. | Execution time | Not supported | Not applicable | SubmitTrigger | | EntityRequest | An EntityRequest retrieves entity-level reference data | Execution time | Not supported | EntityFieldList | SubmitTrigger, ScheduledTrigger |  Security level overrides are ignored where not supported. 

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.RequestsApi()
body = blapi.RequestPostPayload() # RequestPostPayload | 
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.
content_type = 'content_type_example' # str | Media type (https://tools.ietf.org/html/rfc7231#section-3.1.1.5) of the POST/PATCH payload. Only 'application/json' is accepted. Any other format will result in a 400 (bad request).
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).

try:
    # Create a new Per Security request
    api_response = api_instance.post_request(body, jwt, api_version, content_type, catalog)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RequestsApi->post_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestPostPayload**](RequestPostPayload.md)|  | 
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 
 **content_type** | **str**| Media type (https://tools.ietf.org/html/rfc7231#section-3.1.1.5) of the POST/PATCH payload. Only &#x27;application/json&#x27; is accepted. Any other format will result in a 400 (bad request). | 
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 

### Return type

[**RequestCreatedStatus**](RequestCreatedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/ld+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

