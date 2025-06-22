# openapi_client.CollectionApi

All URIs are relative to *https://flathub.org/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_categories_collection_category_get**](CollectionApi.md#get_categories_collection_category_get) | **GET** /collection/category | Get Categories
[**get_category_collection_category_category_get**](CollectionApi.md#get_category_collection_category_category_get) | **GET** /collection/category/{category} | Get Category
[**get_developer_collection_developer_developer_get**](CollectionApi.md#get_developer_collection_developer_developer_get) | **GET** /collection/developer/{developer} | Get Developer
[**get_developers_collection_developer_get**](CollectionApi.md#get_developers_collection_developer_get) | **GET** /collection/developer | Get Developers
[**get_keyword_collection_keyword_get**](CollectionApi.md#get_keyword_collection_keyword_get) | **GET** /collection/keyword | Get Keyword
[**get_mobile_collection_mobile_get**](CollectionApi.md#get_mobile_collection_mobile_get) | **GET** /collection/mobile | Get Mobile
[**get_popular_last_month_collection_popular_get**](CollectionApi.md#get_popular_last_month_collection_popular_get) | **GET** /collection/popular | Get Popular Last Month
[**get_recently_added_collection_recently_added_get**](CollectionApi.md#get_recently_added_collection_recently_added_get) | **GET** /collection/recently-added | Get Recently Added
[**get_recently_updated_collection_recently_updated_get**](CollectionApi.md#get_recently_updated_collection_recently_updated_get) | **GET** /collection/recently-updated | Get Recently Updated
[**get_subcategory_collection_category_category_subcategories_get**](CollectionApi.md#get_subcategory_collection_category_category_subcategories_get) | **GET** /collection/category/{category}/subcategories | Get Subcategory
[**get_trending_last_two_weeks_collection_trending_get**](CollectionApi.md#get_trending_last_two_weeks_collection_trending_get) | **GET** /collection/trending | Get Trending Last Two Weeks
[**get_verified_collection_verified_get**](CollectionApi.md#get_verified_collection_verified_get) | **GET** /collection/verified | Get Verified


# **get_categories_collection_category_get**
> List[Optional[str]] get_categories_collection_category_get()

Get Categories

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
    api_instance = openapi_client.CollectionApi(api_client)

    try:
        # Get Categories
        api_response = api_instance.get_categories_collection_category_get()
        print("The response of CollectionApi->get_categories_collection_category_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionApi->get_categories_collection_category_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_category_collection_category_category_get**
> MeilisearchResponseAppsIndex get_category_collection_category_category_get(category, exclude_subcategories=exclude_subcategories, page=page, per_page=per_page, locale=locale, sort_by=sort_by)

Get Category

### Example


```python
import openapi_client
from openapi_client.models.main_category import MainCategory
from openapi_client.models.meilisearch_response_apps_index import MeilisearchResponseAppsIndex
from openapi_client.models.sort_by import SortBy
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
    api_instance = openapi_client.CollectionApi(api_client)
    category = openapi_client.MainCategory() # MainCategory | 
    exclude_subcategories = ['exclude_subcategories_example'] # List[Optional[str]] |  (optional)
    page = 56 # int |  (optional)
    per_page = 56 # int |  (optional)
    locale = 'en' # str |  (optional) (default to 'en')
    sort_by = openapi_client.SortBy() # SortBy |  (optional)

    try:
        # Get Category
        api_response = api_instance.get_category_collection_category_category_get(category, exclude_subcategories=exclude_subcategories, page=page, per_page=per_page, locale=locale, sort_by=sort_by)
        print("The response of CollectionApi->get_category_collection_category_category_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionApi->get_category_collection_category_category_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | [**MainCategory**](.md)|  | 
 **exclude_subcategories** | [**List[Optional[str]]**](str.md)|  | [optional] 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **locale** | **str**|  | [optional] [default to &#39;en&#39;]
 **sort_by** | [**SortBy**](.md)|  | [optional] 

### Return type

[**MeilisearchResponseAppsIndex**](MeilisearchResponseAppsIndex.md)

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

# **get_developer_collection_developer_developer_get**
> MeilisearchResponseAppsIndex get_developer_collection_developer_developer_get(developer, page=page, per_page=per_page, locale=locale)

Get Developer

### Example


```python
import openapi_client
from openapi_client.models.meilisearch_response_apps_index import MeilisearchResponseAppsIndex
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
    api_instance = openapi_client.CollectionApi(api_client)
    developer = 'developer_example' # str | 
    page = 56 # int |  (optional)
    per_page = 56 # int |  (optional)
    locale = 'en' # str |  (optional) (default to 'en')

    try:
        # Get Developer
        api_response = api_instance.get_developer_collection_developer_developer_get(developer, page=page, per_page=per_page, locale=locale)
        print("The response of CollectionApi->get_developer_collection_developer_developer_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionApi->get_developer_collection_developer_developer_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **developer** | **str**|  | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **locale** | **str**|  | [optional] [default to &#39;en&#39;]

### Return type

[**MeilisearchResponseAppsIndex**](MeilisearchResponseAppsIndex.md)

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

# **get_developers_collection_developer_get**
> AppSearchDevelopersResponse get_developers_collection_developer_get(page=page, per_page=per_page)

Get Developers

### Example


```python
import openapi_client
from openapi_client.models.app_search_developers_response import AppSearchDevelopersResponse
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
    api_instance = openapi_client.CollectionApi(api_client)
    page = 56 # int |  (optional)
    per_page = 56 # int |  (optional)

    try:
        # Get Developers
        api_response = api_instance.get_developers_collection_developer_get(page=page, per_page=per_page)
        print("The response of CollectionApi->get_developers_collection_developer_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionApi->get_developers_collection_developer_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**AppSearchDevelopersResponse**](AppSearchDevelopersResponse.md)

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

# **get_keyword_collection_keyword_get**
> MeilisearchResponseAppsIndex get_keyword_collection_keyword_get(keyword, page=page, per_page=per_page, locale=locale)

Get Keyword

### Example


```python
import openapi_client
from openapi_client.models.meilisearch_response_apps_index import MeilisearchResponseAppsIndex
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
    api_instance = openapi_client.CollectionApi(api_client)
    keyword = 'keyword_example' # str | 
    page = 56 # int |  (optional)
    per_page = 56 # int |  (optional)
    locale = 'en' # str |  (optional) (default to 'en')

    try:
        # Get Keyword
        api_response = api_instance.get_keyword_collection_keyword_get(keyword, page=page, per_page=per_page, locale=locale)
        print("The response of CollectionApi->get_keyword_collection_keyword_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionApi->get_keyword_collection_keyword_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyword** | **str**|  | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **locale** | **str**|  | [optional] [default to &#39;en&#39;]

### Return type

[**MeilisearchResponseAppsIndex**](MeilisearchResponseAppsIndex.md)

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

# **get_mobile_collection_mobile_get**
> MeilisearchResponseAppsIndex get_mobile_collection_mobile_get(page=page, per_page=per_page, locale=locale)

Get Mobile

### Example


```python
import openapi_client
from openapi_client.models.meilisearch_response_apps_index import MeilisearchResponseAppsIndex
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
    api_instance = openapi_client.CollectionApi(api_client)
    page = 56 # int |  (optional)
    per_page = 56 # int |  (optional)
    locale = 'en' # str |  (optional) (default to 'en')

    try:
        # Get Mobile
        api_response = api_instance.get_mobile_collection_mobile_get(page=page, per_page=per_page, locale=locale)
        print("The response of CollectionApi->get_mobile_collection_mobile_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionApi->get_mobile_collection_mobile_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **locale** | **str**|  | [optional] [default to &#39;en&#39;]

### Return type

[**MeilisearchResponseAppsIndex**](MeilisearchResponseAppsIndex.md)

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

# **get_popular_last_month_collection_popular_get**
> MeilisearchResponseAppsIndex get_popular_last_month_collection_popular_get(page=page, per_page=per_page, locale=locale)

Get Popular Last Month

### Example


```python
import openapi_client
from openapi_client.models.meilisearch_response_apps_index import MeilisearchResponseAppsIndex
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
    api_instance = openapi_client.CollectionApi(api_client)
    page = 56 # int |  (optional)
    per_page = 56 # int |  (optional)
    locale = 'en' # str |  (optional) (default to 'en')

    try:
        # Get Popular Last Month
        api_response = api_instance.get_popular_last_month_collection_popular_get(page=page, per_page=per_page, locale=locale)
        print("The response of CollectionApi->get_popular_last_month_collection_popular_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionApi->get_popular_last_month_collection_popular_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **locale** | **str**|  | [optional] [default to &#39;en&#39;]

### Return type

[**MeilisearchResponseAppsIndex**](MeilisearchResponseAppsIndex.md)

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

# **get_recently_added_collection_recently_added_get**
> MeilisearchResponseAppsIndex get_recently_added_collection_recently_added_get(page=page, per_page=per_page, locale=locale)

Get Recently Added

### Example


```python
import openapi_client
from openapi_client.models.meilisearch_response_apps_index import MeilisearchResponseAppsIndex
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
    api_instance = openapi_client.CollectionApi(api_client)
    page = 56 # int |  (optional)
    per_page = 56 # int |  (optional)
    locale = 'en' # str |  (optional) (default to 'en')

    try:
        # Get Recently Added
        api_response = api_instance.get_recently_added_collection_recently_added_get(page=page, per_page=per_page, locale=locale)
        print("The response of CollectionApi->get_recently_added_collection_recently_added_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionApi->get_recently_added_collection_recently_added_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **locale** | **str**|  | [optional] [default to &#39;en&#39;]

### Return type

[**MeilisearchResponseAppsIndex**](MeilisearchResponseAppsIndex.md)

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

# **get_recently_updated_collection_recently_updated_get**
> MeilisearchResponseAppsIndex get_recently_updated_collection_recently_updated_get(page=page, per_page=per_page, locale=locale)

Get Recently Updated

### Example


```python
import openapi_client
from openapi_client.models.meilisearch_response_apps_index import MeilisearchResponseAppsIndex
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
    api_instance = openapi_client.CollectionApi(api_client)
    page = 56 # int |  (optional)
    per_page = 56 # int |  (optional)
    locale = 'en' # str |  (optional) (default to 'en')

    try:
        # Get Recently Updated
        api_response = api_instance.get_recently_updated_collection_recently_updated_get(page=page, per_page=per_page, locale=locale)
        print("The response of CollectionApi->get_recently_updated_collection_recently_updated_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionApi->get_recently_updated_collection_recently_updated_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **locale** | **str**|  | [optional] [default to &#39;en&#39;]

### Return type

[**MeilisearchResponseAppsIndex**](MeilisearchResponseAppsIndex.md)

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

# **get_subcategory_collection_category_category_subcategories_get**
> MeilisearchResponseAppsIndex get_subcategory_collection_category_category_subcategories_get(category, subcategory, exclude_subcategories=exclude_subcategories, page=page, per_page=per_page, locale=locale, sort_by=sort_by)

Get Subcategory

### Example


```python
import openapi_client
from openapi_client.models.main_category import MainCategory
from openapi_client.models.meilisearch_response_apps_index import MeilisearchResponseAppsIndex
from openapi_client.models.sort_by import SortBy
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
    api_instance = openapi_client.CollectionApi(api_client)
    category = openapi_client.MainCategory() # MainCategory | 
    subcategory = ['subcategory_example'] # List[Optional[str]] | 
    exclude_subcategories = ['exclude_subcategories_example'] # List[str] |  (optional)
    page = 56 # int |  (optional)
    per_page = 56 # int |  (optional)
    locale = 'en' # str |  (optional) (default to 'en')
    sort_by = openapi_client.SortBy() # SortBy |  (optional)

    try:
        # Get Subcategory
        api_response = api_instance.get_subcategory_collection_category_category_subcategories_get(category, subcategory, exclude_subcategories=exclude_subcategories, page=page, per_page=per_page, locale=locale, sort_by=sort_by)
        print("The response of CollectionApi->get_subcategory_collection_category_category_subcategories_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionApi->get_subcategory_collection_category_category_subcategories_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | [**MainCategory**](.md)|  | 
 **subcategory** | [**List[Optional[str]]**](str.md)|  | 
 **exclude_subcategories** | [**List[str]**](str.md)|  | [optional] 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **locale** | **str**|  | [optional] [default to &#39;en&#39;]
 **sort_by** | [**SortBy**](.md)|  | [optional] 

### Return type

[**MeilisearchResponseAppsIndex**](MeilisearchResponseAppsIndex.md)

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

# **get_trending_last_two_weeks_collection_trending_get**
> MeilisearchResponseAppsIndex get_trending_last_two_weeks_collection_trending_get(page=page, per_page=per_page, locale=locale)

Get Trending Last Two Weeks

### Example


```python
import openapi_client
from openapi_client.models.meilisearch_response_apps_index import MeilisearchResponseAppsIndex
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
    api_instance = openapi_client.CollectionApi(api_client)
    page = 56 # int |  (optional)
    per_page = 56 # int |  (optional)
    locale = 'en' # str |  (optional) (default to 'en')

    try:
        # Get Trending Last Two Weeks
        api_response = api_instance.get_trending_last_two_weeks_collection_trending_get(page=page, per_page=per_page, locale=locale)
        print("The response of CollectionApi->get_trending_last_two_weeks_collection_trending_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionApi->get_trending_last_two_weeks_collection_trending_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **locale** | **str**|  | [optional] [default to &#39;en&#39;]

### Return type

[**MeilisearchResponseAppsIndex**](MeilisearchResponseAppsIndex.md)

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

# **get_verified_collection_verified_get**
> MeilisearchResponseAppsIndex get_verified_collection_verified_get(page=page, per_page=per_page, locale=locale)

Get Verified

### Example


```python
import openapi_client
from openapi_client.models.meilisearch_response_apps_index import MeilisearchResponseAppsIndex
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
    api_instance = openapi_client.CollectionApi(api_client)
    page = 56 # int |  (optional)
    per_page = 56 # int |  (optional)
    locale = 'en' # str |  (optional) (default to 'en')

    try:
        # Get Verified
        api_response = api_instance.get_verified_collection_verified_get(page=page, per_page=per_page, locale=locale)
        print("The response of CollectionApi->get_verified_collection_verified_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionApi->get_verified_collection_verified_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **locale** | **str**|  | [optional] [default to &#39;en&#39;]

### Return type

[**MeilisearchResponseAppsIndex**](MeilisearchResponseAppsIndex.md)

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

