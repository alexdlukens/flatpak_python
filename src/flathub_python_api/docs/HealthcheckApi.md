# flathub_python_api.HealthcheckApi

All URIs are relative to *https://flathub.org/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**healthcheck_status_get**](HealthcheckApi.md#healthcheck_status_get) | **GET** /status | Healthcheck


# **healthcheck_status_get**
> object healthcheck_status_get()

Healthcheck

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
    api_instance = flathub_python_api.HealthcheckApi(api_client)

    try:
        # Healthcheck
        api_response = api_instance.healthcheck_status_get()
        print("The response of HealthcheckApi->healthcheck_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthcheckApi->healthcheck_status_get: %s\n" % e)
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

