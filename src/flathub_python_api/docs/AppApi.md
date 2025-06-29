# flathub_python_api.AppApi

All URIs are relative to *https://flathub.org/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_to_favorites_favorites_app_id_add_post**](AppApi.md#add_to_favorites_favorites_app_id_add_post) | **POST** /favorites/{app_id}/add | Add To Favorites
[**get_addons_addon_app_id_get**](AppApi.md#get_addons_addon_app_id_get) | **GET** /addon/{app_id} | Get Addons
[**get_appstream_appstream_app_id_get**](AppApi.md#get_appstream_appstream_app_id_get) | **GET** /appstream/{app_id} | Get Appstream
[**get_eol_message_appid_eol_message_app_id_get**](AppApi.md#get_eol_message_appid_eol_message_app_id_get) | **GET** /eol/message/{app_id} | Get Eol Message Appid
[**get_eol_message_eol_message_get**](AppApi.md#get_eol_message_eol_message_get) | **GET** /eol/message | Get Eol Message
[**get_eol_rebase_appid_eol_rebase_app_id_get**](AppApi.md#get_eol_rebase_appid_eol_rebase_app_id_get) | **GET** /eol/rebase/{app_id} | Get Eol Rebase Appid
[**get_eol_rebase_eol_rebase_get**](AppApi.md#get_eol_rebase_eol_rebase_get) | **GET** /eol/rebase | Get Eol Rebase
[**get_exceptions_exceptions_get**](AppApi.md#get_exceptions_exceptions_get) | **GET** /exceptions/ | Get Exceptions
[**get_exceptions_exceptions_get_0**](AppApi.md#get_exceptions_exceptions_get_0) | **GET** /exceptions/ | Get Exceptions
[**get_exceptions_for_app_exceptions_app_id_get**](AppApi.md#get_exceptions_for_app_exceptions_app_id_get) | **GET** /exceptions/{app_id} | Get Exceptions For App
[**get_exceptions_for_app_exceptions_app_id_get_0**](AppApi.md#get_exceptions_for_app_exceptions_app_id_get_0) | **GET** /exceptions/{app_id} | Get Exceptions For App
[**get_favorites_favorites_get**](AppApi.md#get_favorites_favorites_get) | **GET** /favorites | Get Favorites
[**get_is_fullscreen_app_is_fullscreen_app_app_id_get**](AppApi.md#get_is_fullscreen_app_is_fullscreen_app_app_id_get) | **GET** /is-fullscreen-app/{app_id} | Get Isfullscreenapp
[**get_platforms_platforms_get**](AppApi.md#get_platforms_platforms_get) | **GET** /platforms | Get Platforms
[**get_runtime_list_runtimes_get**](AppApi.md#get_runtime_list_runtimes_get) | **GET** /runtimes | Get Runtime List
[**get_summary_summary_app_id_get**](AppApi.md#get_summary_summary_app_id_get) | **GET** /summary/{app_id} | Get Summary
[**is_favorited_favorites_app_id_get**](AppApi.md#is_favorited_favorites_app_id_get) | **GET** /favorites/{app_id} | Is Favorited
[**list_appstream_appstream_get**](AppApi.md#list_appstream_appstream_get) | **GET** /appstream | List Appstream
[**post_search_search_post**](AppApi.md#post_search_search_post) | **POST** /search | Post Search
[**remove_from_favorites_favorites_app_id_remove_delete**](AppApi.md#remove_from_favorites_favorites_app_id_remove_delete) | **DELETE** /favorites/{app_id}/remove | Remove From Favorites


# **add_to_favorites_favorites_app_id_add_post**
> object add_to_favorites_favorites_app_id_add_post(app_id)

Add To Favorites

Add an app to a users favorites. The appid is the ID of the app to add.

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
    api_instance = flathub_python_api.AppApi(api_client)
    app_id = 'app_id_example' # str | 

    try:
        # Add To Favorites
        api_response = api_instance.add_to_favorites_favorites_app_id_add_post(app_id)
        print("The response of AppApi->add_to_favorites_favorites_app_id_add_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppApi->add_to_favorites_favorites_app_id_add_post: %s\n" % e)
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

# **get_addons_addon_app_id_get**
> List[Optional[str]] get_addons_addon_app_id_get(app_id)

Get Addons

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
    api_instance = flathub_python_api.AppApi(api_client)
    app_id = 'app_id_example' # str | 

    try:
        # Get Addons
        api_response = api_instance.get_addons_addon_app_id_get(app_id)
        print("The response of AppApi->get_addons_addon_app_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppApi->get_addons_addon_app_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 

### Return type

**List[Optional[str]]**

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

# **get_appstream_appstream_app_id_get**
> object get_appstream_appstream_app_id_get(app_id, locale=locale)

Get Appstream

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
    api_instance = flathub_python_api.AppApi(api_client)
    app_id = 'app_id_example' # str | 
    locale = 'en' # str |  (optional) (default to 'en')

    try:
        # Get Appstream
        api_response = api_instance.get_appstream_appstream_app_id_get(app_id, locale=locale)
        print("The response of AppApi->get_appstream_appstream_app_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppApi->get_appstream_appstream_app_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
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

# **get_eol_message_appid_eol_message_app_id_get**
> str get_eol_message_appid_eol_message_app_id_get(app_id, branch=branch)

Get Eol Message Appid

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
    api_instance = flathub_python_api.AppApi(api_client)
    app_id = 'app_id_example' # str | 
    branch = 'stable' # str |  (optional) (default to 'stable')

    try:
        # Get Eol Message Appid
        api_response = api_instance.get_eol_message_appid_eol_message_app_id_get(app_id, branch=branch)
        print("The response of AppApi->get_eol_message_appid_eol_message_app_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppApi->get_eol_message_appid_eol_message_app_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **branch** | **str**|  | [optional] [default to &#39;stable&#39;]

### Return type

**str**

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

# **get_eol_message_eol_message_get**
> Dict[str, Optional[str]] get_eol_message_eol_message_get()

Get Eol Message

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
    api_instance = flathub_python_api.AppApi(api_client)

    try:
        # Get Eol Message
        api_response = api_instance.get_eol_message_eol_message_get()
        print("The response of AppApi->get_eol_message_eol_message_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppApi->get_eol_message_eol_message_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, Optional[str]]**

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

# **get_eol_rebase_appid_eol_rebase_app_id_get**
> str get_eol_rebase_appid_eol_rebase_app_id_get(app_id, branch=branch)

Get Eol Rebase Appid

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
    api_instance = flathub_python_api.AppApi(api_client)
    app_id = 'app_id_example' # str | 
    branch = 'stable' # str |  (optional) (default to 'stable')

    try:
        # Get Eol Rebase Appid
        api_response = api_instance.get_eol_rebase_appid_eol_rebase_app_id_get(app_id, branch=branch)
        print("The response of AppApi->get_eol_rebase_appid_eol_rebase_app_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppApi->get_eol_rebase_appid_eol_rebase_app_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **branch** | **str**|  | [optional] [default to &#39;stable&#39;]

### Return type

**str**

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

# **get_eol_rebase_eol_rebase_get**
> Dict[str, List[str]] get_eol_rebase_eol_rebase_get()

Get Eol Rebase

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
    api_instance = flathub_python_api.AppApi(api_client)

    try:
        # Get Eol Rebase
        api_response = api_instance.get_eol_rebase_eol_rebase_get()
        print("The response of AppApi->get_eol_rebase_eol_rebase_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppApi->get_eol_rebase_eol_rebase_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, List[str]]**

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

# **get_exceptions_exceptions_get**
> object get_exceptions_exceptions_get()

Get Exceptions

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
    api_instance = flathub_python_api.AppApi(api_client)

    try:
        # Get Exceptions
        api_response = api_instance.get_exceptions_exceptions_get()
        print("The response of AppApi->get_exceptions_exceptions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppApi->get_exceptions_exceptions_get: %s\n" % e)
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

# **get_exceptions_exceptions_get_0**
> object get_exceptions_exceptions_get_0()

Get Exceptions

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
    api_instance = flathub_python_api.AppApi(api_client)

    try:
        # Get Exceptions
        api_response = api_instance.get_exceptions_exceptions_get_0()
        print("The response of AppApi->get_exceptions_exceptions_get_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppApi->get_exceptions_exceptions_get_0: %s\n" % e)
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

# **get_exceptions_for_app_exceptions_app_id_get**
> object get_exceptions_for_app_exceptions_app_id_get(app_id)

Get Exceptions For App

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
    api_instance = flathub_python_api.AppApi(api_client)
    app_id = 'app_id_example' # str | 

    try:
        # Get Exceptions For App
        api_response = api_instance.get_exceptions_for_app_exceptions_app_id_get(app_id)
        print("The response of AppApi->get_exceptions_for_app_exceptions_app_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppApi->get_exceptions_for_app_exceptions_app_id_get: %s\n" % e)
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

# **get_exceptions_for_app_exceptions_app_id_get_0**
> object get_exceptions_for_app_exceptions_app_id_get_0(app_id)

Get Exceptions For App

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
    api_instance = flathub_python_api.AppApi(api_client)
    app_id = 'app_id_example' # str | 

    try:
        # Get Exceptions For App
        api_response = api_instance.get_exceptions_for_app_exceptions_app_id_get_0(app_id)
        print("The response of AppApi->get_exceptions_for_app_exceptions_app_id_get_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppApi->get_exceptions_for_app_exceptions_app_id_get_0: %s\n" % e)
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

# **get_favorites_favorites_get**
> List[FavoriteApp] get_favorites_favorites_get()

Get Favorites

Get a list of the users favorite apps.

### Example


```python
import flathub_python_api
from flathub_python_api.models.favorite_app import FavoriteApp
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
    api_instance = flathub_python_api.AppApi(api_client)

    try:
        # Get Favorites
        api_response = api_instance.get_favorites_favorites_get()
        print("The response of AppApi->get_favorites_favorites_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppApi->get_favorites_favorites_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[FavoriteApp]**](FavoriteApp.md)

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

# **get_is_fullscreen_app_is_fullscreen_app_app_id_get**
> bool get_is_fullscreen_app_is_fullscreen_app_app_id_get(app_id)

Get Isfullscreenapp

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
    api_instance = flathub_python_api.AppApi(api_client)
    app_id = 'app_id_example' # str | 

    try:
        # Get Isfullscreenapp
        api_response = api_instance.get_is_fullscreen_app_is_fullscreen_app_app_id_get(app_id)
        print("The response of AppApi->get_is_fullscreen_app_is_fullscreen_app_app_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppApi->get_is_fullscreen_app_is_fullscreen_app_app_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 

### Return type

**bool**

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

# **get_platforms_platforms_get**
> Dict[str, Platform] get_platforms_platforms_get()

Get Platforms

Return a mapping from org-name to platform aliases and dependencies which are
recognised by the backend.  These are used by things such as the transactions
and donations APIs to address amounts to the platforms.

### Example


```python
import flathub_python_api
from flathub_python_api.models.platform import Platform
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
    api_instance = flathub_python_api.AppApi(api_client)

    try:
        # Get Platforms
        api_response = api_instance.get_platforms_platforms_get()
        print("The response of AppApi->get_platforms_platforms_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppApi->get_platforms_platforms_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Dict[str, Platform]**](Platform.md)

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

# **get_runtime_list_runtimes_get**
> Dict[str, Optional[int]] get_runtime_list_runtimes_get()

Get Runtime List

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
    api_instance = flathub_python_api.AppApi(api_client)

    try:
        # Get Runtime List
        api_response = api_instance.get_runtime_list_runtimes_get()
        print("The response of AppApi->get_runtime_list_runtimes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppApi->get_runtime_list_runtimes_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, Optional[int]]**

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

# **get_summary_summary_app_id_get**
> object get_summary_summary_app_id_get(app_id, branch=branch)

Get Summary

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
    api_instance = flathub_python_api.AppApi(api_client)
    app_id = 'app_id_example' # str | 
    branch = 'branch_example' # str |  (optional)

    try:
        # Get Summary
        api_response = api_instance.get_summary_summary_app_id_get(app_id, branch=branch)
        print("The response of AppApi->get_summary_summary_app_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppApi->get_summary_summary_app_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **branch** | **str**|  | [optional] 

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

# **is_favorited_favorites_app_id_get**
> bool is_favorited_favorites_app_id_get(app_id)

Is Favorited

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
    api_instance = flathub_python_api.AppApi(api_client)
    app_id = 'app_id_example' # str | 

    try:
        # Is Favorited
        api_response = api_instance.is_favorited_favorites_app_id_get(app_id)
        print("The response of AppApi->is_favorited_favorites_app_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppApi->is_favorited_favorites_app_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 

### Return type

**bool**

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

# **list_appstream_appstream_get**
> List[Optional[str]] list_appstream_appstream_get(filter=filter)

List Appstream

### Example


```python
import flathub_python_api
from flathub_python_api.models.app_type import AppType
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
    api_instance = flathub_python_api.AppApi(api_client)
    filter = flathub_python_api.AppType() # AppType |  (optional)

    try:
        # List Appstream
        api_response = api_instance.list_appstream_appstream_get(filter=filter)
        print("The response of AppApi->list_appstream_appstream_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppApi->list_appstream_appstream_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**AppType**](.md)|  | [optional] 

### Return type

**List[Optional[str]]**

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

# **post_search_search_post**
> MeilisearchResponseLimitedAppsIndex post_search_search_post(search_query, locale=locale)

Post Search

### Example


```python
import flathub_python_api
from flathub_python_api.models.meilisearch_response_limited_apps_index import MeilisearchResponseLimitedAppsIndex
from flathub_python_api.models.search_query import SearchQuery
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
    api_instance = flathub_python_api.AppApi(api_client)
    search_query = flathub_python_api.SearchQuery() # SearchQuery | 
    locale = 'en' # str |  (optional) (default to 'en')

    try:
        # Post Search
        api_response = api_instance.post_search_search_post(search_query, locale=locale)
        print("The response of AppApi->post_search_search_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppApi->post_search_search_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_query** | [**SearchQuery**](SearchQuery.md)|  | 
 **locale** | **str**|  | [optional] [default to &#39;en&#39;]

### Return type

[**MeilisearchResponseLimitedAppsIndex**](MeilisearchResponseLimitedAppsIndex.md)

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

# **remove_from_favorites_favorites_app_id_remove_delete**
> object remove_from_favorites_favorites_app_id_remove_delete(app_id)

Remove From Favorites

Remove an app from a users favorites. The appid is the ID of the app to remove.

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
    api_instance = flathub_python_api.AppApi(api_client)
    app_id = 'app_id_example' # str | 

    try:
        # Remove From Favorites
        api_response = api_instance.remove_from_favorites_favorites_app_id_remove_delete(app_id)
        print("The response of AppApi->remove_from_favorites_favorites_app_id_remove_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppApi->remove_from_favorites_favorites_app_id_remove_delete: %s\n" % e)
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

