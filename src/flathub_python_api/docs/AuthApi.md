# flathub_python_api.AuthApi

All URIs are relative to *https://flathub.org/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**continue_github_flow_auth_login_github_post**](AuthApi.md#continue_github_flow_auth_login_github_post) | **POST** /auth/login/github | Continue Github Flow
[**continue_gitlab_flow_auth_login_gitlab_post**](AuthApi.md#continue_gitlab_flow_auth_login_gitlab_post) | **POST** /auth/login/gitlab | Continue Gitlab Flow
[**continue_gnome_flow_auth_login_gnome_post**](AuthApi.md#continue_gnome_flow_auth_login_gnome_post) | **POST** /auth/login/gnome | Continue Gnome Flow
[**continue_google_flow_auth_login_google_post**](AuthApi.md#continue_google_flow_auth_login_google_post) | **POST** /auth/login/google | Continue Google Flow
[**continue_kde_flow_auth_login_kde_post**](AuthApi.md#continue_kde_flow_auth_login_kde_post) | **POST** /auth/login/kde | Continue Kde Flow
[**do_agree_to_publisher_agreement_auth_accept_publisher_agreement_post**](AuthApi.md#do_agree_to_publisher_agreement_auth_accept_publisher_agreement_post) | **POST** /auth/accept-publisher-agreement | Do Agree To Publisher Agreement
[**do_change_default_account_auth_change_default_account_post**](AuthApi.md#do_change_default_account_auth_change_default_account_post) | **POST** /auth/change-default-account | Do Change Default Account
[**do_deleteuser_auth_deleteuser_post**](AuthApi.md#do_deleteuser_auth_deleteuser_post) | **POST** /auth/deleteuser | Do Deleteuser
[**do_logout_auth_logout_post**](AuthApi.md#do_logout_auth_logout_post) | **POST** /auth/logout | Do Logout
[**do_refresh_dev_flatpaks_auth_refresh_dev_flatpaks_post**](AuthApi.md#do_refresh_dev_flatpaks_auth_refresh_dev_flatpaks_post) | **POST** /auth/refresh-dev-flatpaks | Do Refresh Dev Flatpaks
[**get_deleteuser_auth_deleteuser_get**](AuthApi.md#get_deleteuser_auth_deleteuser_get) | **GET** /auth/deleteuser | Get Deleteuser
[**get_login_methods_auth_login_get**](AuthApi.md#get_login_methods_auth_login_get) | **GET** /auth/login | Get Login Methods
[**get_userinfo_auth_userinfo_get**](AuthApi.md#get_userinfo_auth_userinfo_get) | **GET** /auth/userinfo | Get Userinfo
[**start_github_flow_auth_login_github_get**](AuthApi.md#start_github_flow_auth_login_github_get) | **GET** /auth/login/github | Start Github Flow
[**start_gitlab_flow_auth_login_gitlab_get**](AuthApi.md#start_gitlab_flow_auth_login_gitlab_get) | **GET** /auth/login/gitlab | Start Gitlab Flow
[**start_gnome_flow_auth_login_gnome_get**](AuthApi.md#start_gnome_flow_auth_login_gnome_get) | **GET** /auth/login/gnome | Start Gnome Flow
[**start_kde_flow_auth_login_kde_get**](AuthApi.md#start_kde_flow_auth_login_kde_get) | **GET** /auth/login/kde | Start Kde Flow


# **continue_github_flow_auth_login_github_post**
> object continue_github_flow_auth_login_github_post(data)

Continue Github Flow

Process the result of the Github oauth flow

This expects to have some JSON posted to it which (on success) contains:

```
{
    "state": "the state code",
    "code": "the github oauth code",
}
```

On failure, the frontend should pass through the state and error so that
the backend can clear the flow tokens

```
{
    "state": "the state code",
    "error": "the error code returned from github",
}
```

This endpoint will either return an error, if something was wrong in the
backend state machines; or it will return a success code with an indication
of whether or not the login sequence completed OK.

### Example


```python
import flathub_python_api
from flathub_python_api.models.data import Data
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
    api_instance = flathub_python_api.AuthApi(api_client)
    data = flathub_python_api.Data() # Data | 

    try:
        # Continue Github Flow
        api_response = api_instance.continue_github_flow_auth_login_github_post(data)
        print("The response of AuthApi->continue_github_flow_auth_login_github_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->continue_github_flow_auth_login_github_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data**](Data.md)|  | 

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

# **continue_gitlab_flow_auth_login_gitlab_post**
> object continue_gitlab_flow_auth_login_gitlab_post(data)

Continue Gitlab Flow

Process the result of the Gitlab oauth flow

This expects to have some JSON posted to it which (on success) contains:

```
{
    "state": "the state code",
    "code": "the gitlab oauth code",
}
```

On failure, the frontend should pass through the state and error so that
the backend can clear the flow tokens

```
{
    "state": "the state code",
    "error": "the error code returned from gitlab",
}
```

This endpoint will either return an error, if something was wrong in the
backend state machines; or it will return a success code with an indication
of whether or not the login sequence completed OK.

### Example


```python
import flathub_python_api
from flathub_python_api.models.data import Data
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
    api_instance = flathub_python_api.AuthApi(api_client)
    data = flathub_python_api.Data() # Data | 

    try:
        # Continue Gitlab Flow
        api_response = api_instance.continue_gitlab_flow_auth_login_gitlab_post(data)
        print("The response of AuthApi->continue_gitlab_flow_auth_login_gitlab_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->continue_gitlab_flow_auth_login_gitlab_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data**](Data.md)|  | 

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

# **continue_gnome_flow_auth_login_gnome_post**
> object continue_gnome_flow_auth_login_gnome_post(data)

Continue Gnome Flow

Process the result of the GNOME oauth flow

This expects to have some JSON posted to it which (on success) contains:

```
{
    "state": "the state code",
    "code": "the gitlab oauth code",
}
```

On failure, the frontend should pass through the state and error so that
the backend can clear the flow tokens

```
{
    "state": "the state code",
    "error": "the error code returned from GNOME gitlab",
}
```

This endpoint will either return an error, if something was wrong in the
backend state machines; or it will return a success code with an indication
of whether or not the login sequence completed OK.

### Example


```python
import flathub_python_api
from flathub_python_api.models.data import Data
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
    api_instance = flathub_python_api.AuthApi(api_client)
    data = flathub_python_api.Data() # Data | 

    try:
        # Continue Gnome Flow
        api_response = api_instance.continue_gnome_flow_auth_login_gnome_post(data)
        print("The response of AuthApi->continue_gnome_flow_auth_login_gnome_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->continue_gnome_flow_auth_login_gnome_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data**](Data.md)|  | 

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

# **continue_google_flow_auth_login_google_post**
> object continue_google_flow_auth_login_google_post(data)

Continue Google Flow

Process the result of the Google oauth flow

This expects to have some JSON posted to it which (on success) contains:

```
{
    "state": "the state code",
    "code": "the google oauth code",
}
```

On failure, the frontend should pass through the state and error so that
the backend can clear the flow tokens

```
{
    "state": "the state code",
    "error": "the error code returned from google",
}
```

This endpoint will either return an error, if something was wrong in the
backend state machines; or it will return a success code with an indication
of whether or not the login sequence completed OK.

### Example


```python
import flathub_python_api
from flathub_python_api.models.data import Data
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
    api_instance = flathub_python_api.AuthApi(api_client)
    data = flathub_python_api.Data() # Data | 

    try:
        # Continue Google Flow
        api_response = api_instance.continue_google_flow_auth_login_google_post(data)
        print("The response of AuthApi->continue_google_flow_auth_login_google_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->continue_google_flow_auth_login_google_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data**](Data.md)|  | 

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

# **continue_kde_flow_auth_login_kde_post**
> object continue_kde_flow_auth_login_kde_post(data)

Continue Kde Flow

### Example


```python
import flathub_python_api
from flathub_python_api.models.data import Data
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
    api_instance = flathub_python_api.AuthApi(api_client)
    data = flathub_python_api.Data() # Data | 

    try:
        # Continue Kde Flow
        api_response = api_instance.continue_kde_flow_auth_login_kde_post(data)
        print("The response of AuthApi->continue_kde_flow_auth_login_kde_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->continue_kde_flow_auth_login_kde_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data**](Data.md)|  | 

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

# **do_agree_to_publisher_agreement_auth_accept_publisher_agreement_post**
> object do_agree_to_publisher_agreement_auth_accept_publisher_agreement_post()

Do Agree To Publisher Agreement

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
    api_instance = flathub_python_api.AuthApi(api_client)

    try:
        # Do Agree To Publisher Agreement
        api_response = api_instance.do_agree_to_publisher_agreement_auth_accept_publisher_agreement_post()
        print("The response of AuthApi->do_agree_to_publisher_agreement_auth_accept_publisher_agreement_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->do_agree_to_publisher_agreement_auth_accept_publisher_agreement_post: %s\n" % e)
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

# **do_change_default_account_auth_change_default_account_post**
> do_change_default_account_auth_change_default_account_post(provider)

Do Change Default Account

Changes the user's default account, which determines which display name and email we use.

### Example


```python
import flathub_python_api
from flathub_python_api.models.connected_account_provider import ConnectedAccountProvider
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
    api_instance = flathub_python_api.AuthApi(api_client)
    provider = flathub_python_api.ConnectedAccountProvider() # ConnectedAccountProvider | 

    try:
        # Do Change Default Account
        api_instance.do_change_default_account_auth_change_default_account_post(provider)
    except Exception as e:
        print("Exception when calling AuthApi->do_change_default_account_auth_change_default_account_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | [**ConnectedAccountProvider**](.md)|  | 

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

# **do_deleteuser_auth_deleteuser_post**
> DeleteUserResult do_deleteuser_auth_deleteuser_post(user_delete_request)

Do Deleteuser

Clear the login state. This will then delete the user's account
and associated data. Unless there is an error.

The input to this should be of the form:

```json
{
    "token": "...",
}
```

### Example


```python
import flathub_python_api
from flathub_python_api.models.delete_user_result import DeleteUserResult
from flathub_python_api.models.user_delete_request import UserDeleteRequest
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
    api_instance = flathub_python_api.AuthApi(api_client)
    user_delete_request = flathub_python_api.UserDeleteRequest() # UserDeleteRequest | 

    try:
        # Do Deleteuser
        api_response = api_instance.do_deleteuser_auth_deleteuser_post(user_delete_request)
        print("The response of AuthApi->do_deleteuser_auth_deleteuser_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->do_deleteuser_auth_deleteuser_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_delete_request** | [**UserDeleteRequest**](UserDeleteRequest.md)|  | 

### Return type

[**DeleteUserResult**](DeleteUserResult.md)

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

# **do_logout_auth_logout_post**
> object do_logout_auth_logout_post()

Do Logout

Clear the login state. This will discard tokens which access socials,
and will clear the session cookie so that the user is not logged in.

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
    api_instance = flathub_python_api.AuthApi(api_client)

    try:
        # Do Logout
        api_response = api_instance.do_logout_auth_logout_post()
        print("The response of AuthApi->do_logout_auth_logout_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->do_logout_auth_logout_post: %s\n" % e)
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

# **do_refresh_dev_flatpaks_auth_refresh_dev_flatpaks_post**
> RefreshDevFlatpaksReturn do_refresh_dev_flatpaks_auth_refresh_dev_flatpaks_post()

Do Refresh Dev Flatpaks

### Example


```python
import flathub_python_api
from flathub_python_api.models.refresh_dev_flatpaks_return import RefreshDevFlatpaksReturn
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
    api_instance = flathub_python_api.AuthApi(api_client)

    try:
        # Do Refresh Dev Flatpaks
        api_response = api_instance.do_refresh_dev_flatpaks_auth_refresh_dev_flatpaks_post()
        print("The response of AuthApi->do_refresh_dev_flatpaks_auth_refresh_dev_flatpaks_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->do_refresh_dev_flatpaks_auth_refresh_dev_flatpaks_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**RefreshDevFlatpaksReturn**](RefreshDevFlatpaksReturn.md)

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

# **get_deleteuser_auth_deleteuser_get**
> GetDeleteUserResult get_deleteuser_auth_deleteuser_get()

Get Deleteuser

Delete a user's login information.
If they're not logged in, they'll get a `403` return.
Otherwise they will get an option to delete their account
and data.

### Example


```python
import flathub_python_api
from flathub_python_api.models.get_delete_user_result import GetDeleteUserResult
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
    api_instance = flathub_python_api.AuthApi(api_client)

    try:
        # Get Deleteuser
        api_response = api_instance.get_deleteuser_auth_deleteuser_get()
        print("The response of AuthApi->get_deleteuser_auth_deleteuser_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->get_deleteuser_auth_deleteuser_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetDeleteUserResult**](GetDeleteUserResult.md)

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

# **get_login_methods_auth_login_get**
> List[LoginMethod] get_login_methods_auth_login_get()

Get Login Methods

Retrieve the login methods available from the backend.

For each method returned, flow starts with a `GET` to the endpoint
`.../login/{method}` and upon completion from the user-agent, with a `POST`
to that same endpoint name.

Each method is also given a button icon and some text to use, though
frontends with localisation may choose to render other text instead.

### Example


```python
import flathub_python_api
from flathub_python_api.models.login_method import LoginMethod
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
    api_instance = flathub_python_api.AuthApi(api_client)

    try:
        # Get Login Methods
        api_response = api_instance.get_login_methods_auth_login_get()
        print("The response of AuthApi->get_login_methods_auth_login_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->get_login_methods_auth_login_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[LoginMethod]**](LoginMethod.md)

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

# **get_userinfo_auth_userinfo_get**
> UserInfo get_userinfo_auth_userinfo_get()

Get Userinfo

Retrieve the current login's user information.  If the user is not logged in
you will get a `204` return.  Otherwise you will receive JSON describing the
currently logged in user, for example:

```
{
    "displayname": "Mx Human Person",
    "dev_flatpaks": [ "org.people.human.Appname" ],
    "owned_flatpaks": [ "org.foo.bar.Appname" ],
    "accepted_publisher-agreement_at": "2023-06-23T20:38:28.553028"
}
```

If the user has an active github login, you'll also get their github login
name, and avatar.  If they have some other login, details for that login
will be provided.

dev_flatpaks is filtered against IDs available in AppStream

### Example


```python
import flathub_python_api
from flathub_python_api.models.user_info import UserInfo
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
    api_instance = flathub_python_api.AuthApi(api_client)

    try:
        # Get Userinfo
        api_response = api_instance.get_userinfo_auth_userinfo_get()
        print("The response of AuthApi->get_userinfo_auth_userinfo_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->get_userinfo_auth_userinfo_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserInfo**](UserInfo.md)

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

# **start_github_flow_auth_login_github_get**
> object start_github_flow_auth_login_github_get()

Start Github Flow

Starts a github login flow.  This will set session cookie values and
will return a redirect.  The frontend is expected to save the cookie
for use later, and follow the redirect to Github

Upon return from Github to the frontend, the frontend should POST to this
endpoint with the relevant data from Github

If the user is already logged in, and has a valid github token stored,
then this will return an error instead.

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
    api_instance = flathub_python_api.AuthApi(api_client)

    try:
        # Start Github Flow
        api_response = api_instance.start_github_flow_auth_login_github_get()
        print("The response of AuthApi->start_github_flow_auth_login_github_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->start_github_flow_auth_login_github_get: %s\n" % e)
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

# **start_gitlab_flow_auth_login_gitlab_get**
> object start_gitlab_flow_auth_login_gitlab_get()

Start Gitlab Flow

Starts a gitlab login flow.  This will set session cookie values and
will return a redirect.  The frontend is expected to save the cookie
for use later, and follow the redirect to Gitlab

Upon return from Gitlab to the frontend, the frontend should POST to this
endpoint with the relevant data from Gitlab

If the user is already logged in, and has a valid gitlab token stored,
then this will return an error instead.

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
    api_instance = flathub_python_api.AuthApi(api_client)

    try:
        # Start Gitlab Flow
        api_response = api_instance.start_gitlab_flow_auth_login_gitlab_get()
        print("The response of AuthApi->start_gitlab_flow_auth_login_gitlab_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->start_gitlab_flow_auth_login_gitlab_get: %s\n" % e)
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

# **start_gnome_flow_auth_login_gnome_get**
> object start_gnome_flow_auth_login_gnome_get()

Start Gnome Flow

Starts a GNOME login flow.  This will set session cookie values and
will return a redirect.  The frontend is expected to save the cookie
for use later, and follow the redirect to GNOME Gitlab

Upon return from GNOME to the frontend, the frontend should POST to this
endpoint with the relevant data from GNOME Gitlab

If the user is already logged in, and has a valid GNOME Gitlab token stored,
then this will return an error instead.

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
    api_instance = flathub_python_api.AuthApi(api_client)

    try:
        # Start Gnome Flow
        api_response = api_instance.start_gnome_flow_auth_login_gnome_get()
        print("The response of AuthApi->start_gnome_flow_auth_login_gnome_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->start_gnome_flow_auth_login_gnome_get: %s\n" % e)
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

# **start_kde_flow_auth_login_kde_get**
> object start_kde_flow_auth_login_kde_get()

Start Kde Flow

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
    api_instance = flathub_python_api.AuthApi(api_client)

    try:
        # Start Kde Flow
        api_response = api_instance.start_kde_flow_auth_login_kde_get()
        print("The response of AuthApi->start_kde_flow_auth_login_kde_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->start_kde_flow_auth_login_kde_get: %s\n" % e)
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

