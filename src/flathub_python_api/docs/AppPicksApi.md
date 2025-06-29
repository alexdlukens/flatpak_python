# flathub_python_api.AppPicksApi

All URIs are relative to *https://flathub.org/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_app_of_the_day_app_picks_app_of_the_day_date_get**](AppPicksApi.md#get_app_of_the_day_app_picks_app_of_the_day_date_get) | **GET** /app-picks/app-of-the-day/{date} | Get App Of The Day
[**get_app_of_the_week_app_picks_apps_of_the_week_date_get**](AppPicksApi.md#get_app_of_the_week_app_picks_apps_of_the_week_date_get) | **GET** /app-picks/apps-of-the-week/{date} | Get App Of The Week
[**set_app_of_the_day_app_picks_app_of_the_day_post**](AppPicksApi.md#set_app_of_the_day_app_picks_app_of_the_day_post) | **POST** /app-picks/app-of-the-day | Set App Of The Day
[**set_app_of_the_week_app_picks_app_of_the_week_post**](AppPicksApi.md#set_app_of_the_week_app_picks_app_of_the_week_post) | **POST** /app-picks/app-of-the-week | Set App Of The Week


# **get_app_of_the_day_app_picks_app_of_the_day_date_get**
> AppOfTheDay get_app_of_the_day_app_picks_app_of_the_day_date_get(var_date)

Get App Of The Day

### Example


```python
import flathub_python_api
from flathub_python_api.models.app_of_the_day import AppOfTheDay
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
    api_instance = flathub_python_api.AppPicksApi(api_client)
    var_date = '2013-10-20' # date | 

    try:
        # Get App Of The Day
        api_response = api_instance.get_app_of_the_day_app_picks_app_of_the_day_date_get(var_date)
        print("The response of AppPicksApi->get_app_of_the_day_app_picks_app_of_the_day_date_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppPicksApi->get_app_of_the_day_app_picks_app_of_the_day_date_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_date** | **date**|  | 

### Return type

[**AppOfTheDay**](AppOfTheDay.md)

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

# **get_app_of_the_week_app_picks_apps_of_the_week_date_get**
> AppsOfTheWeek get_app_of_the_week_app_picks_apps_of_the_week_date_get(var_date)

Get App Of The Week

Returns apps of the week

### Example


```python
import flathub_python_api
from flathub_python_api.models.apps_of_the_week import AppsOfTheWeek
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
    api_instance = flathub_python_api.AppPicksApi(api_client)
    var_date = '2013-10-20' # date | 

    try:
        # Get App Of The Week
        api_response = api_instance.get_app_of_the_week_app_picks_apps_of_the_week_date_get(var_date)
        print("The response of AppPicksApi->get_app_of_the_week_app_picks_apps_of_the_week_date_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppPicksApi->get_app_of_the_week_app_picks_apps_of_the_week_date_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_date** | **date**|  | 

### Return type

[**AppsOfTheWeek**](AppsOfTheWeek.md)

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

# **set_app_of_the_day_app_picks_app_of_the_day_post**
> object set_app_of_the_day_app_picks_app_of_the_day_post(app_of_the_day)

Set App Of The Day

Sets an app of the day

### Example


```python
import flathub_python_api
from flathub_python_api.models.app_of_the_day import AppOfTheDay
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
    api_instance = flathub_python_api.AppPicksApi(api_client)
    app_of_the_day = flathub_python_api.AppOfTheDay() # AppOfTheDay | 

    try:
        # Set App Of The Day
        api_response = api_instance.set_app_of_the_day_app_picks_app_of_the_day_post(app_of_the_day)
        print("The response of AppPicksApi->set_app_of_the_day_app_picks_app_of_the_day_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppPicksApi->set_app_of_the_day_app_picks_app_of_the_day_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_of_the_day** | [**AppOfTheDay**](AppOfTheDay.md)|  | 

### Return type

**object**

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

# **set_app_of_the_week_app_picks_app_of_the_week_post**
> object set_app_of_the_week_app_picks_app_of_the_week_post(upsert_app_of_the_week)

Set App Of The Week

Sets an app of the week

### Example


```python
import flathub_python_api
from flathub_python_api.models.upsert_app_of_the_week import UpsertAppOfTheWeek
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
    api_instance = flathub_python_api.AppPicksApi(api_client)
    upsert_app_of_the_week = flathub_python_api.UpsertAppOfTheWeek() # UpsertAppOfTheWeek | 

    try:
        # Set App Of The Week
        api_response = api_instance.set_app_of_the_week_app_picks_app_of_the_week_post(upsert_app_of_the_week)
        print("The response of AppPicksApi->set_app_of_the_week_app_picks_app_of_the_week_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppPicksApi->set_app_of_the_week_app_picks_app_of_the_week_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_app_of_the_week** | [**UpsertAppOfTheWeek**](UpsertAppOfTheWeek.md)|  | 

### Return type

**object**

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

