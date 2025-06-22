# openapi_client.CompatApi

All URIs are relative to *https://flathub.org/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_popular_apps_compat_apps_collection_popular50_get**](CompatApi.md#get_popular_apps_compat_apps_collection_popular50_get) | **GET** /compat/apps/collection/popular/50 | Get Popular Apps
[**get_popular_apps_compat_apps_collection_popular_get**](CompatApi.md#get_popular_apps_compat_apps_collection_popular_get) | **GET** /compat/apps/collection/popular | Get Popular Apps
[**get_recently_added_compat_apps_collection_new25_get**](CompatApi.md#get_recently_added_compat_apps_collection_new25_get) | **GET** /compat/apps/collection/new/25 | Get Recently Added
[**get_recently_added_compat_apps_collection_new_get**](CompatApi.md#get_recently_added_compat_apps_collection_new_get) | **GET** /compat/apps/collection/new | Get Recently Added
[**get_recently_updated_compat_apps_collection_recently_updated25_get**](CompatApi.md#get_recently_updated_compat_apps_collection_recently_updated25_get) | **GET** /compat/apps/collection/recently-updated/25 | Get Recently Updated
[**get_recently_updated_compat_apps_collection_recently_updated_get**](CompatApi.md#get_recently_updated_compat_apps_collection_recently_updated_get) | **GET** /compat/apps/collection/recently-updated | Get Recently Updated
[**get_search_compat_apps_search_query_get**](CompatApi.md#get_search_compat_apps_search_query_get) | **GET** /compat/apps/search/{query} | Get Search
[**get_single_app_compat_apps_app_id_get**](CompatApi.md#get_single_app_compat_apps_app_id_get) | **GET** /compat/apps/{app_id} | Get Single App


# **get_popular_apps_compat_apps_collection_popular50_get**
> object get_popular_apps_compat_apps_collection_popular50_get()

Get Popular Apps

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
    api_instance = openapi_client.CompatApi(api_client)

    try:
        # Get Popular Apps
        api_response = api_instance.get_popular_apps_compat_apps_collection_popular50_get()
        print("The response of CompatApi->get_popular_apps_compat_apps_collection_popular50_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompatApi->get_popular_apps_compat_apps_collection_popular50_get: %s\n" % e)
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

# **get_popular_apps_compat_apps_collection_popular_get**
> object get_popular_apps_compat_apps_collection_popular_get()

Get Popular Apps

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
    api_instance = openapi_client.CompatApi(api_client)

    try:
        # Get Popular Apps
        api_response = api_instance.get_popular_apps_compat_apps_collection_popular_get()
        print("The response of CompatApi->get_popular_apps_compat_apps_collection_popular_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompatApi->get_popular_apps_compat_apps_collection_popular_get: %s\n" % e)
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

# **get_recently_added_compat_apps_collection_new25_get**
> object get_recently_added_compat_apps_collection_new25_get()

Get Recently Added

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
    api_instance = openapi_client.CompatApi(api_client)

    try:
        # Get Recently Added
        api_response = api_instance.get_recently_added_compat_apps_collection_new25_get()
        print("The response of CompatApi->get_recently_added_compat_apps_collection_new25_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompatApi->get_recently_added_compat_apps_collection_new25_get: %s\n" % e)
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

# **get_recently_added_compat_apps_collection_new_get**
> object get_recently_added_compat_apps_collection_new_get()

Get Recently Added

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
    api_instance = openapi_client.CompatApi(api_client)

    try:
        # Get Recently Added
        api_response = api_instance.get_recently_added_compat_apps_collection_new_get()
        print("The response of CompatApi->get_recently_added_compat_apps_collection_new_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompatApi->get_recently_added_compat_apps_collection_new_get: %s\n" % e)
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

# **get_recently_updated_compat_apps_collection_recently_updated25_get**
> object get_recently_updated_compat_apps_collection_recently_updated25_get()

Get Recently Updated

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
    api_instance = openapi_client.CompatApi(api_client)

    try:
        # Get Recently Updated
        api_response = api_instance.get_recently_updated_compat_apps_collection_recently_updated25_get()
        print("The response of CompatApi->get_recently_updated_compat_apps_collection_recently_updated25_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompatApi->get_recently_updated_compat_apps_collection_recently_updated25_get: %s\n" % e)
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

# **get_recently_updated_compat_apps_collection_recently_updated_get**
> object get_recently_updated_compat_apps_collection_recently_updated_get()

Get Recently Updated

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
    api_instance = openapi_client.CompatApi(api_client)

    try:
        # Get Recently Updated
        api_response = api_instance.get_recently_updated_compat_apps_collection_recently_updated_get()
        print("The response of CompatApi->get_recently_updated_compat_apps_collection_recently_updated_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompatApi->get_recently_updated_compat_apps_collection_recently_updated_get: %s\n" % e)
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

# **get_search_compat_apps_search_query_get**
> object get_search_compat_apps_search_query_get(query, locale=locale)

Get Search

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
    api_instance = openapi_client.CompatApi(api_client)
    query = 'query_example' # str | 
    locale = 'en' # str |  (optional) (default to 'en')

    try:
        # Get Search
        api_response = api_instance.get_search_compat_apps_search_query_get(query, locale=locale)
        print("The response of CompatApi->get_search_compat_apps_search_query_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompatApi->get_search_compat_apps_search_query_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | 
 **locale** | **str**|  | [optional] [default to &#39;en&#39;]

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

# **get_single_app_compat_apps_app_id_get**
> object get_single_app_compat_apps_app_id_get(app_id)

Get Single App

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
    api_instance = openapi_client.CompatApi(api_client)
    app_id = 'app_id_example' # str | 

    try:
        # Get Single App
        api_response = api_instance.get_single_app_compat_apps_app_id_get(app_id)
        print("The response of CompatApi->get_single_app_compat_apps_app_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompatApi->get_single_app_compat_apps_app_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 

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

