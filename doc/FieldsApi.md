# blapi.FieldsApi

All URIs are relative to *https://api.bloomberg.com/eap*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_field**](FieldsApi.md#get_field) | **GET** /catalogs/bbg/fields/{field}/ | Metadata describing a Bloomberg field
[**get_fields**](FieldsApi.md#get_fields) | **GET** /catalogs/bbg/fields/ | List fields

# **get_field**
> Field get_field(field, jwt, api_version)

Metadata describing a Bloomberg field

Fetch the latest field metadata for a given Bloomberg field.

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.FieldsApi()
field = 'field_example' # str | Field identifier
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.

try:
    # Metadata describing a Bloomberg field
    api_response = api_instance.get_field(field, jwt, api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldsApi->get_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field** | **str**| Field identifier | 
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 

### Return type

[**Field**](Field.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fields**
> Fields get_fields(jwt, api_version, page=page, sort=sort, q=q, dl_bulk=dl_bulk, data_license=data_license, platform_static=platform_static, platform_streaming=platform_streaming, platform_terminal_required=platform_terminal_required, xsdtype=xsdtype, yk_commodity=yk_commodity, yk_corporate=yk_corporate, yk_currency=yk_currency, yk_equity=yk_equity, yk_index=yk_index, yk_mortgage=yk_mortgage, yk_money_market=yk_money_market, yk_municipal=yk_municipal, yk_preferred=yk_preferred, yk_us_government=yk_us_government)

List fields

List of all Bloomberg fields

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.FieldsApi()
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
api_version = 'api_version_example' # str | Version of the API to access. The only valid value is 2.
page = 56 # int | Page number to view (optional)
sort = 'sort_example' # str | Field to sort by. Accepted are relevance, title and -title. This is only applicable when catalog is `bbg`. (optional)
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
    # List fields
    api_response = api_instance.get_fields(jwt, api_version, page=page, sort=sort, q=q, dl_bulk=dl_bulk, data_license=data_license, platform_static=platform_static, platform_streaming=platform_streaming, platform_terminal_required=platform_terminal_required, xsdtype=xsdtype, yk_commodity=yk_commodity, yk_corporate=yk_corporate, yk_currency=yk_currency, yk_equity=yk_equity, yk_index=yk_index, yk_mortgage=yk_mortgage, yk_money_market=yk_money_market, yk_municipal=yk_municipal, yk_preferred=yk_preferred, yk_us_government=yk_us_government)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldsApi->get_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **api_version** | **str**| Version of the API to access. The only valid value is 2. | 
 **page** | **int**| Page number to view | [optional] 
 **sort** | **str**| Field to sort by. Accepted are relevance, title and -title. This is only applicable when catalog is &#x60;bbg&#x60;. | [optional] 
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

[**Fields**](Fields.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

