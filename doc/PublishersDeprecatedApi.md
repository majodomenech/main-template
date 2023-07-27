# blapi.PublishersDeprecatedApi

All URIs are relative to *https://api.bloomberg.com/eap*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogs_bbg_publishers_get**](PublishersDeprecatedApi.md#catalogs_bbg_publishers_get) | **GET** /catalogs/bbg/publishers/ | A collection of Publisher resources
[**catalogs_bbg_publishers_publisher_name_get**](PublishersDeprecatedApi.md#catalogs_bbg_publishers_publisher_name_get) | **GET** /catalogs/bbg/publishers/{publisherName}/ | Metadata for a publisher

# **catalogs_bbg_publishers_get**
> catalogs_bbg_publishers_get(jwt, api_version, page=page, sort=sort, q=q)

A collection of Publisher resources

A collection of [(Dublin Core)](http://dublincore.org/documents/dcmi-terms/#terms-publisher) `Publishers`, which are used as a primary means of classifying each [Bulk Dataset](#tag/datasets) in the [Bloomberg Catalog](#tag/catalogs). `Publishers` are provided to support the exploration and discovery of [Bulk Datasets](#tag/datasets). Each [publisher](#tag/publishers) is annotated with a dataset count and facetted search URL to list the [datasets](#tag/datasets) offered by that [publisher](#tag/publishers). 

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.PublishersDeprecatedApi()
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.
page = 56 # int | Page number to view (optional)
sort = 'sort_example' # str | Field to sort by. Accepted are relevance, title and -title. This is only applicable when catalog is `bbg`. (optional)
q = 'q_example' # str | Search terms. This is only applicable when catalog is `bbg`. (optional)

try:
    # A collection of Publisher resources
    api_instance.catalogs_bbg_publishers_get(jwt, api_version, page=page, sort=sort, q=q)
except ApiException as e:
    print("Exception when calling PublishersDeprecatedApi->catalogs_bbg_publishers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 
 **page** | **int**| Page number to view | [optional] 
 **sort** | **str**| Field to sort by. Accepted are relevance, title and -title. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **q** | **str**| Search terms. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json-ld, application/ld+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalogs_bbg_publishers_publisher_name_get**
> catalogs_bbg_publishers_publisher_name_get(publisher_name, jwt, api_version)

Metadata for a publisher

A single [(Dublin Core)](http://dublincore.org/documents/dcmi-terms/#terms-publisher) `Publisher`, which exists to classify a group of [Bulk Datasets](#tag/datasets) in the [Bloomberg Catalog](#tag/catalogs). Each [publisher](#tag/publishers) is annotated with a dataset count and facetted search URL to list the [datasets](#tag/datasets) offered by that [publisher](#tag/publishers). 

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.PublishersDeprecatedApi()
publisher_name = 'publisher_name_example' # str | Publisher name
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.

try:
    # Metadata for a publisher
    api_instance.catalogs_bbg_publishers_publisher_name_get(publisher_name, jwt, api_version)
except ApiException as e:
    print("Exception when calling PublishersDeprecatedApi->catalogs_bbg_publishers_publisher_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publisher_name** | **str**| Publisher name | 
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json-ld, application/ld+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

