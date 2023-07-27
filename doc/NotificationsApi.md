# blapi.NotificationsApi

All URIs are relative to *https://api.bloomberg.com/eap*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_sse**](NotificationsApi.md#get_sse) | **GET** /notifications/sse | SSE Event Stream for DL Platform Notifications

# **get_sse**
> get_sse(jwt, last_event_id=last_event_id)

SSE Event Stream for DL Platform Notifications

# Overview An event stream providing [W3C Server-Sent Event (SSE)](https://www.w3.org/TR/eventsource/) push-notifications of Bloomberg Data License Platform activity.  # Heartbeat Notifications The notification API will periodically send out empty notifications that do not have any content to keep the connection alive. These `heartbeat` notifications can be ignored.  # Distribution Availability Notifications DL REST API publishes a [`Distribution`](#tag/distributions) availability notification event immediately when a distribution is published to the Bloomberg Catalog or Account Catalog, where the distribution is accessible using the credentials of the user who is subscribed to the event stream. Dataset availability notifications contain a JSON-LD payload, where the `@type` property value is set to `DistributionPublishedActivity`, and include additional metadata that allows a handler to process the notification.  ## Duplicate Notifications We recommend that client processes handle the receipt of duplicate or out-of-sequence notifications. Each notification includes a `digestValue` which should be used to verify if the `Distribution` has already been processed. If the `digestValue` indicates the `Distribution` has not been seen previously, the handler should then check the `endedAtTime` timestamp. If `endedAtTime` is earlier than the most recently processed timestamp for the same `Distribution`, this indicates that a notification for a more recent version of the `Distribution` has already been processed.  # Disconnections Client applications may periodically get disconnected from the notification service. When reconnecting, clients can send a `Last-Event-ID` header, as described in the SSE specification, to receive notifications that they may have missed. The `Last-Event-ID` parameter should be the most recently received SSE `id`, not the `identifier` within the notification payload. Upon reconnection, the notification service will use the `Last-Event-ID` to determine the last notification the client received, and start sending notifications from that point onward. `Last-Event-ID`s are valid for 48 hours; if a `Last-Event-ID` is received for a notification issued more than 48 hours ago, it will be ignored and the client will only receive new notifications.  # Media Format Notifications will always be returned in an HTTP response with a `Content-Type` of `text/event-stream`, per the [SSE specification](https://www.w3.org/TR/eventsource/). The documentation provided for `application/ld+json` only documents the `data` field and is provided solely for viewing the notification content at [https://data.bloomberg.com/docs/HAPI/](https://data.bloomberg.com/docs/HAPI/); please download the full OpenAPI specification to view the schema for the entire SSE.  # Connection Limits Each client can have up to 16 concurrent connections. Any connection exceeding this limit will be rejected with HTTP response status 429 - Too Many Requests. 

### Example
```python
from __future__ import print_function
import time
import blapi
from blapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blapi.NotificationsApi()
jwt = 'jwt_example' # str | JWT(https://tools.ietf.org/html/rfc7519) Authentication token
last_event_id = 'last_event_id_example' # str | Last SSE `id` that the client received. Clients can specify this in the request header to receive any notifications they may have missed over the past 48 hours. (optional)

try:
    # SSE Event Stream for DL Platform Notifications
    api_instance.get_sse(jwt, last_event_id=last_event_id)
except ApiException as e:
    print("Exception when calling NotificationsApi->get_sse: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jwt** | **str**| JWT(https://tools.ietf.org/html/rfc7519) Authentication token | 
 **last_event_id** | **str**| Last SSE &#x60;id&#x60; that the client received. Clients can specify this in the request header to receive any notifications they may have missed over the past 48 hours. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/event-stream, application/ld+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

