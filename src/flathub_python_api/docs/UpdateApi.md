# flathub_python_api.UpdateApi

All URIs are relative to *https://flathub.org/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**process_transfers_update_process_pending_transfers_post**](UpdateApi.md#process_transfers_update_process_pending_transfers_post) | **POST** /update/process-pending-transfers | Process Transfers
[**update_stats_update_stats_post**](UpdateApi.md#update_stats_update_stats_post) | **POST** /update/stats | Update Stats
[**update_update_post**](UpdateApi.md#update_update_post) | **POST** /update | Update


# **process_transfers_update_process_pending_transfers_post**
> object process_transfers_update_process_pending_transfers_post()

Process Transfers

Process any pending transfers which may be in the system

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
    api_instance = flathub_python_api.UpdateApi(api_client)

    try:
        # Process Transfers
        api_response = api_instance.process_transfers_update_process_pending_transfers_post()
        print("The response of UpdateApi->process_transfers_update_process_pending_transfers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UpdateApi->process_transfers_update_process_pending_transfers_post: %s\n" % e)
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

# **update_stats_update_stats_post**
> object update_stats_update_stats_post()

Update Stats

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
    api_instance = flathub_python_api.UpdateApi(api_client)

    try:
        # Update Stats
        api_response = api_instance.update_stats_update_stats_post()
        print("The response of UpdateApi->update_stats_update_stats_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UpdateApi->update_stats_update_stats_post: %s\n" % e)
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

# **update_update_post**
> object update_update_post()

Update

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
    api_instance = flathub_python_api.UpdateApi(api_client)

    try:
        # Update
        api_response = api_instance.update_update_post()
        print("The response of UpdateApi->update_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UpdateApi->update_update_post: %s\n" % e)
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

