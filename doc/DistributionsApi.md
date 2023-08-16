# blapi.DistributionsApi

All URIs are relative to *https://api.bloomberg.com/eap*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_distribution**](DistributionsApi.md#get_distribution) | **GET** /catalogs/{catalog}/datasets/{dataset}/snapshots/{snapshot}/distributions/{distributionName} | A downloadable distribution of a snapshot
[**get_distributions**](DistributionsApi.md#get_distributions) | **GET** /catalogs/{catalog}/datasets/{dataset}/snapshots/{snapshot}/distributions/ | List of distributions of a snapshot

# **get_distribution**
> str get_distribution(catalog, dataset, snapshot, distribution_name, jwt, api_version, range=range)

A downloadable distribution of a snapshot

A downloadable serialization of [snapshot](#tag/snapshots) as a standard [media type](https://www.w3.org/TR/vocab-dcat-2/#Property:distribution_media_type) (content type). 

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.DistributionsApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
dataset = 'dataset_example' # str | Dataset identifier
snapshot = 'snapshot_example' # str | Dataset snapshot identifier
distribution_name = 'distribution_name_example' # str | Distribution name
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.
range = 'range_example' # str | For file download requests this can be used to specify a specific part of the file to be returned. Bytes is the only supported unit. DL REST API requires that `Accept-Encoding: gzip` is specified for range requests. (optional)

try:
    # A downloadable distribution of a snapshot
    api_response = api_instance.get_distribution(catalog, dataset, snapshot, distribution_name, jwt, api_version, range=range)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionsApi->get_distribution: %s\n" % e)
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
 **range** | **str**| For file download requests this can be used to specify a specific part of the file to be returned. Bytes is the only supported unit. DL REST API requires that &#x60;Accept-Encoding: gzip&#x60; is specified for range requests. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/vnd.blp.dl.std, text/csv, application/ld+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_distributions**
> Distributions get_distributions(catalog, dataset, snapshot, jwt, api_version, type=type)

List of distributions of a snapshot

A collection of downloadable [distribution](#tag/distribution) resources. Each [distribution](#tag/distributions) in the collection serializes a [snapshot](#tag/snapshots) as a different [media type](https://www.w3.org/TR/vocab-dcat-2/#Property:distribution_media_type) (content type), and is represented as a structure: the downloadable [distribution] itself; if it is a sample of the [snapshot](#tag/snapshots) (samples are accessible to all users); and if it is accessible with the requesting credentials. 

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.DistributionsApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
dataset = 'dataset_example' # str | Dataset identifier
snapshot = 'snapshot_example' # str | Dataset snapshot identifier
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.
type = [blapi.DistributionType()] # list[DistributionType] | The type of distributions to be returned (optional)

try:
    # List of distributions of a snapshot
    api_response = api_instance.get_distributions(catalog, dataset, snapshot, jwt, api_version, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionsApi->get_distributions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 
 **dataset** | **str**| Dataset identifier | 
 **snapshot** | **str**| Dataset snapshot identifier | 
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 
 **type** | [**list[DistributionType]**](DistributionType.md)| The type of distributions to be returned | [optional] 

### Return type

[**Distributions**](Distributions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

