# openapi_client.StatsApi

All URIs are relative to *https://flathub.org/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_stats_for_app_stats_app_id_get**](StatsApi.md#get_stats_for_app_stats_app_id_get) | **GET** /stats/{app_id} | Get Stats For App
[**get_stats_stats_get**](StatsApi.md#get_stats_stats_get) | **GET** /stats/ | Get Stats


# **get_stats_for_app_stats_app_id_get**
> object get_stats_for_app_stats_app_id_get(app_id, all=all, days=days)

Get Stats For App

### Example


```python
import openapi_client
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
    api_instance = openapi_client.StatsApi(api_client)
    app_id = 'app_id_example' # str | 
    all = False # bool |  (optional) (default to False)
    days = 180 # int |  (optional) (default to 180)

    try:
        # Get Stats For App
        api_response = api_instance.get_stats_for_app_stats_app_id_get(app_id, all=all, days=days)
        print("The response of StatsApi->get_stats_for_app_stats_app_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->get_stats_for_app_stats_app_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **all** | **bool**|  | [optional] [default to False]
 **days** | **int**|  | [optional] [default to 180]

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stats_stats_get**
> StatsResult get_stats_stats_get()

Get Stats

### Example


```python
import openapi_client
from openapi_client.models.stats_result import StatsResult
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
    api_instance = openapi_client.StatsApi(api_client)

    try:
        # Get Stats
        api_response = api_instance.get_stats_stats_get()
        print("The response of StatsApi->get_stats_stats_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->get_stats_stats_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**StatsResult**](StatsResult.md)

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

