# flathub_python_api.QualityModerationApi

All URIs are relative to *https://flathub.org/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_review_request_for_app_quality_moderation_app_id_request_review_delete**](QualityModerationApi.md#delete_review_request_for_app_quality_moderation_app_id_request_review_delete) | **DELETE** /quality-moderation/{app_id}/request-review | Delete Review Request For App
[**get_app_pick_recommendations_quality_moderation_app_pick_recommendations_get**](QualityModerationApi.md#get_app_pick_recommendations_quality_moderation_app_pick_recommendations_get) | **GET** /quality-moderation/app-pick-recommendations | Get App Pick Recommendations
[**get_passing_quality_apps_quality_moderation_passing_apps_get**](QualityModerationApi.md#get_passing_quality_apps_quality_moderation_passing_apps_get) | **GET** /quality-moderation/passing-apps | Get Passing Quality Apps
[**get_quality_moderation_for_app_quality_moderation_app_id_get**](QualityModerationApi.md#get_quality_moderation_for_app_quality_moderation_app_id_get) | **GET** /quality-moderation/{app_id} | Get Quality Moderation For App
[**get_quality_moderation_stats_quality_moderation_failed_by_guideline_get**](QualityModerationApi.md#get_quality_moderation_stats_quality_moderation_failed_by_guideline_get) | **GET** /quality-moderation/failed-by-guideline | Get Quality Moderation Stats
[**get_quality_moderation_status_for_app_quality_moderation_app_id_status_get**](QualityModerationApi.md#get_quality_moderation_status_for_app_quality_moderation_app_id_status_get) | **GET** /quality-moderation/{app_id}/status | Get Quality Moderation Status For App
[**get_quality_moderation_status_quality_moderation_status_get**](QualityModerationApi.md#get_quality_moderation_status_quality_moderation_status_get) | **GET** /quality-moderation/status | Get Quality Moderation Status
[**request_review_for_app_quality_moderation_app_id_request_review_post**](QualityModerationApi.md#request_review_for_app_quality_moderation_app_id_request_review_post) | **POST** /quality-moderation/{app_id}/request-review | Request Review For App
[**set_fullscreen_app_quality_moderation_app_id_fullscreen_post**](QualityModerationApi.md#set_fullscreen_app_quality_moderation_app_id_fullscreen_post) | **POST** /quality-moderation/{app_id}/fullscreen | Set Fullscreen App
[**set_quality_moderation_for_app_quality_moderation_app_id_post**](QualityModerationApi.md#set_quality_moderation_for_app_quality_moderation_app_id_post) | **POST** /quality-moderation/{app_id} | Set Quality Moderation For App


# **delete_review_request_for_app_quality_moderation_app_id_request_review_delete**
> object delete_review_request_for_app_quality_moderation_app_id_request_review_delete(app_id)

Delete Review Request For App

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
    api_instance = flathub_python_api.QualityModerationApi(api_client)
    app_id = 'app_id_example' # str | 

    try:
        # Delete Review Request For App
        api_response = api_instance.delete_review_request_for_app_quality_moderation_app_id_request_review_delete(app_id)
        print("The response of QualityModerationApi->delete_review_request_for_app_quality_moderation_app_id_request_review_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualityModerationApi->delete_review_request_for_app_quality_moderation_app_id_request_review_delete: %s\n" % e)
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

# **get_app_pick_recommendations_quality_moderation_app_pick_recommendations_get**
> AppPickRecommendationsResponse get_app_pick_recommendations_quality_moderation_app_pick_recommendations_get(recommendation_date=recommendation_date)

Get App Pick Recommendations

### Example


```python
import flathub_python_api
from flathub_python_api.models.app_pick_recommendations_response import AppPickRecommendationsResponse
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
    api_instance = flathub_python_api.QualityModerationApi(api_client)
    recommendation_date = '2013-10-20' # date |  (optional)

    try:
        # Get App Pick Recommendations
        api_response = api_instance.get_app_pick_recommendations_quality_moderation_app_pick_recommendations_get(recommendation_date=recommendation_date)
        print("The response of QualityModerationApi->get_app_pick_recommendations_quality_moderation_app_pick_recommendations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualityModerationApi->get_app_pick_recommendations_quality_moderation_app_pick_recommendations_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recommendation_date** | **date**|  | [optional] 

### Return type

[**AppPickRecommendationsResponse**](AppPickRecommendationsResponse.md)

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

# **get_passing_quality_apps_quality_moderation_passing_apps_get**
> SimpleQualityModerationResponse get_passing_quality_apps_quality_moderation_passing_apps_get(page=page, page_size=page_size)

Get Passing Quality Apps

### Example


```python
import flathub_python_api
from flathub_python_api.models.simple_quality_moderation_response import SimpleQualityModerationResponse
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
    api_instance = flathub_python_api.QualityModerationApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    page_size = 25 # int |  (optional) (default to 25)

    try:
        # Get Passing Quality Apps
        api_response = api_instance.get_passing_quality_apps_quality_moderation_passing_apps_get(page=page, page_size=page_size)
        print("The response of QualityModerationApi->get_passing_quality_apps_quality_moderation_passing_apps_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualityModerationApi->get_passing_quality_apps_quality_moderation_passing_apps_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 25]

### Return type

[**SimpleQualityModerationResponse**](SimpleQualityModerationResponse.md)

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

# **get_quality_moderation_for_app_quality_moderation_app_id_get**
> QualityModerationResponse get_quality_moderation_for_app_quality_moderation_app_id_get(app_id)

Get Quality Moderation For App

### Example


```python
import flathub_python_api
from flathub_python_api.models.quality_moderation_response import QualityModerationResponse
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
    api_instance = flathub_python_api.QualityModerationApi(api_client)
    app_id = 'app_id_example' # str | 

    try:
        # Get Quality Moderation For App
        api_response = api_instance.get_quality_moderation_for_app_quality_moderation_app_id_get(app_id)
        print("The response of QualityModerationApi->get_quality_moderation_for_app_quality_moderation_app_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualityModerationApi->get_quality_moderation_for_app_quality_moderation_app_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 

### Return type

[**QualityModerationResponse**](QualityModerationResponse.md)

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

# **get_quality_moderation_stats_quality_moderation_failed_by_guideline_get**
> List[FailedByGuideline] get_quality_moderation_stats_quality_moderation_failed_by_guideline_get()

Get Quality Moderation Stats

### Example


```python
import flathub_python_api
from flathub_python_api.models.failed_by_guideline import FailedByGuideline
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
    api_instance = flathub_python_api.QualityModerationApi(api_client)

    try:
        # Get Quality Moderation Stats
        api_response = api_instance.get_quality_moderation_stats_quality_moderation_failed_by_guideline_get()
        print("The response of QualityModerationApi->get_quality_moderation_stats_quality_moderation_failed_by_guideline_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualityModerationApi->get_quality_moderation_stats_quality_moderation_failed_by_guideline_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[FailedByGuideline]**](FailedByGuideline.md)

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

# **get_quality_moderation_status_for_app_quality_moderation_app_id_status_get**
> QualityModerationStatus get_quality_moderation_status_for_app_quality_moderation_app_id_status_get(app_id)

Get Quality Moderation Status For App

### Example


```python
import flathub_python_api
from flathub_python_api.models.quality_moderation_status import QualityModerationStatus
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
    api_instance = flathub_python_api.QualityModerationApi(api_client)
    app_id = 'app_id_example' # str | 

    try:
        # Get Quality Moderation Status For App
        api_response = api_instance.get_quality_moderation_status_for_app_quality_moderation_app_id_status_get(app_id)
        print("The response of QualityModerationApi->get_quality_moderation_status_for_app_quality_moderation_app_id_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualityModerationApi->get_quality_moderation_status_for_app_quality_moderation_app_id_status_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 

### Return type

[**QualityModerationStatus**](QualityModerationStatus.md)

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

# **get_quality_moderation_status_quality_moderation_status_get**
> QualityModerationDashboardResponse get_quality_moderation_status_quality_moderation_status_get(page=page, page_size=page_size, filter=filter)

Get Quality Moderation Status

### Example


```python
import flathub_python_api
from flathub_python_api.models.quality_moderation_dashboard_response import QualityModerationDashboardResponse
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
    api_instance = flathub_python_api.QualityModerationApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    page_size = 25 # int |  (optional) (default to 25)
    filter = all # str |  (optional) (default to all)

    try:
        # Get Quality Moderation Status
        api_response = api_instance.get_quality_moderation_status_quality_moderation_status_get(page=page, page_size=page_size, filter=filter)
        print("The response of QualityModerationApi->get_quality_moderation_status_quality_moderation_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualityModerationApi->get_quality_moderation_status_quality_moderation_status_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 25]
 **filter** | **str**|  | [optional] [default to all]

### Return type

[**QualityModerationDashboardResponse**](QualityModerationDashboardResponse.md)

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

# **request_review_for_app_quality_moderation_app_id_request_review_post**
> object request_review_for_app_quality_moderation_app_id_request_review_post(app_id)

Request Review For App

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
    api_instance = flathub_python_api.QualityModerationApi(api_client)
    app_id = 'app_id_example' # str | 

    try:
        # Request Review For App
        api_response = api_instance.request_review_for_app_quality_moderation_app_id_request_review_post(app_id)
        print("The response of QualityModerationApi->request_review_for_app_quality_moderation_app_id_request_review_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualityModerationApi->request_review_for_app_quality_moderation_app_id_request_review_post: %s\n" % e)
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

# **set_fullscreen_app_quality_moderation_app_id_fullscreen_post**
> object set_fullscreen_app_quality_moderation_app_id_fullscreen_post(app_id, is_fullscreen_app)

Set Fullscreen App

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
    api_instance = flathub_python_api.QualityModerationApi(api_client)
    app_id = 'app_id_example' # str | 
    is_fullscreen_app = True # bool | 

    try:
        # Set Fullscreen App
        api_response = api_instance.set_fullscreen_app_quality_moderation_app_id_fullscreen_post(app_id, is_fullscreen_app)
        print("The response of QualityModerationApi->set_fullscreen_app_quality_moderation_app_id_fullscreen_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualityModerationApi->set_fullscreen_app_quality_moderation_app_id_fullscreen_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **is_fullscreen_app** | **bool**|  | 

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

# **set_quality_moderation_for_app_quality_moderation_app_id_post**
> object set_quality_moderation_for_app_quality_moderation_app_id_post(app_id, upsert_quality_moderation)

Set Quality Moderation For App

### Example


```python
import flathub_python_api
from flathub_python_api.models.upsert_quality_moderation import UpsertQualityModeration
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
    api_instance = flathub_python_api.QualityModerationApi(api_client)
    app_id = 'app_id_example' # str | 
    upsert_quality_moderation = flathub_python_api.UpsertQualityModeration() # UpsertQualityModeration | 

    try:
        # Set Quality Moderation For App
        api_response = api_instance.set_quality_moderation_for_app_quality_moderation_app_id_post(app_id, upsert_quality_moderation)
        print("The response of QualityModerationApi->set_quality_moderation_for_app_quality_moderation_app_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualityModerationApi->set_quality_moderation_for_app_quality_moderation_app_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **upsert_quality_moderation** | [**UpsertQualityModeration**](UpsertQualityModeration.md)|  | 

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

