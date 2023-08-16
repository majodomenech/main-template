# blapi.ArchivesApi

All URIs are relative to *https://api.bloomberg.com/eap*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_archive**](ArchivesApi.md#get_archive) | **GET** /catalogs/{catalog}/datasets/{dataset}/archives/{archiveName} | A downloadable historical file
[**get_archives**](ArchivesApi.md#get_archives) | **GET** /catalogs/{catalog}/datasets/{dataset}/archives/ | List of available archives for a dataset

# **get_archive**
> str get_archive(catalog, dataset, archive_name, jwt, api_version)

A downloadable historical file

A downloadable serialization of [archive](#tag/archive) in formats such as Parquet(http://parquet.apache.org/documentation/latest/). Please note that for content encoding of Parquet only identity (Accept-Encoding = identity) is supported, but not gzip.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.ArchivesApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
dataset = 'dataset_example' # str | Dataset identifier
archive_name = 'archive_name_example' # str | Archive name
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.

try:
    # A downloadable historical file
    api_response = api_instance.get_archive(catalog, dataset, archive_name, jwt, api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchivesApi->get_archive: %s\n" % e)
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

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/parquet, application/ld+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_archives**
> InlineResponse2001 get_archives(catalog, dataset, jwt, api_version, status=status, start_snapshot_date=start_snapshot_date, end_snapshot_date=end_snapshot_date, start_issued=start_issued, end_issued=end_issued, page=page, page_size=page_size)

List of available archives for a dataset

`archives` returns a collection of [archive](#tag/archives) resources, where each [archive](#tag/archives) describes aggregated historical data for the [dataset](#tag/datasets), and a downloadable link.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.ArchivesApi()
catalog = 'catalog_example' # str | Catalog identifier. Must be either `bbg` or the customer's DL account number (e.g. `1234`).
dataset = 'dataset_example' # str | Dataset identifier
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.
status = blapi.ArchiveStatus() # ArchiveStatus | The status by which to filter the returned Archives. If unspecified Archives of all statuses are returned. (optional)
start_snapshot_date = '2013-10-20' # date | The start of the date range within which to filter Archive snapshots. The filter is an inclusive match between Archive startSnpashotDate and endSnpashotDate. If unspecified, there is no lower bound on the snapshot date range. (e.g. `2020-11-15`). (optional)
end_snapshot_date = '2013-10-20' # date | The end of the date range within which to filter Archive snapshots. The filter is an inclusive match between Archive startSnapshotDate and endSnapshotDate. If unspecified, there is no upper bound on the snapshot date range. (e.g. `2020-11-17`). (optional)
start_issued = 'start_issued_example' # str | snapshot issued date filter, e.g. 2019-05-31. Snapshots issued on or after the given filter will be returned. (optional)
end_issued = 'end_issued_example' # str | snapshot issued date filter, e.g. 2019-12-31. Snapshots issued on or before the given filter will be returned. (optional)
page = 56 # int | Page number to view (optional)
page_size = 56 # int | Number of items per page. Defaults to 20 if not supplied. (optional)

try:
    # List of available archives for a dataset
    api_response = api_instance.get_archives(catalog, dataset, jwt, api_version, status=status, start_snapshot_date=start_snapshot_date, end_snapshot_date=end_snapshot_date, start_issued=start_issued, end_issued=end_issued, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchivesApi->get_archives: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog** | **str**| Catalog identifier. Must be either &#x60;bbg&#x60; or the customer&#x27;s DL account number (e.g. &#x60;1234&#x60;). | 
 **dataset** | **str**| Dataset identifier | 
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 
 **status** | [**ArchiveStatus**](.md)| The status by which to filter the returned Archives. If unspecified Archives of all statuses are returned. | [optional] 
 **start_snapshot_date** | **date**| The start of the date range within which to filter Archive snapshots. The filter is an inclusive match between Archive startSnpashotDate and endSnpashotDate. If unspecified, there is no lower bound on the snapshot date range. (e.g. &#x60;2020-11-15&#x60;). | [optional] 
 **end_snapshot_date** | **date**| The end of the date range within which to filter Archive snapshots. The filter is an inclusive match between Archive startSnapshotDate and endSnapshotDate. If unspecified, there is no upper bound on the snapshot date range. (e.g. &#x60;2020-11-17&#x60;). | [optional] 
 **start_issued** | **str**| snapshot issued date filter, e.g. 2019-05-31. Snapshots issued on or after the given filter will be returned. | [optional] 
 **end_issued** | **str**| snapshot issued date filter, e.g. 2019-12-31. Snapshots issued on or before the given filter will be returned. | [optional] 
 **page** | **int**| Page number to view | [optional] 
 **page_size** | **int**| Number of items per page. Defaults to 20 if not supplied. | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

