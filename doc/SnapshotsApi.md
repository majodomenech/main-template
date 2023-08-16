# blapi.SnapshotsApi

All URIs are relative to *https://api.bloomberg.com/eap*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_snapshot**](SnapshotsApi.md#get_snapshot) | **GET** /catalogs/{catalog}/datasets/{dataset}/snapshots/{snapshot}/ | Snapshot metadata and available distributions
[**get_snapshots**](SnapshotsApi.md#get_snapshots) | **GET** /catalogs/{catalog}/datasets/{dataset}/snapshots/ | List of available snapshots for a dataset

# **get_snapshot**
> Snapshot get_snapshot(catalog, dataset, snapshot, jwt, api_version)

Snapshot metadata and available distributions

A `snapshot` represents a publication of a [dataset](#tag/datasets). It contains a collection of [distributions](#tag/distributions) which are downloadable serializations of the `snapshots` as different content types. 

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.SnapshotsApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
dataset = 'dataset_example' # str | Dataset identifier
snapshot = 'snapshot_example' # str | Dataset snapshot identifier
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.

try:
    # Snapshot metadata and available distributions
    api_response = api_instance.get_snapshot(catalog, dataset, snapshot, jwt, api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotsApi->get_snapshot: %s\n" % e)
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

[**Snapshot**](Snapshot.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snapshots**
> Snapshots get_snapshots(catalog, dataset, jwt, api_version, page=page, start_issued=start_issued, end_issued=end_issued)

List of available snapshots for a dataset

`snapshots` returns a collection of [snapshot](#tag/snapshots) resources, where each [snapshot](#tag/snapshots) describes a point in the publication time series for the [dataset](#tag/datasets), and may be downloaded as a full or sample [distributions](#tag/distributions).

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.SnapshotsApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
dataset = 'dataset_example' # str | Dataset identifier
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.
page = 56 # int | Page number to view (optional)
start_issued = 'start_issued_example' # str | snapshot issued date filter, e.g. 2019-05-31. Snapshots issued on or after the given filter will be returned. (optional)
end_issued = 'end_issued_example' # str | snapshot issued date filter, e.g. 2019-12-31. Snapshots issued on or before the given filter will be returned. (optional)

try:
    # List of available snapshots for a dataset
    api_response = api_instance.get_snapshots(catalog, dataset, jwt, api_version, page=page, start_issued=start_issued, end_issued=end_issued)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotsApi->get_snapshots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 
 **dataset** | **str**| Dataset identifier | 
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 
 **page** | **int**| Page number to view | [optional] 
 **start_issued** | **str**| snapshot issued date filter, e.g. 2019-05-31. Snapshots issued on or after the given filter will be returned. | [optional] 
 **end_issued** | **str**| snapshot issued date filter, e.g. 2019-12-31. Snapshots issued on or before the given filter will be returned. | [optional] 

### Return type

[**Snapshots**](Snapshots.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

