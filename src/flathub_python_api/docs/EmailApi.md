# flathub_python_api.EmailApi

All URIs are relative to *https://flathub.org/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**build_notification_emails_build_notification_post**](EmailApi.md#build_notification_emails_build_notification_post) | **POST** /emails/build-notification | Build Notification


# **build_notification_emails_build_notification_post**
> object build_notification_emails_build_notification_post(build_notification_request)

Build Notification

### Example

* Bearer Authentication (HTTPBearer):

```python
import flathub_python_api
from flathub_python_api.models.build_notification_request import BuildNotificationRequest
from flathub_python_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://flathub.org/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = flathub_python_api.Configuration(
    host = "https://flathub.org/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = flathub_python_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with flathub_python_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flathub_python_api.EmailApi(api_client)
    build_notification_request = flathub_python_api.BuildNotificationRequest() # BuildNotificationRequest | 

    try:
        # Build Notification
        api_response = api_instance.build_notification_emails_build_notification_post(build_notification_request)
        print("The response of EmailApi->build_notification_emails_build_notification_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->build_notification_emails_build_notification_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_notification_request** | [**BuildNotificationRequest**](BuildNotificationRequest.md)|  | 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

