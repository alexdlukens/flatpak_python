# openapi_client.ModerationApi

All URIs are relative to *https://flathub.org/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_moderation_app_moderation_apps_app_id_get**](ModerationApi.md#get_moderation_app_moderation_apps_app_id_get) | **GET** /moderation/apps/{app_id} | Get Moderation App
[**get_moderation_apps_moderation_apps_get**](ModerationApi.md#get_moderation_apps_moderation_apps_get) | **GET** /moderation/apps | Get Moderation Apps
[**submit_review_moderation_requests_id_review_post**](ModerationApi.md#submit_review_moderation_requests_id_review_post) | **POST** /moderation/requests/{id}/review | Submit Review
[**submit_review_request_moderation_submit_review_request_post**](ModerationApi.md#submit_review_request_moderation_submit_review_request_post) | **POST** /moderation/submit_review_request | Submit Review Request


# **get_moderation_app_moderation_apps_app_id_get**
> ModerationApp get_moderation_app_moderation_apps_app_id_get(app_id, include_outdated=include_outdated, include_handled=include_handled, limit=limit, offset=offset)

Get Moderation App

Get a list of moderation requests for an app.

### Example


```python
import openapi_client
from openapi_client.models.moderation_app import ModerationApp
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://flathub.org/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://flathub.org/api/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ModerationApi(api_client)
    app_id = 'app_id_example' # str | 
    include_outdated = False # bool |  (optional) (default to False)
    include_handled = False # bool |  (optional) (default to False)
    limit = 100 # int |  (optional) (default to 100)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # Get Moderation App
        api_response = api_instance.get_moderation_app_moderation_apps_app_id_get(app_id, include_outdated=include_outdated, include_handled=include_handled, limit=limit, offset=offset)
        print("The response of ModerationApi->get_moderation_app_moderation_apps_app_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModerationApi->get_moderation_app_moderation_apps_app_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **include_outdated** | **bool**|  | [optional] [default to False]
 **include_handled** | **bool**|  | [optional] [default to False]
 **limit** | **int**|  | [optional] [default to 100]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**ModerationApp**](ModerationApp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_moderation_apps_moderation_apps_get**
> ModerationAppsResponse get_moderation_apps_moderation_apps_get(new_submissions=new_submissions, show_handled=show_handled, limit=limit, offset=offset)

Get Moderation Apps

Get a list of apps with unhandled moderation requests.

### Example


```python
import openapi_client
from openapi_client.models.moderation_apps_response import ModerationAppsResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://flathub.org/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://flathub.org/api/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ModerationApi(api_client)
    new_submissions = True # bool |  (optional)
    show_handled = False # bool |  (optional) (default to False)
    limit = 100 # int |  (optional) (default to 100)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # Get Moderation Apps
        api_response = api_instance.get_moderation_apps_moderation_apps_get(new_submissions=new_submissions, show_handled=show_handled, limit=limit, offset=offset)
        print("The response of ModerationApi->get_moderation_apps_moderation_apps_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModerationApi->get_moderation_apps_moderation_apps_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_submissions** | **bool**|  | [optional] 
 **show_handled** | **bool**|  | [optional] [default to False]
 **limit** | **int**|  | [optional] [default to 100]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**ModerationAppsResponse**](ModerationAppsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_review_moderation_requests_id_review_post**
> ReviewResponse submit_review_moderation_requests_id_review_post(id, review)

Submit Review

Approve or reject the moderation request with a comment. If all requests for a job are approved, the job is
marked as successful in flat-manager.

### Example


```python
import openapi_client
from openapi_client.models.review import Review
from openapi_client.models.review_response import ReviewResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://flathub.org/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://flathub.org/api/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ModerationApi(api_client)
    id = 56 # int | 
    review = openapi_client.Review() # Review | 

    try:
        # Submit Review
        api_response = api_instance.submit_review_moderation_requests_id_review_post(id, review)
        print("The response of ModerationApi->submit_review_moderation_requests_id_review_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModerationApi->submit_review_moderation_requests_id_review_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **review** | [**Review**](Review.md)|  | 

### Return type

[**ReviewResponse**](ReviewResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_review_request_moderation_submit_review_request_post**
> ReviewRequestResponse submit_review_request_moderation_submit_review_request_post(review_request)

Submit Review Request

### Example

* Bearer Authentication (HTTPBearer):

```python
import openapi_client
from openapi_client.models.review_request import ReviewRequest
from openapi_client.models.review_request_response import ReviewRequestResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://flathub.org/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://flathub.org/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ModerationApi(api_client)
    review_request = openapi_client.ReviewRequest() # ReviewRequest | 

    try:
        # Submit Review Request
        api_response = api_instance.submit_review_request_moderation_submit_review_request_post(review_request)
        print("The response of ModerationApi->submit_review_request_moderation_submit_review_request_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModerationApi->submit_review_request_moderation_submit_review_request_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **review_request** | [**ReviewRequest**](ReviewRequest.md)|  | 

### Return type

[**ReviewRequestResponse**](ReviewRequestResponse.md)

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

