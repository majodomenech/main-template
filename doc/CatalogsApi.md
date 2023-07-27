# blapi.CatalogsApi

All URIs are relative to *https://api.bloomberg.com/eap*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_catalog**](CatalogsApi.md#get_catalog) | **GET** /catalogs/{catalog}/ | Data resources in this catalog
[**get_catalogs**](CatalogsApi.md#get_catalogs) | **GET** /catalogs/ | Collection of available catalogs

# **get_catalog**
> Catalog get_catalog(jwt, api_version, catalog)

Data resources in this catalog

Both the [Bloomberg Catalog](#tag/catalogs) and an [Account Catalog](#tag/catalogs) comprise a collection of resource containers, comprising [datasets](#tag/datasets), [publishers](#tag/publishers), [fields](#tag/fields), [requests](#tag/requests), [universes](#tag/universes), [fieldLists](#tag/fieldLists) and [triggers](#tag/triggers). 

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.CatalogsApi()
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).

try:
    # Data resources in this catalog
    api_response = api_instance.get_catalog(jwt, api_version, catalog)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogsApi->get_catalog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 

### Return type

[**Catalog**](Catalog.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_catalogs**
> Catalogs get_catalogs(jwt, api_version)

Collection of available catalogs

Returns a collection of Bloomberg Data License catalogs, organized by Data License Account. DL REST API exposes the following [catalog](#tag/catalogs) resources (subject to access rights):  ## Bloomberg Catalog The Bloomberg catalog ([`/catalogs/bbg`](#tag/catalogs)) is visible to all DL REST API users.  ### Bulk Datasets The Bloomberg catalog contains Bulk datasets offered by Bloomberg Data License.  Access rights to these Bulk [datasets](#tag/datasets) are governed through Bloomberg Data License Bulk Agreements for the Account that issued the requestor's credentials. Samples of the Bulk [datasets](#tag/datasets) are available to all DL REST API users.  ### Metadata The Bloomberg catalog exposes [Fields](#tag/fields) and [publishers](#tag/publishers) metadata describing all Data License products to all DL REST API users.  ### Bloomberg Re-Usable Resources The Bloomberg catalog also provides containers of \"re-usable\" [universes](#tag/universes) and [fieldLists](#tag/fieldLists). These resources may be referenced through a request submitted through an Account `catalog`  ## Account Catalogs An Account Catalog ([`/catalogs/{catalog}`](#tag/catalogs)) and the resources in it are accessible only to a requestor using credentials issued for Bloomberg Data License account that is subject to a metered usage agreement, such as a Master Data Schedule (MDS) agreement.  ### Account Re-Usable Resources Each Account Catalog allows DL REST API users to create and maintain user-defined reusable resources than can be used to request a [Custom dataset](#tag/datasets). These re-usable resources, or components, comprise: ([requests](#tag/requests), [universes](#tag/universes), [fieldLists](#tag/fieldLists) and [triggers](#tag/triggers)).  The Account Catalog also provides the Bloomberg Data License responses ([datasets](#tag/datasets) to these requests. 

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.CatalogsApi()
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.

try:
    # Collection of available catalogs
    api_response = api_instance.get_catalogs(jwt, api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogsApi->get_catalogs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 

### Return type

[**Catalogs**](Catalogs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

