# blapi.OntologyDeprecatedApi

All URIs are relative to *https://api.bloomberg.com/eap*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ontology**](OntologyDeprecatedApi.md#get_ontology) | **GET** /ontology | Returns latest Vocabulary Documentation

# **get_ontology**
> str get_ontology(jwt, api_version)

Returns latest Vocabulary Documentation

A resource with a canonical URL which provides access to a [ttl serialization of the latest snapshot of the DATA&lt;GO&gt; Ontology](https://data.bloomberg.com/catalogs/bbg/datasets/beapOntology/snapshots/20200406/distributions/beapOntology.ttl) 

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.OntologyDeprecatedApi()
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.

try:
    # Returns latest Vocabulary Documentation
    api_response = api_instance.get_ontology(jwt, api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OntologyDeprecatedApi->get_ontology: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/vnd.blp.dl.std, application/ld+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

