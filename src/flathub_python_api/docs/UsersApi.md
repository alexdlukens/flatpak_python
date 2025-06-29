# flathub_python_api.UsersApi

All URIs are relative to *https://flathub.org/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user_role_users_user_id_role_post**](UsersApi.md#add_user_role_users_user_id_role_post) | **POST** /users/{user_id}/role | Add User Role
[**delete_user_role_users_user_id_role_delete**](UsersApi.md#delete_user_role_users_user_id_role_delete) | **DELETE** /users/{user_id}/role | Delete User Role
[**role_users_users_roles_role_name_get**](UsersApi.md#role_users_users_roles_role_name_get) | **GET** /users/roles/{role_name} | Role Users
[**roles_users_roles_get**](UsersApi.md#roles_users_roles_get) | **GET** /users/roles | Roles
[**user_users_user_id_get**](UsersApi.md#user_users_user_id_get) | **GET** /users/{user_id} | User
[**users_users_get**](UsersApi.md#users_users_get) | **GET** /users | Users


# **add_user_role_users_user_id_role_post**
> UserResult add_user_role_users_user_id_role_post(user_id, role)

Add User Role

Add a role to a user

### Example


```python
import flathub_python_api
from flathub_python_api.models.role_name import RoleName
from flathub_python_api.models.user_result import UserResult
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
    api_instance = flathub_python_api.UsersApi(api_client)
    user_id = 56 # int | 
    role = flathub_python_api.RoleName() # RoleName | 

    try:
        # Add User Role
        api_response = api_instance.add_user_role_users_user_id_role_post(user_id, role)
        print("The response of UsersApi->add_user_role_users_user_id_role_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->add_user_role_users_user_id_role_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **role** | [**RoleName**](.md)|  | 

### Return type

[**UserResult**](UserResult.md)

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

# **delete_user_role_users_user_id_role_delete**
> UserResult delete_user_role_users_user_id_role_delete(user_id, role)

Delete User Role

Remove a role from a user

### Example


```python
import flathub_python_api
from flathub_python_api.models.role_name import RoleName
from flathub_python_api.models.user_result import UserResult
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
    api_instance = flathub_python_api.UsersApi(api_client)
    user_id = 56 # int | 
    role = flathub_python_api.RoleName() # RoleName | 

    try:
        # Delete User Role
        api_response = api_instance.delete_user_role_users_user_id_role_delete(user_id, role)
        print("The response of UsersApi->delete_user_role_users_user_id_role_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->delete_user_role_users_user_id_role_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **role** | [**RoleName**](.md)|  | 

### Return type

[**UserResult**](UserResult.md)

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

# **role_users_users_roles_role_name_get**
> List[UserResult] role_users_users_roles_role_name_get(role_name)

Role Users

Return all users with a specific role

### Example


```python
import flathub_python_api
from flathub_python_api.models.role_name import RoleName
from flathub_python_api.models.user_result import UserResult
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
    api_instance = flathub_python_api.UsersApi(api_client)
    role_name = flathub_python_api.RoleName() # RoleName | 

    try:
        # Role Users
        api_response = api_instance.role_users_users_roles_role_name_get(role_name)
        print("The response of UsersApi->role_users_users_roles_role_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->role_users_users_roles_role_name_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | [**RoleName**](.md)|  | 

### Return type

[**List[UserResult]**](UserResult.md)

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

# **roles_users_roles_get**
> List[Optional[str]] roles_users_roles_get()

Roles

Return a list of all known role names

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
    api_instance = flathub_python_api.UsersApi(api_client)

    try:
        # Roles
        api_response = api_instance.roles_users_roles_get()
        print("The response of UsersApi->roles_users_roles_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->roles_users_roles_get: %s\n" % e)
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

# **user_users_user_id_get**
> UserResult user_users_user_id_get(user_id)

User

Return the current user

### Example


```python
import flathub_python_api
from flathub_python_api.models.user_result import UserResult
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
    api_instance = flathub_python_api.UsersApi(api_client)
    user_id = 56 # int | 

    try:
        # User
        api_response = api_instance.user_users_user_id_get(user_id)
        print("The response of UsersApi->user_users_user_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->user_users_user_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

[**UserResult**](UserResult.md)

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

# **users_users_get**
> FlathubUsersResult users_users_get(page=page, page_size=page_size, filter_string=filter_string)

Users

Return a list of all known users

### Example


```python
import flathub_python_api
from flathub_python_api.models.flathub_users_result import FlathubUsersResult
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
    api_instance = flathub_python_api.UsersApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    page_size = 30 # int |  (optional) (default to 30)
    filter_string = 'filter_string_example' # str |  (optional)

    try:
        # Users
        api_response = api_instance.users_users_get(page=page, page_size=page_size, filter_string=filter_string)
        print("The response of UsersApi->users_users_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_users_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 30]
 **filter_string** | **str**|  | [optional] 

### Return type

[**FlathubUsersResult**](FlathubUsersResult.md)

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

