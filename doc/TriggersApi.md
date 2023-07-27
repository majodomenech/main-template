# blapi.TriggersApi

All URIs are relative to *https://api.bloomberg.com/eap*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_trigger**](TriggersApi.md#delete_trigger) | **DELETE** /catalogs/{catalog}/triggers/{triggerName}/ | Delete a trigger resource
[**get_deleted_trigger**](TriggersApi.md#get_deleted_trigger) | **GET** /catalogs/{catalog}/deleted/triggers/{triggerUUID}/ | Deleted trigger resource
[**get_trigger**](TriggersApi.md#get_trigger) | **GET** /catalogs/{catalog}/triggers/{triggerName}/ | A trigger resource
[**get_triggers**](TriggersApi.md#get_triggers) | **GET** /catalogs/{catalog}/triggers/ | A collection of triggers
[**patch_trigger**](TriggersApi.md#patch_trigger) | **PATCH** /catalogs/{catalog}/triggers/{triggerName}/ | Update a trigger resource
[**post_trigger**](TriggersApi.md#post_trigger) | **POST** /catalogs/{catalog}/triggers/ | Create a new trigger resource

# **delete_trigger**
> delete_trigger(catalog, trigger_name, jwt, api_version)

Delete a trigger resource

Triggers that are referenced by active recurring requests CAN NOT be deleted and will return a status code of 400

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.TriggersApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
trigger_name = 'trigger_name_example' # str | Trigger name.
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.

try:
    # Delete a trigger resource
    api_instance.delete_trigger(catalog, trigger_name, jwt, api_version)
except ApiException as e:
    print("Exception when calling TriggersApi->delete_trigger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 
 **trigger_name** | **str**| Trigger name. | 
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deleted_trigger**
> PolymorphicDeletedTrigger get_deleted_trigger(catalog, trigger_uuid, jwt, api_version)

Deleted trigger resource

A trigger that has been deleted.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.TriggersApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
trigger_uuid = 'trigger_uuid_example' # str | Trigger unique identifier.
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.

try:
    # Deleted trigger resource
    api_response = api_instance.get_deleted_trigger(catalog, trigger_uuid, jwt, api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TriggersApi->get_deleted_trigger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 
 **trigger_uuid** | **str**| Trigger unique identifier. | 
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 

### Return type

[**PolymorphicDeletedTrigger**](PolymorphicDeletedTrigger.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trigger**
> PolymorphicTrigger get_trigger(catalog, trigger_name, jwt, api_version)

A trigger resource

A trigger resource

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.TriggersApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
trigger_name = 'trigger_name_example' # str | Trigger name.
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.

try:
    # A trigger resource
    api_response = api_instance.get_trigger(catalog, trigger_name, jwt, api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TriggersApi->get_trigger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 
 **trigger_name** | **str**| Trigger name. | 
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 

### Return type

[**PolymorphicTrigger**](PolymorphicTrigger.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_triggers**
> TriggerCollection get_triggers(catalog, jwt, api_version, page=page, page_size=page_size)

A collection of triggers

A collection of triggers within a specific catalog.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.TriggersApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.
page = 56 # int | Page number to view (optional)
page_size = 56 # int | Number of items per page. Defaults to 20 if not supplied. (optional)

try:
    # A collection of triggers
    api_response = api_instance.get_triggers(catalog, jwt, api_version, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TriggersApi->get_triggers: %s\n" % e)
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

[**TriggerCollection**](TriggerCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_trigger**
> patch_trigger(body, jwt, api_version, content_type, catalog, trigger_name)

Update a trigger resource

Triggers that are referenced by active recurring requests CAN NOT be updated and will return a status code of 400.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.TriggersApi()
body = blapi.TriggerPatchPayload() # TriggerPatchPayload | 
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.
content_type = 'content_type_example' # str | Media type (https://tools.ietf.org/html/rfc7231#section-3.1.1.5) of the POST/PATCH payload. Only 'application/json' is accepted. Any other format will result in a 400 (bad request).
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
trigger_name = 'trigger_name_example' # str | Trigger name.

try:
    # Update a trigger resource
    api_instance.patch_trigger(body, jwt, api_version, content_type, catalog, trigger_name)
except ApiException as e:
    print("Exception when calling TriggersApi->patch_trigger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TriggerPatchPayload**](TriggerPatchPayload.md)|  | 
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 
 **content_type** | **str**| Media type (https://tools.ietf.org/html/rfc7231#section-3.1.1.5) of the POST/PATCH payload. Only &#x27;application/json&#x27; is accepted. Any other format will result in a 400 (bad request). | 
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 
 **trigger_name** | **str**| Trigger name. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/ld+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_trigger**
> Status post_trigger(body, jwt, api_version, content_type, catalog)

Create a new trigger resource

Create a new trigger resource. Requires an identifier (the name, used to construct the URI, must begin with a letter and consist only of alphanumeric characters), title (short description) and the contents  | Trigger @type | Action | Time Zone | Time Behavior | Frequency | Scheduling Behavior | | --- | --- | --- | --- | --- | --- | | ScheduledTrigger | Execute a DataRequest, HistoryRequest, or ActionsRequest | Billing region of requesting account. | If `startTime` is omitted and `startDate` is in the future, the request is scheduled for 00:00. If `startTime` is omitted and `startDate` is in the past, the request is scheduled immediately. |Once | If `startDate` and `startTime` have passed, execution is scheduled immediately. Otherwise request is scheduled for `startDate` and `startTime`. | | | | | | Recurring |  If `startDate` has passed, request submission will fail. Otherwise schedule begins at `startDate` and `startTime`. If `startDate` is omitted, it defaults to the next date for the `frequency`. | | SubmitTrigger | Execute a DataRequest, HistoryRequest, ActionsRequest, or TickHistoryRequest | Billing region of requesting account. | The request is scheduled for immediate execution. |Once | The request is scheduled for immediate execution. | | BvalSnapshotTrigger | Execute a BvalSnapshotRequest| `snapshotTimeZoneName` must be a valid [IANA](https://www.iana.org/time-zones) Time Zone Name and [BVAL snapshot timezone](/#section/Features/BVAL-Evaluated-Pricing) | `snapshotTime` must be a valid BVAL [snapshot time](/#section/Features/BVAL-Evaluated-Pricing) within `snapshotTimeZoneName`| Any | If  [cutoff](/#section/Features/BVAL-Evaluated-Pricing) has passed for the `snapshotDate` and `snapshotTime` provided, the request will be rejected. If `snapshotDate` is omitted the request will be scheduled for the next available `snapshotDate`.  | | PricingSnapshotTrigger | Execute a PricingSnapshotRequest | Pricing Snapshots are only supported in the Billing region of the requesting account. | `snapshotTime` must be, 0, 15, 30, or 45 minutes past the hour.  | Any | If [cutoff](/#section/Features/Pricing-Snapshots) has passed for the `snapshotDate` and `snapshotTime` provided, the request will be rejected. If `snapshotDate` is omitted the request will be scheduled for the next available `snapshotDate`. | 

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.TriggersApi()
body = blapi.TriggerPostPayload() # TriggerPostPayload | 
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.
content_type = 'content_type_example' # str | Media type (https://tools.ietf.org/html/rfc7231#section-3.1.1.5) of the POST/PATCH payload. Only 'application/json' is accepted. Any other format will result in a 400 (bad request).
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).

try:
    # Create a new trigger resource
    api_response = api_instance.post_trigger(body, jwt, api_version, content_type, catalog)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TriggersApi->post_trigger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TriggerPostPayload**](TriggerPostPayload.md)|  | 
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 
 **content_type** | **str**| Media type (https://tools.ietf.org/html/rfc7231#section-3.1.1.5) of the POST/PATCH payload. Only &#x27;application/json&#x27; is accepted. Any other format will result in a 400 (bad request). | 
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 

### Return type

[**Status**](Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/ld+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

