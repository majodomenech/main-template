# blapi.MethodsApi

All URIs are relative to *https://api.bloomberg.com/eap*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogs_bbg_publishers_head**](MethodsApi.md#catalogs_bbg_publishers_head) | **HEAD** /catalogs/bbg/publishers/ | Headers for a collection of Publisher resources
[**catalogs_bbg_publishers_options**](MethodsApi.md#catalogs_bbg_publishers_options) | **OPTIONS** /catalogs/bbg/publishers/ | Options for a collection of Publisher resources
[**catalogs_bbg_publishers_publisher_name_head**](MethodsApi.md#catalogs_bbg_publishers_publisher_name_head) | **HEAD** /catalogs/bbg/publishers/{publisherName}/ | Headers for metadata for a publisher
[**catalogs_bbg_publishers_publisher_name_options**](MethodsApi.md#catalogs_bbg_publishers_publisher_name_options) | **OPTIONS** /catalogs/bbg/publishers/{publisherName}/ | Options for metadata for a publisher
[**head_archive**](MethodsApi.md#head_archive) | **HEAD** /catalogs/{catalog}/datasets/{dataset}/archives/{archiveName} | Headers for a downloadable historical file.
[**head_archives**](MethodsApi.md#head_archives) | **HEAD** /catalogs/{catalog}/datasets/{dataset}/archives/ | Headers for collection of historical records.
[**head_catalog**](MethodsApi.md#head_catalog) | **HEAD** /catalogs/{catalog}/ | Headers for available data resources in this catalog
[**head_catalogs**](MethodsApi.md#head_catalogs) | **HEAD** /catalogs/ | Headers for collection of available catalogs 
[**head_dataset**](MethodsApi.md#head_dataset) | **HEAD** /catalogs/{catalog}/datasets/{dataset}/ | Headers for dataset definition and available snapshot resources
[**head_datasets**](MethodsApi.md#head_datasets) | **HEAD** /catalogs/{catalog}/datasets/ | Headers for available datasets in this catalog
[**head_distribution**](MethodsApi.md#head_distribution) | **HEAD** /catalogs/{catalog}/datasets/{dataset}/snapshots/{snapshot}/distributions/{distributionName} | Headers for a downloadable distribution of a snapshot
[**head_distributions**](MethodsApi.md#head_distributions) | **HEAD** /catalogs/{catalog}/datasets/{dataset}/snapshots/{snapshot}/distributions/ | Headers for list of available distributions of a snapshot
[**head_field**](MethodsApi.md#head_field) | **HEAD** /catalogs/bbg/fields/{field}/ | Headers for metadata describing a Bloomberg field
[**head_field_list**](MethodsApi.md#head_field_list) | **HEAD** /catalogs/{catalog}/fieldLists/{fieldListName}/ | Headers for a field list
[**head_field_lists**](MethodsApi.md#head_field_lists) | **HEAD** /catalogs/{catalog}/fieldLists/ | Headers for a collection of field lists
[**head_fields**](MethodsApi.md#head_fields) | **HEAD** /catalogs/bbg/fields/ | Headers for list of all fields
[**head_ontology**](MethodsApi.md#head_ontology) | **HEAD** /ontology | Headers for the DATA&lt;GO&gt; Ontology
[**head_request**](MethodsApi.md#head_request) | **HEAD** /catalogs/{catalog}/requests/{requestName}/ | Headers for a request resource
[**head_request_field_list**](MethodsApi.md#head_request_field_list) | **HEAD** /catalogs/{catalog}/requests/{requestName}/fieldList/ | Headers for a field list resource
[**head_request_trigger**](MethodsApi.md#head_request_trigger) | **HEAD** /catalogs/{catalog}/requests/{requestName}/trigger/ | Headers for a trigger resource
[**head_request_universe_list**](MethodsApi.md#head_request_universe_list) | **HEAD** /catalogs/{catalog}/requests/{requestName}/universe/ | Headers for a universe resource
[**head_requests**](MethodsApi.md#head_requests) | **HEAD** /catalogs/{catalog}/requests/ | Headers for a collection of requests
[**head_root**](MethodsApi.md#head_root) | **HEAD** / | Headers for entry point
[**head_snapshot**](MethodsApi.md#head_snapshot) | **HEAD** /catalogs/{catalog}/datasets/{dataset}/snapshots/{snapshot}/ | Headers for snapshot metadata and available distributions
[**head_snapshots**](MethodsApi.md#head_snapshots) | **HEAD** /catalogs/{catalog}/datasets/{dataset}/snapshots/ | Headers for list of available snapshots for a dataset
[**head_trigger**](MethodsApi.md#head_trigger) | **HEAD** /catalogs/{catalog}/triggers/{triggerName}/ | Headers for a trigger resource
[**head_triggers**](MethodsApi.md#head_triggers) | **HEAD** /catalogs/{catalog}/triggers/ | Headers for a collection of triggers
[**head_universe**](MethodsApi.md#head_universe) | **HEAD** /catalogs/{catalog}/universes/{universeName}/ | Headers for a universe resource
[**head_universes**](MethodsApi.md#head_universes) | **HEAD** /catalogs/{catalog}/universes/ | Headers for a collection of universes
[**options_archive**](MethodsApi.md#options_archive) | **OPTIONS** /catalogs/{catalog}/datasets/{dataset}/archives/{archiveName} | Options for a downloadable historical file.
[**options_archives**](MethodsApi.md#options_archives) | **OPTIONS** /catalogs/{catalog}/datasets/{dataset}/archives/ | Options for dataset archive collection.
[**options_catalog**](MethodsApi.md#options_catalog) | **OPTIONS** /catalogs/{catalog}/ | Options for data resources in this catalog
[**options_catalogs**](MethodsApi.md#options_catalogs) | **OPTIONS** /catalogs/ | Options for collection of available catalogs
[**options_dataset**](MethodsApi.md#options_dataset) | **OPTIONS** /catalogs/{catalog}/datasets/{dataset}/ | Options for dataset definition and available snapshot resources
[**options_datasets**](MethodsApi.md#options_datasets) | **OPTIONS** /catalogs/{catalog}/datasets/ | Options for available datasets in this catalog
[**options_distribution**](MethodsApi.md#options_distribution) | **OPTIONS** /catalogs/{catalog}/datasets/{dataset}/snapshots/{snapshot}/distributions/{distributionName} | Options for a downloadable distribution of a snapshot
[**options_distributions**](MethodsApi.md#options_distributions) | **OPTIONS** /catalogs/{catalog}/datasets/{dataset}/snapshots/{snapshot}/distributions/ | Options for list of available distributions of a snapshot
[**options_field**](MethodsApi.md#options_field) | **OPTIONS** /catalogs/bbg/fields/{field}/ | Options for metadata describing a Bloomberg field
[**options_field_list**](MethodsApi.md#options_field_list) | **OPTIONS** /catalogs/{catalog}/fieldLists/{fieldListName}/ | Options for a field list resource
[**options_field_lists**](MethodsApi.md#options_field_lists) | **OPTIONS** /catalogs/{catalog}/fieldLists/ | Options for a collection of field lists
[**options_fields**](MethodsApi.md#options_fields) | **OPTIONS** /catalogs/bbg/fields/ | Options for list of all fields
[**options_ontology**](MethodsApi.md#options_ontology) | **OPTIONS** /ontology | Options for the DATA&lt;GO&gt; Ontology
[**options_request**](MethodsApi.md#options_request) | **OPTIONS** /catalogs/{catalog}/requests/{requestName}/ | Options for a request resource
[**options_request_field_list**](MethodsApi.md#options_request_field_list) | **OPTIONS** /catalogs/{catalog}/requests/{requestName}/fieldList/ | Options for a field list resource
[**options_request_trigger**](MethodsApi.md#options_request_trigger) | **OPTIONS** /catalogs/{catalog}/requests/{requestName}/trigger/ | Options for a trigger resource
[**options_request_universe**](MethodsApi.md#options_request_universe) | **OPTIONS** /catalogs/{catalog}/requests/{requestName}/universe/ | Options for a universe resource
[**options_requests**](MethodsApi.md#options_requests) | **OPTIONS** /catalogs/{catalog}/requests/ | Options for a collection of requests
[**options_root**](MethodsApi.md#options_root) | **OPTIONS** / | Options for entry point
[**options_snapshot**](MethodsApi.md#options_snapshot) | **OPTIONS** /catalogs/{catalog}/datasets/{dataset}/snapshots/{snapshot}/ | Options for snapshot metadata and available distributions
[**options_snapshots**](MethodsApi.md#options_snapshots) | **OPTIONS** /catalogs/{catalog}/datasets/{dataset}/snapshots/ | Options for list of available snapshots for a dataset
[**options_trigger**](MethodsApi.md#options_trigger) | **OPTIONS** /catalogs/{catalog}/triggers/{triggerName}/ | Options for a trigger resource
[**options_triggers**](MethodsApi.md#options_triggers) | **OPTIONS** /catalogs/{catalog}/triggers/ | Options for a collection of triggers
[**options_universe**](MethodsApi.md#options_universe) | **OPTIONS** /catalogs/{catalog}/universes/{universeName}/ | Options for a universe resource
[**options_universes**](MethodsApi.md#options_universes) | **OPTIONS** /catalogs/{catalog}/universes/ | Options for a collection of universes

# **catalogs_bbg_publishers_head**
> catalogs_bbg_publishers_head(jwt, api_version)

Headers for a collection of Publisher resources

Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.MethodsApi()
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.

try:
    # Headers for a collection of Publisher resources
    api_instance.catalogs_bbg_publishers_head(jwt, api_version)
except ApiException as e:
    print("Exception when calling MethodsApi->catalogs_bbg_publishers_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalogs_bbg_publishers_options**
> catalogs_bbg_publishers_options(jwt, api_version)

Options for a collection of Publisher resources

Returns the methods that are supported by this endpoint.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.MethodsApi()
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.

try:
    # Options for a collection of Publisher resources
    api_instance.catalogs_bbg_publishers_options(jwt, api_version)
except ApiException as e:
    print("Exception when calling MethodsApi->catalogs_bbg_publishers_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **catalogs_bbg_publishers_publisher_name_head**
> catalogs_bbg_publishers_publisher_name_head(publisher_name, jwt, api_version)

Headers for metadata for a publisher

Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.MethodsApi()
publisher_name = 'publisher_name_example' # str | Publisher name
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.

try:
    # Headers for metadata for a publisher
    api_instance.catalogs_bbg_publishers_publisher_name_head(publisher_name, jwt, api_version)
except ApiException as e:
    print("Exception when calling MethodsApi->catalogs_bbg_publishers_publisher_name_head: %s\n" % e)
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
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalogs_bbg_publishers_publisher_name_options**
> catalogs_bbg_publishers_publisher_name_options(publisher_name, jwt, api_version)

Options for metadata for a publisher

Returns the methods that are supported by this endpoint.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.MethodsApi()
publisher_name = 'publisher_name_example' # str | Publisher name
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.

try:
    # Options for metadata for a publisher
    api_instance.catalogs_bbg_publishers_publisher_name_options(publisher_name, jwt, api_version)
except ApiException as e:
    print("Exception when calling MethodsApi->catalogs_bbg_publishers_publisher_name_options: %s\n" % e)
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
 - **Accept**: application/ld+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_archive**
> head_archive(catalog, dataset, archive_name, jwt, api_version)

Headers for a downloadable historical file.

Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.MethodsApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
dataset = 'dataset_example' # str | Dataset identifier
archive_name = 'archive_name_example' # str | Archive name
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.

try:
    # Headers for a downloadable historical file.
    api_instance.head_archive(catalog, dataset, archive_name, jwt, api_version)
except ApiException as e:
    print("Exception when calling MethodsApi->head_archive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 
 **dataset** | **str**| Dataset identifier | 
 **archive_name** | **str**| Archive name | 
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_archives**
> head_archives(jwt, api_version, catalog, dataset)

Headers for collection of historical records.

Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.MethodsApi()
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
dataset = 'dataset_example' # str | Dataset identifier

try:
    # Headers for collection of historical records.
    api_instance.head_archives(jwt, api_version, catalog, dataset)
except ApiException as e:
    print("Exception when calling MethodsApi->head_archives: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 
 **dataset** | **str**| Dataset identifier | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_catalog**
> head_catalog(jwt, api_version, catalog)

Headers for available data resources in this catalog

Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.MethodsApi()
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).

try:
    # Headers for available data resources in this catalog
    api_instance.head_catalog(jwt, api_version, catalog)
except ApiException as e:
    print("Exception when calling MethodsApi->head_catalog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_catalogs**
> head_catalogs(jwt, api_version)

Headers for collection of available catalogs 

Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.MethodsApi()
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.

try:
    # Headers for collection of available catalogs 
    api_instance.head_catalogs(jwt, api_version)
except ApiException as e:
    print("Exception when calling MethodsApi->head_catalogs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_dataset**
> head_dataset(jwt, api_version, catalog, dataset)

Headers for dataset definition and available snapshot resources

Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.MethodsApi()
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
dataset = 'dataset_example' # str | Dataset identifier

try:
    # Headers for dataset definition and available snapshot resources
    api_instance.head_dataset(jwt, api_version, catalog, dataset)
except ApiException as e:
    print("Exception when calling MethodsApi->head_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 
 **dataset** | **str**| Dataset identifier | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_datasets**
> head_datasets(catalog, jwt, api_version, page=page, q=q, subscribed=subscribed, module_level1=module_level1, module_level2=module_level2, module_level3=module_level3, universe_label=universe_label, universe_subset_label=universe_subset_label, publisher=publisher)

Headers for available datasets in this catalog

Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.MethodsApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.
page = 56 # int | Page number to view (optional)
q = 'q_example' # str | Search terms. This is only applicable when catalog is `bbg`. (optional)
subscribed = true # bool | Subscription status. This is only applicable when catalog is `bbg`. (optional)
module_level1 = 'module_level1_example' # str | Filter by module level 1. This is only applicable when catalog is `bbg`. (optional)
module_level2 = 'module_level2_example' # str | Filter by module level 2. This is only applicable when catalog is `bbg`. (optional)
module_level3 = 'module_level3_example' # str | Filter by module level 3. This is only applicable when catalog is `bbg`. (optional)
universe_label = 'universe_label_example' # str | Filter by universe label. This is only applicable when catalog is `bbg`. (optional)
universe_subset_label = 'universe_subset_label_example' # str | Filter by universe subset label. This is only applicable when catalog is `bbg`. (optional)
publisher = 'publisher_example' # str | Filter by the publisher. This is only applicable when catalog is `bbg`. (optional)

try:
    # Headers for available datasets in this catalog
    api_instance.head_datasets(catalog, jwt, api_version, page=page, q=q, subscribed=subscribed, module_level1=module_level1, module_level2=module_level2, module_level3=module_level3, universe_label=universe_label, universe_subset_label=universe_subset_label, publisher=publisher)
except ApiException as e:
    print("Exception when calling MethodsApi->head_datasets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 
 **page** | **int**| Page number to view | [optional] 
 **q** | **str**| Search terms. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **subscribed** | **bool**| Subscription status. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **module_level1** | **str**| Filter by module level 1. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **module_level2** | **str**| Filter by module level 2. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **module_level3** | **str**| Filter by module level 3. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **universe_label** | **str**| Filter by universe label. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **universe_subset_label** | **str**| Filter by universe subset label. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **publisher** | **str**| Filter by the publisher. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_distribution**
> head_distribution(catalog, dataset, snapshot, distribution_name, jwt, api_version)

Headers for a downloadable distribution of a snapshot

Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.MethodsApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
dataset = 'dataset_example' # str | Dataset identifier
snapshot = 'snapshot_example' # str | Dataset snapshot identifier
distribution_name = 'distribution_name_example' # str | Distribution name
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.

try:
    # Headers for a downloadable distribution of a snapshot
    api_instance.head_distribution(catalog, dataset, snapshot, distribution_name, jwt, api_version)
except ApiException as e:
    print("Exception when calling MethodsApi->head_distribution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 
 **dataset** | **str**| Dataset identifier | 
 **snapshot** | **str**| Dataset snapshot identifier | 
 **distribution_name** | **str**| Distribution name | 
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_distributions**
> head_distributions(catalog, dataset, snapshot, jwt, api_version)

Headers for list of available distributions of a snapshot

Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.MethodsApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
dataset = 'dataset_example' # str | Dataset identifier
snapshot = 'snapshot_example' # str | Dataset snapshot identifier
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.

try:
    # Headers for list of available distributions of a snapshot
    api_instance.head_distributions(catalog, dataset, snapshot, jwt, api_version)
except ApiException as e:
    print("Exception when calling MethodsApi->head_distributions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 
 **dataset** | **str**| Dataset identifier | 
 **snapshot** | **str**| Dataset snapshot identifier | 
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_field**
> head_field(jwt, api_version, field)

Headers for metadata describing a Bloomberg field

Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.MethodsApi()
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.
field = 'field_example' # str | Field identifier

try:
    # Headers for metadata describing a Bloomberg field
    api_instance.head_field(jwt, api_version, field)
except ApiException as e:
    print("Exception when calling MethodsApi->head_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 
 **field** | **str**| Field identifier | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_field_list**
> head_field_list(catalog, field_list_name, jwt, api_version)

Headers for a field list

Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.MethodsApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
field_list_name = 'field_list_name_example' # str | Field list name.
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.

try:
    # Headers for a field list
    api_instance.head_field_list(catalog, field_list_name, jwt, api_version)
except ApiException as e:
    print("Exception when calling MethodsApi->head_field_list: %s\n" % e)
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
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_field_lists**
> head_field_lists(catalog, jwt, api_version, page=page)

Headers for a collection of field lists

Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.MethodsApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.
page = 56 # int | Page number to view (optional)

try:
    # Headers for a collection of field lists
    api_instance.head_field_lists(catalog, jwt, api_version, page=page)
except ApiException as e:
    print("Exception when calling MethodsApi->head_field_lists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 
 **page** | **int**| Page number to view | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_fields**
> head_fields(jwt, api_version, page=page, q=q, dl_bulk=dl_bulk, data_license=data_license, platform_static=platform_static, platform_streaming=platform_streaming, platform_terminal_required=platform_terminal_required, xsdtype=xsdtype, yk_commodity=yk_commodity, yk_corporate=yk_corporate, yk_currency=yk_currency, yk_equity=yk_equity, yk_index=yk_index, yk_mortgage=yk_mortgage, yk_money_market=yk_money_market, yk_municipal=yk_municipal, yk_preferred=yk_preferred, yk_us_government=yk_us_government)

Headers for list of all fields

Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.MethodsApi()
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.
page = 56 # int | Page number to view (optional)
q = 'q_example' # str | Search terms. This is only applicable when catalog is `bbg`. (optional)
dl_bulk = 'dl_bulk_example' # str | Filter by DL:Bulk. This is only applicable when catalog is `bbg`. (optional)
data_license = 'data_license_example' # str | Filter by Data License. This is only applicable when catalog is `bbg`. (optional)
platform_static = 'platform_static_example' # str | Filter by Platform: Static. This is only applicable when catalog is `bbg`. (optional)
platform_streaming = 'platform_streaming_example' # str | Filter by Platform: Streaming. This is only applicable when catalog is `bbg`. (optional)
platform_terminal_required = 'platform_terminal_required_example' # str | Filter by Platform: Terminal Required. This is only applicable when catalog is `bbg`. (optional)
xsdtype = 'xsdtype_example' # str | Filter by xsd:type. This is only applicable when catalog is `bbg`. (optional)
yk_commodity = 'yk_commodity_example' # str | Filter by the YK: Commodity. This is only applicable when catalog is `bbg`. (optional)
yk_corporate = 'yk_corporate_example' # str | Filter by the YK: Corporate. This is only applicable when catalog is `bbg`. (optional)
yk_currency = 'yk_currency_example' # str | Filter by the YK: Currency. This is only applicable when catalog is `bbg`. (optional)
yk_equity = 'yk_equity_example' # str | Filter by the YK: Equity. This is only applicable when catalog is `bbg`. (optional)
yk_index = 'yk_index_example' # str | Filter by the YK: Index. This is only applicable when catalog is `bbg`. (optional)
yk_mortgage = 'yk_mortgage_example' # str | Filter by the YK: Mortgage. This is only applicable when catalog is `bbg`. (optional)
yk_money_market = 'yk_money_market_example' # str | Filter by the YK: Money Market. This is only applicable when catalog is `bbg`. (optional)
yk_municipal = 'yk_municipal_example' # str | Filter by the YK: Municipal. This is only applicable when catalog is `bbg`. (optional)
yk_preferred = 'yk_preferred_example' # str | Filter by the YK: Preferred. This is only applicable when catalog is `bbg`. (optional)
yk_us_government = 'yk_us_government_example' # str | Filter by the YK: US Government. This is only applicable when catalog is `bbg`. (optional)

try:
    # Headers for list of all fields
    api_instance.head_fields(jwt, api_version, page=page, q=q, dl_bulk=dl_bulk, data_license=data_license, platform_static=platform_static, platform_streaming=platform_streaming, platform_terminal_required=platform_terminal_required, xsdtype=xsdtype, yk_commodity=yk_commodity, yk_corporate=yk_corporate, yk_currency=yk_currency, yk_equity=yk_equity, yk_index=yk_index, yk_mortgage=yk_mortgage, yk_money_market=yk_money_market, yk_municipal=yk_municipal, yk_preferred=yk_preferred, yk_us_government=yk_us_government)
except ApiException as e:
    print("Exception when calling MethodsApi->head_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 
 **page** | **int**| Page number to view | [optional] 
 **q** | **str**| Search terms. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **dl_bulk** | **str**| Filter by DL:Bulk. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **data_license** | **str**| Filter by Data License. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **platform_static** | **str**| Filter by Platform: Static. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **platform_streaming** | **str**| Filter by Platform: Streaming. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **platform_terminal_required** | **str**| Filter by Platform: Terminal Required. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **xsdtype** | **str**| Filter by xsd:type. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **yk_commodity** | **str**| Filter by the YK: Commodity. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **yk_corporate** | **str**| Filter by the YK: Corporate. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **yk_currency** | **str**| Filter by the YK: Currency. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **yk_equity** | **str**| Filter by the YK: Equity. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **yk_index** | **str**| Filter by the YK: Index. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **yk_mortgage** | **str**| Filter by the YK: Mortgage. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **yk_money_market** | **str**| Filter by the YK: Money Market. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **yk_municipal** | **str**| Filter by the YK: Municipal. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **yk_preferred** | **str**| Filter by the YK: Preferred. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **yk_us_government** | **str**| Filter by the YK: US Government. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_ontology**
> head_ontology(jwt, api_version)

Headers for the DATA<GO> Ontology

Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.MethodsApi()
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.

try:
    # Headers for the DATA<GO> Ontology
    api_instance.head_ontology(jwt, api_version)
except ApiException as e:
    print("Exception when calling MethodsApi->head_ontology: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_request**
> head_request(catalog, request_name, jwt, api_version)

Headers for a request resource

Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.MethodsApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
request_name = 'request_name_example' # str | Request name
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.

try:
    # Headers for a request resource
    api_instance.head_request(catalog, request_name, jwt, api_version)
except ApiException as e:
    print("Exception when calling MethodsApi->head_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 
 **request_name** | **str**| Request name | 
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_request_field_list**
> head_request_field_list(catalog, request_name, jwt, api_version, page=page, page_size=page_size)

Headers for a field list resource

Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.MethodsApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
request_name = 'request_name_example' # str | Request name
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.
page = 56 # int | Page number to view (optional)
page_size = 56 # int | Number of items per page. Defaults to 20 if not supplied. (optional)

try:
    # Headers for a field list resource
    api_instance.head_request_field_list(catalog, request_name, jwt, api_version, page=page, page_size=page_size)
except ApiException as e:
    print("Exception when calling MethodsApi->head_request_field_list: %s\n" % e)
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

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_request_trigger**
> head_request_trigger(catalog, request_name, jwt, api_version)

Headers for a trigger resource

Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.MethodsApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
request_name = 'request_name_example' # str | Request name
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.

try:
    # Headers for a trigger resource
    api_instance.head_request_trigger(catalog, request_name, jwt, api_version)
except ApiException as e:
    print("Exception when calling MethodsApi->head_request_trigger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 
 **request_name** | **str**| Request name | 
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_request_universe_list**
> head_request_universe_list(catalog, request_name, jwt, api_version, page=page, page_size=page_size)

Headers for a universe resource

Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.MethodsApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
request_name = 'request_name_example' # str | Request name
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.
page = 56 # int | Page number to view (optional)
page_size = 56 # int | Number of items per page. Defaults to 20 if not supplied. (optional)

try:
    # Headers for a universe resource
    api_instance.head_request_universe_list(catalog, request_name, jwt, api_version, page=page, page_size=page_size)
except ApiException as e:
    print("Exception when calling MethodsApi->head_request_universe_list: %s\n" % e)
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

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_requests**
> head_requests(catalog, jwt, api_version, page=page)

Headers for a collection of requests

Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.MethodsApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.
page = 56 # int | Page number to view (optional)

try:
    # Headers for a collection of requests
    api_instance.head_requests(catalog, jwt, api_version, page=page)
except ApiException as e:
    print("Exception when calling MethodsApi->head_requests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 
 **page** | **int**| Page number to view | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_root**
> head_root(jwt, api_version)

Headers for entry point

Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.MethodsApi()
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.

try:
    # Headers for entry point
    api_instance.head_root(jwt, api_version)
except ApiException as e:
    print("Exception when calling MethodsApi->head_root: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_snapshot**
> head_snapshot(catalog, dataset, snapshot, jwt, api_version)

Headers for snapshot metadata and available distributions

Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.MethodsApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
dataset = 'dataset_example' # str | Dataset identifier
snapshot = 'snapshot_example' # str | Dataset snapshot identifier
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.

try:
    # Headers for snapshot metadata and available distributions
    api_instance.head_snapshot(catalog, dataset, snapshot, jwt, api_version)
except ApiException as e:
    print("Exception when calling MethodsApi->head_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 
 **dataset** | **str**| Dataset identifier | 
 **snapshot** | **str**| Dataset snapshot identifier | 
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_snapshots**
> head_snapshots(catalog, dataset, jwt, api_version, page=page)

Headers for list of available snapshots for a dataset

Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.MethodsApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
dataset = 'dataset_example' # str | Dataset identifier
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.
page = 56 # int | Page number to view (optional)

try:
    # Headers for list of available snapshots for a dataset
    api_instance.head_snapshots(catalog, dataset, jwt, api_version, page=page)
except ApiException as e:
    print("Exception when calling MethodsApi->head_snapshots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 
 **dataset** | **str**| Dataset identifier | 
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 
 **page** | **int**| Page number to view | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_trigger**
> head_trigger(catalog, trigger_name, jwt, api_version)

Headers for a trigger resource

Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.MethodsApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
trigger_name = 'trigger_name_example' # str | Trigger name.
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.

try:
    # Headers for a trigger resource
    api_instance.head_trigger(catalog, trigger_name, jwt, api_version)
except ApiException as e:
    print("Exception when calling MethodsApi->head_trigger: %s\n" % e)
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
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_triggers**
> head_triggers(catalog, jwt, api_version, page=page)

Headers for a collection of triggers

Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.MethodsApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.
page = 56 # int | Page number to view (optional)

try:
    # Headers for a collection of triggers
    api_instance.head_triggers(catalog, jwt, api_version, page=page)
except ApiException as e:
    print("Exception when calling MethodsApi->head_triggers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 
 **page** | **int**| Page number to view | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_universe**
> head_universe(catalog, universe_name, jwt, api_version)

Headers for a universe resource

Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.MethodsApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
universe_name = 'universe_name_example' # str | Universe name.
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.

try:
    # Headers for a universe resource
    api_instance.head_universe(catalog, universe_name, jwt, api_version)
except ApiException as e:
    print("Exception when calling MethodsApi->head_universe: %s\n" % e)
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
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_universes**
> head_universes(catalog, jwt, api_version, page=page)

Headers for a collection of universes

Returns the headers that would be returned if the specified resource were requested with an HTTP GET method.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.MethodsApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.
page = 56 # int | Page number to view (optional)

try:
    # Headers for a collection of universes
    api_instance.head_universes(catalog, jwt, api_version, page=page)
except ApiException as e:
    print("Exception when calling MethodsApi->head_universes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 
 **page** | **int**| Page number to view | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **options_archive**
> options_archive(catalog, dataset, archive_name, jwt, api_version)

Options for a downloadable historical file.

Returns the methods that are supported by this endpoint.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.MethodsApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
dataset = 'dataset_example' # str | Dataset identifier
archive_name = 'archive_name_example' # str | Archive name
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.

try:
    # Options for a downloadable historical file.
    api_instance.options_archive(catalog, dataset, archive_name, jwt, api_version)
except ApiException as e:
    print("Exception when calling MethodsApi->options_archive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 
 **dataset** | **str**| Dataset identifier | 
 **archive_name** | **str**| Archive name | 
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

# **options_archives**
> options_archives(jwt, api_version, catalog, dataset)

Options for dataset archive collection.

Returns the methods that are supported by this endpoint.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.MethodsApi()
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
dataset = 'dataset_example' # str | Dataset identifier

try:
    # Options for dataset archive collection.
    api_instance.options_archives(jwt, api_version, catalog, dataset)
except ApiException as e:
    print("Exception when calling MethodsApi->options_archives: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 
 **dataset** | **str**| Dataset identifier | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **options_catalog**
> options_catalog(jwt, api_version, catalog)

Options for data resources in this catalog

Returns the methods that are supported by this endpoint.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.MethodsApi()
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).

try:
    # Options for data resources in this catalog
    api_instance.options_catalog(jwt, api_version, catalog)
except ApiException as e:
    print("Exception when calling MethodsApi->options_catalog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **options_catalogs**
> options_catalogs(jwt, api_version)

Options for collection of available catalogs

Returns the methods that are supported by this endpoint.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.MethodsApi()
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.

try:
    # Options for collection of available catalogs
    api_instance.options_catalogs(jwt, api_version)
except ApiException as e:
    print("Exception when calling MethodsApi->options_catalogs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **options_dataset**
> options_dataset(jwt, api_version, catalog, dataset)

Options for dataset definition and available snapshot resources

Returns the methods that are supported by this endpoint.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.MethodsApi()
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
dataset = 'dataset_example' # str | Dataset identifier

try:
    # Options for dataset definition and available snapshot resources
    api_instance.options_dataset(jwt, api_version, catalog, dataset)
except ApiException as e:
    print("Exception when calling MethodsApi->options_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 
 **dataset** | **str**| Dataset identifier | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **options_datasets**
> options_datasets(catalog, jwt, api_version, page=page, q=q, subscribed=subscribed, module_level1=module_level1, module_level2=module_level2, module_level3=module_level3, universe_label=universe_label, universe_subset_label=universe_subset_label, publisher=publisher)

Options for available datasets in this catalog

Returns the methods that are supported by this endpoint.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.MethodsApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.
page = 56 # int | Page number to view (optional)
q = 'q_example' # str | Search terms. This is only applicable when catalog is `bbg`. (optional)
subscribed = true # bool | Subscription status. This is only applicable when catalog is `bbg`. (optional)
module_level1 = 'module_level1_example' # str | Filter by module level 1. This is only applicable when catalog is `bbg`. (optional)
module_level2 = 'module_level2_example' # str | Filter by module level 2. This is only applicable when catalog is `bbg`. (optional)
module_level3 = 'module_level3_example' # str | Filter by module level 3. This is only applicable when catalog is `bbg`. (optional)
universe_label = 'universe_label_example' # str | Filter by universe label. This is only applicable when catalog is `bbg`. (optional)
universe_subset_label = 'universe_subset_label_example' # str | Filter by universe subset label. This is only applicable when catalog is `bbg`. (optional)
publisher = 'publisher_example' # str | Filter by the publisher. This is only applicable when catalog is `bbg`. (optional)

try:
    # Options for available datasets in this catalog
    api_instance.options_datasets(catalog, jwt, api_version, page=page, q=q, subscribed=subscribed, module_level1=module_level1, module_level2=module_level2, module_level3=module_level3, universe_label=universe_label, universe_subset_label=universe_subset_label, publisher=publisher)
except ApiException as e:
    print("Exception when calling MethodsApi->options_datasets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 
 **page** | **int**| Page number to view | [optional] 
 **q** | **str**| Search terms. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **subscribed** | **bool**| Subscription status. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **module_level1** | **str**| Filter by module level 1. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **module_level2** | **str**| Filter by module level 2. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **module_level3** | **str**| Filter by module level 3. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **universe_label** | **str**| Filter by universe label. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **universe_subset_label** | **str**| Filter by universe subset label. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **publisher** | **str**| Filter by the publisher. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **options_distribution**
> options_distribution(catalog, dataset, snapshot, distribution_name, jwt, api_version)

Options for a downloadable distribution of a snapshot

Returns the methods that are supported by this endpoint.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.MethodsApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
dataset = 'dataset_example' # str | Dataset identifier
snapshot = 'snapshot_example' # str | Dataset snapshot identifier
distribution_name = 'distribution_name_example' # str | Distribution name
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.

try:
    # Options for a downloadable distribution of a snapshot
    api_instance.options_distribution(catalog, dataset, snapshot, distribution_name, jwt, api_version)
except ApiException as e:
    print("Exception when calling MethodsApi->options_distribution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 
 **dataset** | **str**| Dataset identifier | 
 **snapshot** | **str**| Dataset snapshot identifier | 
 **distribution_name** | **str**| Distribution name | 
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

# **options_distributions**
> options_distributions(catalog, dataset, snapshot, jwt, api_version)

Options for list of available distributions of a snapshot

Returns the methods that are supported by this endpoint.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.MethodsApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
dataset = 'dataset_example' # str | Dataset identifier
snapshot = 'snapshot_example' # str | Dataset snapshot identifier
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.

try:
    # Options for list of available distributions of a snapshot
    api_instance.options_distributions(catalog, dataset, snapshot, jwt, api_version)
except ApiException as e:
    print("Exception when calling MethodsApi->options_distributions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 
 **dataset** | **str**| Dataset identifier | 
 **snapshot** | **str**| Dataset snapshot identifier | 
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

# **options_field**
> options_field(jwt, api_version, field)

Options for metadata describing a Bloomberg field

Returns the methods that are supported by this endpoint.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.MethodsApi()
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.
field = 'field_example' # str | Field identifier

try:
    # Options for metadata describing a Bloomberg field
    api_instance.options_field(jwt, api_version, field)
except ApiException as e:
    print("Exception when calling MethodsApi->options_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 
 **field** | **str**| Field identifier | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **options_field_list**
> options_field_list(catalog, field_list_name, jwt, api_version)

Options for a field list resource

Returns the methods that are supported by this endpoint.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.MethodsApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
field_list_name = 'field_list_name_example' # str | Field list name.
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.

try:
    # Options for a field list resource
    api_instance.options_field_list(catalog, field_list_name, jwt, api_version)
except ApiException as e:
    print("Exception when calling MethodsApi->options_field_list: %s\n" % e)
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

# **options_field_lists**
> options_field_lists(catalog, jwt, api_version, page=page)

Options for a collection of field lists

Returns the methods that are supported by this endpoint.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.MethodsApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.
page = 56 # int | Page number to view (optional)

try:
    # Options for a collection of field lists
    api_instance.options_field_lists(catalog, jwt, api_version, page=page)
except ApiException as e:
    print("Exception when calling MethodsApi->options_field_lists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 
 **page** | **int**| Page number to view | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **options_fields**
> options_fields(jwt, api_version, page=page, q=q, dl_bulk=dl_bulk, data_license=data_license, platform_static=platform_static, platform_streaming=platform_streaming, platform_terminal_required=platform_terminal_required, xsdtype=xsdtype, yk_commodity=yk_commodity, yk_corporate=yk_corporate, yk_currency=yk_currency, yk_equity=yk_equity, yk_index=yk_index, yk_mortgage=yk_mortgage, yk_money_market=yk_money_market, yk_municipal=yk_municipal, yk_preferred=yk_preferred, yk_us_government=yk_us_government)

Options for list of all fields

Returns the methods that are supported by this endpoint.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.MethodsApi()
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.
page = 56 # int | Page number to view (optional)
q = 'q_example' # str | Search terms. This is only applicable when catalog is `bbg`. (optional)
dl_bulk = 'dl_bulk_example' # str | Filter by DL:Bulk. This is only applicable when catalog is `bbg`. (optional)
data_license = 'data_license_example' # str | Filter by Data License. This is only applicable when catalog is `bbg`. (optional)
platform_static = 'platform_static_example' # str | Filter by Platform: Static. This is only applicable when catalog is `bbg`. (optional)
platform_streaming = 'platform_streaming_example' # str | Filter by Platform: Streaming. This is only applicable when catalog is `bbg`. (optional)
platform_terminal_required = 'platform_terminal_required_example' # str | Filter by Platform: Terminal Required. This is only applicable when catalog is `bbg`. (optional)
xsdtype = 'xsdtype_example' # str | Filter by xsd:type. This is only applicable when catalog is `bbg`. (optional)
yk_commodity = 'yk_commodity_example' # str | Filter by the YK: Commodity. This is only applicable when catalog is `bbg`. (optional)
yk_corporate = 'yk_corporate_example' # str | Filter by the YK: Corporate. This is only applicable when catalog is `bbg`. (optional)
yk_currency = 'yk_currency_example' # str | Filter by the YK: Currency. This is only applicable when catalog is `bbg`. (optional)
yk_equity = 'yk_equity_example' # str | Filter by the YK: Equity. This is only applicable when catalog is `bbg`. (optional)
yk_index = 'yk_index_example' # str | Filter by the YK: Index. This is only applicable when catalog is `bbg`. (optional)
yk_mortgage = 'yk_mortgage_example' # str | Filter by the YK: Mortgage. This is only applicable when catalog is `bbg`. (optional)
yk_money_market = 'yk_money_market_example' # str | Filter by the YK: Money Market. This is only applicable when catalog is `bbg`. (optional)
yk_municipal = 'yk_municipal_example' # str | Filter by the YK: Municipal. This is only applicable when catalog is `bbg`. (optional)
yk_preferred = 'yk_preferred_example' # str | Filter by the YK: Preferred. This is only applicable when catalog is `bbg`. (optional)
yk_us_government = 'yk_us_government_example' # str | Filter by the YK: US Government. This is only applicable when catalog is `bbg`. (optional)

try:
    # Options for list of all fields
    api_instance.options_fields(jwt, api_version, page=page, q=q, dl_bulk=dl_bulk, data_license=data_license, platform_static=platform_static, platform_streaming=platform_streaming, platform_terminal_required=platform_terminal_required, xsdtype=xsdtype, yk_commodity=yk_commodity, yk_corporate=yk_corporate, yk_currency=yk_currency, yk_equity=yk_equity, yk_index=yk_index, yk_mortgage=yk_mortgage, yk_money_market=yk_money_market, yk_municipal=yk_municipal, yk_preferred=yk_preferred, yk_us_government=yk_us_government)
except ApiException as e:
    print("Exception when calling MethodsApi->options_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 
 **page** | **int**| Page number to view | [optional] 
 **q** | **str**| Search terms. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **dl_bulk** | **str**| Filter by DL:Bulk. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **data_license** | **str**| Filter by Data License. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **platform_static** | **str**| Filter by Platform: Static. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **platform_streaming** | **str**| Filter by Platform: Streaming. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **platform_terminal_required** | **str**| Filter by Platform: Terminal Required. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **xsdtype** | **str**| Filter by xsd:type. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **yk_commodity** | **str**| Filter by the YK: Commodity. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **yk_corporate** | **str**| Filter by the YK: Corporate. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **yk_currency** | **str**| Filter by the YK: Currency. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **yk_equity** | **str**| Filter by the YK: Equity. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **yk_index** | **str**| Filter by the YK: Index. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **yk_mortgage** | **str**| Filter by the YK: Mortgage. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **yk_money_market** | **str**| Filter by the YK: Money Market. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **yk_municipal** | **str**| Filter by the YK: Municipal. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **yk_preferred** | **str**| Filter by the YK: Preferred. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
 **yk_us_government** | **str**| Filter by the YK: US Government. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **options_ontology**
> options_ontology(jwt, api_version)

Options for the DATA<GO> Ontology

Returns the methods that are supported by this endpoint.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.MethodsApi()
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.

try:
    # Options for the DATA<GO> Ontology
    api_instance.options_ontology(jwt, api_version)
except ApiException as e:
    print("Exception when calling MethodsApi->options_ontology: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **options_request**
> options_request(catalog, request_name, jwt, api_version)

Options for a request resource

Returns the methods that are supported by this endpoint.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.MethodsApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
request_name = 'request_name_example' # str | Request name
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.

try:
    # Options for a request resource
    api_instance.options_request(catalog, request_name, jwt, api_version)
except ApiException as e:
    print("Exception when calling MethodsApi->options_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 
 **request_name** | **str**| Request name | 
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

# **options_request_field_list**
> options_request_field_list(catalog, request_name, jwt, api_version, page=page, page_size=page_size)

Options for a field list resource

Returns the methods that are supported by this endpoint.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.MethodsApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
request_name = 'request_name_example' # str | Request name
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.
page = 56 # int | Page number to view (optional)
page_size = 56 # int | Number of items per page. Defaults to 20 if not supplied. (optional)

try:
    # Options for a field list resource
    api_instance.options_request_field_list(catalog, request_name, jwt, api_version, page=page, page_size=page_size)
except ApiException as e:
    print("Exception when calling MethodsApi->options_request_field_list: %s\n" % e)
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

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **options_request_trigger**
> options_request_trigger(catalog, request_name, jwt, api_version)

Options for a trigger resource

Returns the methods that are supported by this endpoint.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.MethodsApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
request_name = 'request_name_example' # str | Request name
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.

try:
    # Options for a trigger resource
    api_instance.options_request_trigger(catalog, request_name, jwt, api_version)
except ApiException as e:
    print("Exception when calling MethodsApi->options_request_trigger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 
 **request_name** | **str**| Request name | 
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

# **options_request_universe**
> options_request_universe(catalog, request_name, jwt, api_version, page=page, page_size=page_size)

Options for a universe resource

Returns the methods that are supported by this endpoint.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.MethodsApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
request_name = 'request_name_example' # str | Request name
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.
page = 56 # int | Page number to view (optional)
page_size = 56 # int | Number of items per page. Defaults to 20 if not supplied. (optional)

try:
    # Options for a universe resource
    api_instance.options_request_universe(catalog, request_name, jwt, api_version, page=page, page_size=page_size)
except ApiException as e:
    print("Exception when calling MethodsApi->options_request_universe: %s\n" % e)
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

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **options_requests**
> options_requests(catalog, jwt, api_version, page=page)

Options for a collection of requests

Returns the methods that are supported by this endpoint.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.MethodsApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.
page = 56 # int | Page number to view (optional)

try:
    # Options for a collection of requests
    api_instance.options_requests(catalog, jwt, api_version, page=page)
except ApiException as e:
    print("Exception when calling MethodsApi->options_requests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 
 **page** | **int**| Page number to view | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **options_root**
> options_root(jwt, api_version)

Options for entry point

Returns the methods that are supported by this endpoint.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.MethodsApi()
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.

try:
    # Options for entry point
    api_instance.options_root(jwt, api_version)
except ApiException as e:
    print("Exception when calling MethodsApi->options_root: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **options_snapshot**
> options_snapshot(catalog, dataset, snapshot, jwt, api_version)

Options for snapshot metadata and available distributions

Returns the methods that are supported by this endpoint.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.MethodsApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
dataset = 'dataset_example' # str | Dataset identifier
snapshot = 'snapshot_example' # str | Dataset snapshot identifier
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.

try:
    # Options for snapshot metadata and available distributions
    api_instance.options_snapshot(catalog, dataset, snapshot, jwt, api_version)
except ApiException as e:
    print("Exception when calling MethodsApi->options_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 
 **dataset** | **str**| Dataset identifier | 
 **snapshot** | **str**| Dataset snapshot identifier | 
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

# **options_snapshots**
> options_snapshots(catalog, dataset, jwt, api_version, page=page)

Options for list of available snapshots for a dataset

Returns the methods that are supported by this endpoint.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.MethodsApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
dataset = 'dataset_example' # str | Dataset identifier
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.
page = 56 # int | Page number to view (optional)

try:
    # Options for list of available snapshots for a dataset
    api_instance.options_snapshots(catalog, dataset, jwt, api_version, page=page)
except ApiException as e:
    print("Exception when calling MethodsApi->options_snapshots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 
 **dataset** | **str**| Dataset identifier | 
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 
 **page** | **int**| Page number to view | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **options_trigger**
> options_trigger(catalog, trigger_name, jwt, api_version)

Options for a trigger resource

Returns the methods that are supported by this endpoint.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.MethodsApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
trigger_name = 'trigger_name_example' # str | Trigger name.
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.

try:
    # Options for a trigger resource
    api_instance.options_trigger(catalog, trigger_name, jwt, api_version)
except ApiException as e:
    print("Exception when calling MethodsApi->options_trigger: %s\n" % e)
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

# **options_triggers**
> options_triggers(catalog, jwt, api_version, page=page)

Options for a collection of triggers

Returns the methods that are supported by this endpoint.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.MethodsApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.
page = 56 # int | Page number to view (optional)

try:
    # Options for a collection of triggers
    api_instance.options_triggers(catalog, jwt, api_version, page=page)
except ApiException as e:
    print("Exception when calling MethodsApi->options_triggers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 
 **page** | **int**| Page number to view | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **options_universe**
> options_universe(catalog, universe_name, jwt, api_version)

Options for a universe resource

Returns the methods that are supported by this endpoint.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.MethodsApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
universe_name = 'universe_name_example' # str | Universe name.
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.

try:
    # Options for a universe resource
    api_instance.options_universe(catalog, universe_name, jwt, api_version)
except ApiException as e:
    print("Exception when calling MethodsApi->options_universe: %s\n" % e)
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

# **options_universes**
> options_universes(catalog, jwt, api_version, page=page)

Options for a collection of universes

Returns the methods that are supported by this endpoint.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.MethodsApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.
page = 56 # int | Page number to view (optional)

try:
    # Options for a collection of universes
    api_instance.options_universes(catalog, jwt, api_version, page=page)
except ApiException as e:
    print("Exception when calling MethodsApi->options_universes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 
 **page** | **int**| Page number to view | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

