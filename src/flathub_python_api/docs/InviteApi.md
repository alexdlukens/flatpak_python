# flathub_python_api.InviteApi

All URIs are relative to *https://flathub.org/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_invite_invites_app_id_accept_post**](InviteApi.md#accept_invite_invites_app_id_accept_post) | **POST** /invites/{app_id}/accept | Accept Invite
[**decline_invite_invites_app_id_decline_post**](InviteApi.md#decline_invite_invites_app_id_decline_post) | **POST** /invites/{app_id}/decline | Decline Invite
[**get_app_developers_invites_app_id_developers_get**](InviteApi.md#get_app_developers_invites_app_id_developers_get) | **GET** /invites/{app_id}/developers | Get App Developers
[**get_invite_status_invites_app_id_get**](InviteApi.md#get_invite_status_invites_app_id_get) | **GET** /invites/{app_id} | Get Invite Status
[**invite_developer_invites_app_id_invite_post**](InviteApi.md#invite_developer_invites_app_id_invite_post) | **POST** /invites/{app_id}/invite | Invite Developer
[**leave_team_invites_app_id_leave_post**](InviteApi.md#leave_team_invites_app_id_leave_post) | **POST** /invites/{app_id}/leave | Leave Team
[**remove_developer_invites_app_id_remove_developer_post**](InviteApi.md#remove_developer_invites_app_id_remove_developer_post) | **POST** /invites/{app_id}/remove-developer | Remove Developer
[**revoke_invite_invites_app_id_revoke_post**](InviteApi.md#revoke_invite_invites_app_id_revoke_post) | **POST** /invites/{app_id}/revoke | Revoke Invite


# **accept_invite_invites_app_id_accept_post**
> accept_invite_invites_app_id_accept_post(app_id)

Accept Invite

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
    api_instance = flathub_python_api.InviteApi(api_client)
    app_id = 'app_id_example' # str | 

    try:
        # Accept Invite
        api_instance.accept_invite_invites_app_id_accept_post(app_id)
    except Exception as e:
        print("Exception when calling InviteApi->accept_invite_invites_app_id_accept_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **decline_invite_invites_app_id_decline_post**
> decline_invite_invites_app_id_decline_post(app_id)

Decline Invite

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
    api_instance = flathub_python_api.InviteApi(api_client)
    app_id = 'app_id_example' # str | 

    try:
        # Decline Invite
        api_instance.decline_invite_invites_app_id_decline_post(app_id)
    except Exception as e:
        print("Exception when calling InviteApi->decline_invite_invites_app_id_decline_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_developers_invites_app_id_developers_get**
> AppRoutesInvitesDevelopersResponse get_app_developers_invites_app_id_developers_get(app_id)

Get App Developers

### Example


```python
import flathub_python_api
from flathub_python_api.models.app_routes_invites_developers_response import AppRoutesInvitesDevelopersResponse
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
    api_instance = flathub_python_api.InviteApi(api_client)
    app_id = 'app_id_example' # str | 

    try:
        # Get App Developers
        api_response = api_instance.get_app_developers_invites_app_id_developers_get(app_id)
        print("The response of InviteApi->get_app_developers_invites_app_id_developers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InviteApi->get_app_developers_invites_app_id_developers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 

### Return type

[**AppRoutesInvitesDevelopersResponse**](AppRoutesInvitesDevelopersResponse.md)

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

# **get_invite_status_invites_app_id_get**
> InviteStatus get_invite_status_invites_app_id_get(app_id)

Get Invite Status

### Example


```python
import flathub_python_api
from flathub_python_api.models.invite_status import InviteStatus
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
    api_instance = flathub_python_api.InviteApi(api_client)
    app_id = 'app_id_example' # str | 

    try:
        # Get Invite Status
        api_response = api_instance.get_invite_status_invites_app_id_get(app_id)
        print("The response of InviteApi->get_invite_status_invites_app_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InviteApi->get_invite_status_invites_app_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 

### Return type

[**InviteStatus**](InviteStatus.md)

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

# **invite_developer_invites_app_id_invite_post**
> invite_developer_invites_app_id_invite_post(app_id, invite_code)

Invite Developer

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
    api_instance = flathub_python_api.InviteApi(api_client)
    app_id = 'app_id_example' # str | 
    invite_code = 'invite_code_example' # str | 

    try:
        # Invite Developer
        api_instance.invite_developer_invites_app_id_invite_post(app_id, invite_code)
    except Exception as e:
        print("Exception when calling InviteApi->invite_developer_invites_app_id_invite_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **invite_code** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leave_team_invites_app_id_leave_post**
> leave_team_invites_app_id_leave_post(app_id)

Leave Team

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
    api_instance = flathub_python_api.InviteApi(api_client)
    app_id = 'app_id_example' # str | 

    try:
        # Leave Team
        api_instance.leave_team_invites_app_id_leave_post(app_id)
    except Exception as e:
        print("Exception when calling InviteApi->leave_team_invites_app_id_leave_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_developer_invites_app_id_remove_developer_post**
> remove_developer_invites_app_id_remove_developer_post(app_id, developer_id)

Remove Developer

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
    api_instance = flathub_python_api.InviteApi(api_client)
    app_id = 'app_id_example' # str | 
    developer_id = 56 # int | 

    try:
        # Remove Developer
        api_instance.remove_developer_invites_app_id_remove_developer_post(app_id, developer_id)
    except Exception as e:
        print("Exception when calling InviteApi->remove_developer_invites_app_id_remove_developer_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **developer_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_invite_invites_app_id_revoke_post**
> revoke_invite_invites_app_id_revoke_post(app_id, invite_id)

Revoke Invite

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
    api_instance = flathub_python_api.InviteApi(api_client)
    app_id = 'app_id_example' # str | 
    invite_id = 56 # int | 

    try:
        # Revoke Invite
        api_instance.revoke_invite_invites_app_id_revoke_post(app_id, invite_id)
    except Exception as e:
        print("Exception when calling InviteApi->revoke_invite_invites_app_id_revoke_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **invite_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

