# blapi.FieldListsApi

All URIs are relative to *https://api.bloomberg.com/eap*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_field_list**](FieldListsApi.md#delete_field_list) | **DELETE** /catalogs/{catalog}/fieldLists/{fieldListName}/ | Delete a field list resource
[**get_deleted_field_list**](FieldListsApi.md#get_deleted_field_list) | **GET** /catalogs/{catalog}/deleted/fieldLists/{fieldListUUID}/ | Deleted field list resource
[**get_field_list**](FieldListsApi.md#get_field_list) | **GET** /catalogs/{catalog}/fieldLists/{fieldListName}/ | A field list resource
[**get_field_lists**](FieldListsApi.md#get_field_lists) | **GET** /catalogs/{catalog}/fieldLists/ | A collection of field lists
[**patch_field_list**](FieldListsApi.md#patch_field_list) | **PATCH** /catalogs/{catalog}/fieldLists/{fieldListName}/ | Update a field list resource
[**post_field_list**](FieldListsApi.md#post_field_list) | **POST** /catalogs/{catalog}/fieldLists/ | Create a new field list resource

# **delete_field_list**
> delete_field_list(catalog, field_list_name, jwt, api_version)

Delete a field list resource

Field Lists that are referenced by active recurring requests CAN NOT be deleted and will return a status code of 400.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.FieldListsApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
field_list_name = 'field_list_name_example' # str | Field list name.
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.

try:
    # Delete a field list resource
    api_instance.delete_field_list(catalog, field_list_name, jwt, api_version)
except ApiException as e:
    print("Exception when calling FieldListsApi->delete_field_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 
 **field_list_name** | **str**| Field list name. | 
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

# **get_deleted_field_list**
> InlineResponse2002 get_deleted_field_list(catalog, field_list_uuid, jwt, api_version, page=page, page_size=page_size)

Deleted field list resource

A field list that has been deleted.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.FieldListsApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
field_list_uuid = 'field_list_uuid_example' # str | Field list unique identifier.
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.
page = 56 # int | Page number to view (optional)
page_size = 56 # int | Number of items per page. Defaults to 20 if not supplied. (optional)

try:
    # Deleted field list resource
    api_response = api_instance.get_deleted_field_list(catalog, field_list_uuid, jwt, api_version, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldListsApi->get_deleted_field_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 
 **field_list_uuid** | **str**| Field list unique identifier. | 
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 
 **page** | **int**| Page number to view | [optional] 
 **page_size** | **int**| Number of items per page. Defaults to 20 if not supplied. | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_field_list**
> FieldList get_field_list(catalog, field_list_name, jwt, api_version, page=page, page_size=page_size)

A field list resource

A field list resource.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.FieldListsApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
field_list_name = 'field_list_name_example' # str | Field list name.
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.
page = 56 # int | Page number to view (optional)
page_size = 56 # int | Number of items per page. Defaults to 20 if not supplied. (optional)

try:
    # A field list resource
    api_response = api_instance.get_field_list(catalog, field_list_name, jwt, api_version, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldListsApi->get_field_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 
 **field_list_name** | **str**| Field list name. | 
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

# **get_field_lists**
> FieldListCollection get_field_lists(catalog, jwt, api_version, page=page, page_size=page_size, type=type)

A collection of field lists

A collection of field lists within a specific catalog.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.FieldListsApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.
page = 56 # int | Page number to view (optional)
page_size = 56 # int | Number of items per page. Defaults to 20 if not supplied. (optional)
type = blapi.FieldListType() # FieldListType | Filter field lists by @type. If not supplied, no filtering is applied. (optional)

try:
    # A collection of field lists
    api_response = api_instance.get_field_lists(catalog, jwt, api_version, page=page, page_size=page_size, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldListsApi->get_field_lists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 
 **page** | **int**| Page number to view | [optional] 
 **page_size** | **int**| Number of items per page. Defaults to 20 if not supplied. | [optional] 
 **type** | [**FieldListType**](.md)| Filter field lists by @type. If not supplied, no filtering is applied. | [optional] 

### Return type

[**FieldListCollection**](FieldListCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_field_list**
> patch_field_list(body, jwt, api_version, content_type, catalog, field_list_name)

Update a field list resource

Field lists that have active requests referencing them CAN NOT be updated and will return a 400 status code.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.FieldListsApi()
body = blapi.FieldListPatchPayload() # FieldListPatchPayload | 
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.
content_type = 'content_type_example' # str | Media type (https://tools.ietf.org/html/rfc7231#section-3.1.1.5) of the POST/PATCH payload. Only 'application/json' is accepted. Any other format will result in a 400 (bad request).
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
field_list_name = 'field_list_name_example' # str | Field list name.

try:
    # Update a field list resource
    api_instance.patch_field_list(body, jwt, api_version, content_type, catalog, field_list_name)
except ApiException as e:
    print("Exception when calling FieldListsApi->patch_field_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FieldListPatchPayload**](FieldListPatchPayload.md)|  | 
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 
 **content_type** | **str**| Media type (https://tools.ietf.org/html/rfc7231#section-3.1.1.5) of the POST/PATCH payload. Only &#x27;application/json&#x27; is accepted. Any other format will result in a 400 (bad request). | 
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 
 **field_list_name** | **str**| Field list name. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/ld+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_field_list**
> Status post_field_list(body, jwt, api_version, content_type, catalog)

Create a new field list resource

Create a new field list resource. Requires an identifier (the name, used to construct the URI, must begin with a letter and consist only of alphanumeric characters), title (short description) and the contents.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.FieldListsApi()
body = blapi.FieldListPostPayload() # FieldListPostPayload | 
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.
content_type = 'content_type_example' # str | Media type (https://tools.ietf.org/html/rfc7231#section-3.1.1.5) of the POST/PATCH payload. Only 'application/json' is accepted. Any other format will result in a 400 (bad request).
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).

try:
    # Create a new field list resource
    api_response = api_instance.post_field_list(body, jwt, api_version, content_type, catalog)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldListsApi->post_field_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FieldListPostPayload**](FieldListPostPayload.md)|  | 
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

