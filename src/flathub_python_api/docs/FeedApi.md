# flathub_python_api.FeedApi

All URIs are relative to *https://flathub.org/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_new_apps_feed_feed_new_get**](FeedApi.md#get_new_apps_feed_feed_new_get) | **GET** /feed/new | Get New Apps Feed
[**get_recently_updated_apps_feed_feed_recently_updated_get**](FeedApi.md#get_recently_updated_apps_feed_feed_recently_updated_get) | **GET** /feed/recently-updated | Get Recently Updated Apps Feed


# **get_new_apps_feed_feed_new_get**
> object get_new_apps_feed_feed_new_get()

Get New Apps Feed

### Example


```python
import flathub_python_api
from flathub_python_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://flathub.org/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = flathub_python_api.Configuration(
    host = "https://flathub.org/api/v2"
)


# Enter a context with an instance of the API client
with flathub_python_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flathub_python_api.FeedApi(api_client)

    try:
        # Get New Apps Feed
        api_response = api_instance.get_new_apps_feed_feed_new_get()
        print("The response of FeedApi->get_new_apps_feed_feed_new_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeedApi->get_new_apps_feed_feed_new_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recently_updated_apps_feed_feed_recently_updated_get**
> object get_recently_updated_apps_feed_feed_recently_updated_get()

Get Recently Updated Apps Feed

### Example


```python
import flathub_python_api
from flathub_python_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://flathub.org/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = flathub_python_api.Configuration(
    host = "https://flathub.org/api/v2"
)


# Enter a context with an instance of the API client
with flathub_python_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flathub_python_api.FeedApi(api_client)

    try:
        # Get Recently Updated Apps Feed
        api_response = api_instance.get_recently_updated_apps_feed_feed_recently_updated_get()
        print("The response of FeedApi->get_recently_updated_apps_feed_feed_recently_updated_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeedApi->get_recently_updated_apps_feed_feed_recently_updated_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

