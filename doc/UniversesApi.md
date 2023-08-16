# blapi.UniversesApi

All URIs are relative to *https://api.bloomberg.com/eap*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_universe**](UniversesApi.md#delete_universe) | **DELETE** /catalogs/{catalog}/universes/{universeName}/ | Delete a Per Security universe
[**get_deleted_universe**](UniversesApi.md#get_deleted_universe) | **GET** /catalogs/{catalog}/deleted/universes/{universeUUID}/ | Deleted Per Security universe
[**get_universe**](UniversesApi.md#get_universe) | **GET** /catalogs/{catalog}/universes/{universeName}/ | Get a Per Security universe
[**get_universes**](UniversesApi.md#get_universes) | **GET** /catalogs/{catalog}/universes/ | List all Per Security universes
[**patch_universe**](UniversesApi.md#patch_universe) | **PATCH** /catalogs/{catalog}/universes/{universeName}/ | Update a Per Security universe
[**post_universe**](UniversesApi.md#post_universe) | **POST** /catalogs/{catalog}/universes/ | Create a new Per Security universe

# **delete_universe**
> delete_universe(catalog, universe_name, jwt, api_version)

Delete a Per Security universe

Universes that are referenced by active recurring requests CAN NOT be deleted and will return a status code of 400.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.UniversesApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
universe_name = 'universe_name_example' # str | Universe name.
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.

try:
    # Delete a Per Security universe
    api_instance.delete_universe(catalog, universe_name, jwt, api_version)
except ApiException as e:
    print("Exception when calling UniversesApi->delete_universe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 
 **universe_name** | **str**| Universe name. | 
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

# **get_deleted_universe**
> DeletedUniverse get_deleted_universe(catalog, universe_uuid, jwt, api_version, page=page, page_size=page_size, request_type=request_type)

Deleted Per Security universe

Universe that has been deleted.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.UniversesApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
universe_uuid = 'universe_uuid_example' # str | Universe unique identifier.
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.
page = 56 # int | Page number to view (optional)
page_size = 56 # int | Number of items per page. Defaults to 20 if not supplied. (optional)
request_type = 'request_type_example' # str | The type of the request. If this query parameter is provided, only those field overrides applicable to the request type will be returned in the `fieldOverrides` property. Those which are inapplicable to the request type will be returned in the `ignoredFieldOverrides` property. (optional)

try:
    # Deleted Per Security universe
    api_response = api_instance.get_deleted_universe(catalog, universe_uuid, jwt, api_version, page=page, page_size=page_size, request_type=request_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UniversesApi->get_deleted_universe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 
 **universe_uuid** | **str**| Universe unique identifier. | 
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 
 **page** | **int**| Page number to view | [optional] 
 **page_size** | **int**| Number of items per page. Defaults to 20 if not supplied. | [optional] 
 **request_type** | **str**| The type of the request. If this query parameter is provided, only those field overrides applicable to the request type will be returned in the &#x60;fieldOverrides&#x60; property. Those which are inapplicable to the request type will be returned in the &#x60;ignoredFieldOverrides&#x60; property. | [optional] 

### Return type

[**DeletedUniverse**](DeletedUniverse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_universe**
> Universe get_universe(catalog, universe_name, jwt, api_version, page=page, page_size=page_size, request_type=request_type)

Get a Per Security universe

Available content for the specified universe.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.UniversesApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
universe_name = 'universe_name_example' # str | Universe name.
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.
page = 56 # int | Page number to view (optional)
page_size = 56 # int | Number of items per page. Defaults to 20 if not supplied. (optional)
request_type = 'request_type_example' # str | The type of the request. If this query parameter is provided, only those field overrides applicable to the request type will be returned in the `fieldOverrides` property. Those which are inapplicable to the request type will be returned in the `ignoredFieldOverrides` property. (optional)

try:
    # Get a Per Security universe
    api_response = api_instance.get_universe(catalog, universe_name, jwt, api_version, page=page, page_size=page_size, request_type=request_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UniversesApi->get_universe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 
 **universe_name** | **str**| Universe name. | 
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 
 **page** | **int**| Page number to view | [optional] 
 **page_size** | **int**| Number of items per page. Defaults to 20 if not supplied. | [optional] 
 **request_type** | **str**| The type of the request. If this query parameter is provided, only those field overrides applicable to the request type will be returned in the &#x60;fieldOverrides&#x60; property. Those which are inapplicable to the request type will be returned in the &#x60;ignoredFieldOverrides&#x60; property. | [optional] 

### Return type

[**Universe**](Universe.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_universes**
> UniverseCollection get_universes(catalog, jwt, api_version, page=page, page_size=page_size)

List all Per Security universes

A collection of universes within a specific catalog.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.UniversesApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.
page = 56 # int | Page number to view (optional)
page_size = 56 # int | Number of items per page. Defaults to 20 if not supplied. (optional)

try:
    # List all Per Security universes
    api_response = api_instance.get_universes(catalog, jwt, api_version, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UniversesApi->get_universes: %s\n" % e)
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

[**UniverseCollection**](UniverseCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_universe**
> patch_universe(body, jwt, api_version, content_type, catalog, universe_name)

Update a Per Security universe

Please be aware that this will affect all requests that are actively referencing the universe being updated.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.UniversesApi()
body = blapi.UniversePatchPayload() # UniversePatchPayload | 
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.
content_type = 'content_type_example' # str | Media type (https://tools.ietf.org/html/rfc7231#section-3.1.1.5) of the POST/PATCH payload. Only 'application/json' is accepted. Any other format will result in a 400 (bad request).
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
universe_name = 'universe_name_example' # str | Universe name.

try:
    # Update a Per Security universe
    api_instance.patch_universe(body, jwt, api_version, content_type, catalog, universe_name)
except ApiException as e:
    print("Exception when calling UniversesApi->patch_universe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UniversePatchPayload**](UniversePatchPayload.md)|  | 
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 
 **content_type** | **str**| Media type (https://tools.ietf.org/html/rfc7231#section-3.1.1.5) of the POST/PATCH payload. Only &#x27;application/json&#x27; is accepted. Any other format will result in a 400 (bad request). | 
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 
 **universe_name** | **str**| Universe name. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/ld+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_universe**
> Status post_universe(body, jwt, api_version, content_type, catalog)

Create a new Per Security universe

Create a new universe resource. Requires an identifier (the name, used to construct the URI, must begin with a letter and consist only of alphanumeric characters), title (short description) and the contents.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.UniversesApi()
body = blapi.UniversePostPayload() # UniversePostPayload | 
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.
content_type = 'content_type_example' # str | Media type (https://tools.ietf.org/html/rfc7231#section-3.1.1.5) of the POST/PATCH payload. Only 'application/json' is accepted. Any other format will result in a 400 (bad request).
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).

try:
    # Create a new Per Security universe
    api_response = api_instance.post_universe(body, jwt, api_version, content_type, catalog)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UniversesApi->post_universe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UniversePostPayload**](UniversePostPayload.md)|  | 
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

