# blapi.DatasetsApi

All URIs are relative to *https://api.bloomberg.com/eap*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dataset**](DatasetsApi.md#get_dataset) | **GET** /catalogs/{catalog}/datasets/{dataset}/ | Dataset definition and available snapshot resources
[**get_datasets**](DatasetsApi.md#get_datasets) | **GET** /catalogs/{catalog}/datasets/ | Datasets in this catalog

# **get_dataset**
> InlineResponse200 get_dataset(catalog, dataset, jwt, api_version)

Dataset definition and available snapshot resources

## Bulk Dataset In the [Bloomberg Catalog](#tag/catalogs), a `dataset` is a class of publication, containing a time series of [snapshots](#tag/snapshots). Each [snapshot](#tag/snapshots) is a point in the time series, which represents a single publication of the `dataset`.  ## Custom Dataset In an [Account Catalog](#tag/catalogs), each `dataset` represents a response to a user defined [request](#/tags/request) in that [catalog](#tag/catalogs). The custom `dataset` and the [snapshots](#tag/snapshots) container within it are created at the moment a [request](#tag/requests) is created. Individual [snapshot](#tag/snapshots) resources are added to the [snapshots](#tag/snapshots) container each time the [request](#tags/requests) is executed. 

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.DatasetsApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
dataset = 'dataset_example' # str | Dataset identifier
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.

try:
    # Dataset definition and available snapshot resources
    api_response = api_instance.get_dataset(catalog, dataset, jwt, api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetsApi->get_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 
 **dataset** | **str**| Dataset identifier | 
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_datasets**
> Datasets get_datasets(catalog, jwt, api_version, page=page, sort=sort, q=q, subscribed=subscribed, module_level1=module_level1, module_level2=module_level2, module_level3=module_level3, universe_label=universe_label, universe_subset_label=universe_subset_label, publisher=publisher)

Datasets in this catalog

## Bloomberg Catalog (Bulk Datasets) The [Bloomberg Catalog](#tag/catalogs) contains a collection of Bulk [datasets](#tag/datasets) defined and offered by Bloomberg Data License.  Access rights to Bulk `datasets` are determined through active subscriptions for the DL account that issued the requestor's credentials. Sample data is accessible for all Bulk `datasets`.  The `subscribed` property (which can be used as a query parameter) indicates if the requesting credentials are privileged to access non-sample [snapshots](#tag/snapshots) of each dataset.  ## Account Catalog (Custom Datasets) An [Account Catalog](#tag/catalogs) contains a collection of Bloomberg Data License responses ([datasets](#tag/datasets)) to the user defined [requests](#/tags/requests) that have been submitted to the same [catalog](#tag/catalogs).  Custom `datasets` are accessible to requestors using any credential issued by the DL account that submitted the [request](#tag/requests) 

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.DatasetsApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.
page = 56 # int | Page number to view (optional)
sort = 'sort_example' # str | Field to sort by. Accepted are relevance, title and -title. This is only applicable when catalog is `bbg`. (optional)
q = 'q_example' # str | Search terms. This is only applicable when catalog is `bbg`. (optional)
subscribed = true # bool | Subscription status. This is only applicable when catalog is `bbg`. (optional)
module_level1 = 'module_level1_example' # str | Filter by module level 1. This is only applicable when catalog is `bbg`. (optional)
module_level2 = 'module_level2_example' # str | Filter by module level 2. This is only applicable when catalog is `bbg`. (optional)
module_level3 = 'module_level3_example' # str | Filter by module level 3. This is only applicable when catalog is `bbg`. (optional)
universe_label = 'universe_label_example' # str | Filter by universe label. This is only applicable when catalog is `bbg`. (optional)
universe_subset_label = 'universe_subset_label_example' # str | Filter by universe subset label. This is only applicable when catalog is `bbg`. (optional)
publisher = 'publisher_example' # str | Filter by the publisher. This is only applicable when catalog is `bbg`. (optional)

try:
    # Datasets in this catalog
    api_response = api_instance.get_datasets(catalog, jwt, api_version, page=page, sort=sort, q=q, subscribed=subscribed, module_level1=module_level1, module_level2=module_level2, module_level3=module_level3, universe_label=universe_label, universe_subset_label=universe_subset_label, publisher=publisher)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetsApi->get_datasets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 
 **page** | **int**| Page number to view | [optional] 
 **sort** | **str**| Field to sort by. Accepted are relevance, title and -title. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **q** | **str**| Search terms. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **subscribed** | **bool**| Subscription status. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **module_level1** | **str**| Filter by module level 1. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **module_level2** | **str**| Filter by module level 2. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **module_level3** | **str**| Filter by module level 3. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **universe_label** | **str**| Filter by universe label. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **universe_subset_label** | **str**| Filter by universe subset label. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **publisher** | **str**| Filter by the publisher. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 

### Return type

[**Datasets**](Datasets.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

