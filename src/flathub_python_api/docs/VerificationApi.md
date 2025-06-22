# openapi_client.VerificationApi

All URIs are relative to *https://flathub.org/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_verification_app_id_archive_post**](VerificationApi.md#archive_verification_app_id_archive_post) | **POST** /verification/{app_id}/archive | Archive
[**confirm_website_verification_verification_app_id_confirm_website_verification_post**](VerificationApi.md#confirm_website_verification_verification_app_id_confirm_website_verification_post) | **POST** /verification/{app_id}/confirm-website-verification | Confirm Website Verification
[**get_available_methods_verification_app_id_available_methods_get**](VerificationApi.md#get_available_methods_verification_app_id_available_methods_get) | **GET** /verification/{app_id}/available-methods | Get Available Methods
[**get_verification_status_verification_app_id_status_get**](VerificationApi.md#get_verification_status_verification_app_id_status_get) | **GET** /verification/{app_id}/status | Get Verification Status
[**request_organization_access_github_verification_request_organization_access_github_get**](VerificationApi.md#request_organization_access_github_verification_request_organization_access_github_get) | **GET** /verification/request-organization-access/github | Request Organization Access Github
[**setup_website_verification_verification_app_id_setup_website_verification_post**](VerificationApi.md#setup_website_verification_verification_app_id_setup_website_verification_post) | **POST** /verification/{app_id}/setup-website-verification | Setup Website Verification
[**switch_to_direct_upload_verification_app_id_switch_to_direct_upload_post**](VerificationApi.md#switch_to_direct_upload_verification_app_id_switch_to_direct_upload_post) | **POST** /verification/{app_id}/switch_to_direct_upload | Switch To Direct Upload
[**unverify_verification_app_id_unverify_post**](VerificationApi.md#unverify_verification_app_id_unverify_post) | **POST** /verification/{app_id}/unverify | Unverify
[**verify_by_login_provider_verification_app_id_verify_by_login_provider_post**](VerificationApi.md#verify_by_login_provider_verification_app_id_verify_by_login_provider_post) | **POST** /verification/{app_id}/verify-by-login-provider | Verify By Login Provider


# **archive_verification_app_id_archive_post**
> archive_verification_app_id_archive_post(app_id, archive_request)

Archive

### Example


```python
import openapi_client
from openapi_client.models.archive_request import ArchiveRequest
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
    api_instance = openapi_client.VerificationApi(api_client)
    app_id = 'app_id_example' # str | 
    archive_request = openapi_client.ArchiveRequest() # ArchiveRequest | 

    try:
        # Archive
        api_instance.archive_verification_app_id_archive_post(app_id, archive_request)
    except Exception as e:
        print("Exception when calling VerificationApi->archive_verification_app_id_archive_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **archive_request** | [**ArchiveRequest**](ArchiveRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confirm_website_verification_verification_app_id_confirm_website_verification_post**
> WebsiteVerificationResult confirm_website_verification_verification_app_id_confirm_website_verification_post(app_id, new_app=new_app)

Confirm Website Verification

Checks website verification, and if it succeeds, marks the app as verified for the current account.

### Example


```python
import openapi_client
from openapi_client.models.website_verification_result import WebsiteVerificationResult
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
    api_instance = openapi_client.VerificationApi(api_client)
    app_id = 'app_id_example' # str | 
    new_app = False # bool |  (optional) (default to False)

    try:
        # Confirm Website Verification
        api_response = api_instance.confirm_website_verification_verification_app_id_confirm_website_verification_post(app_id, new_app=new_app)
        print("The response of VerificationApi->confirm_website_verification_verification_app_id_confirm_website_verification_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VerificationApi->confirm_website_verification_verification_app_id_confirm_website_verification_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **new_app** | **bool**|  | [optional] [default to False]

### Return type

[**WebsiteVerificationResult**](WebsiteVerificationResult.md)

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

# **get_available_methods_verification_app_id_available_methods_get**
> AvailableMethods get_available_methods_verification_app_id_available_methods_get(app_id, new_app=new_app)

Get Available Methods

Gets the ways an app may be verified.

### Example


```python
import openapi_client
from openapi_client.models.available_methods import AvailableMethods
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
    api_instance = openapi_client.VerificationApi(api_client)
    app_id = 'app_id_example' # str | 
    new_app = False # bool |  (optional) (default to False)

    try:
        # Get Available Methods
        api_response = api_instance.get_available_methods_verification_app_id_available_methods_get(app_id, new_app=new_app)
        print("The response of VerificationApi->get_available_methods_verification_app_id_available_methods_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VerificationApi->get_available_methods_verification_app_id_available_methods_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **new_app** | **bool**|  | [optional] [default to False]

### Return type

[**AvailableMethods**](AvailableMethods.md)

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

# **get_verification_status_verification_app_id_status_get**
> VerificationStatus get_verification_status_verification_app_id_status_get(app_id)

Get Verification Status

Gets the verification status of the given app.

### Example


```python
import openapi_client
from openapi_client.models.verification_status import VerificationStatus
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
    api_instance = openapi_client.VerificationApi(api_client)
    app_id = 'app_id_example' # str | 

    try:
        # Get Verification Status
        api_response = api_instance.get_verification_status_verification_app_id_status_get(app_id)
        print("The response of VerificationApi->get_verification_status_verification_app_id_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VerificationApi->get_verification_status_verification_app_id_status_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 

### Return type

[**VerificationStatus**](VerificationStatus.md)

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

# **request_organization_access_github_verification_request_organization_access_github_get**
> LinkResponse request_organization_access_github_verification_request_organization_access_github_get()

Request Organization Access Github

Returns the URL to request access to the organization so we can verify the user's membership.

### Example


```python
import openapi_client
from openapi_client.models.link_response import LinkResponse
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
    api_instance = openapi_client.VerificationApi(api_client)

    try:
        # Request Organization Access Github
        api_response = api_instance.request_organization_access_github_verification_request_organization_access_github_get()
        print("The response of VerificationApi->request_organization_access_github_verification_request_organization_access_github_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VerificationApi->request_organization_access_github_verification_request_organization_access_github_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**LinkResponse**](LinkResponse.md)

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

# **setup_website_verification_verification_app_id_setup_website_verification_post**
> WebsiteVerificationToken setup_website_verification_verification_app_id_setup_website_verification_post(app_id, new_app=new_app)

Setup Website Verification

Creates a token for the user to verify the app via website.

### Example


```python
import openapi_client
from openapi_client.models.website_verification_token import WebsiteVerificationToken
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
    api_instance = openapi_client.VerificationApi(api_client)
    app_id = 'app_id_example' # str | 
    new_app = False # bool |  (optional) (default to False)

    try:
        # Setup Website Verification
        api_response = api_instance.setup_website_verification_verification_app_id_setup_website_verification_post(app_id, new_app=new_app)
        print("The response of VerificationApi->setup_website_verification_verification_app_id_setup_website_verification_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VerificationApi->setup_website_verification_verification_app_id_setup_website_verification_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **new_app** | **bool**|  | [optional] [default to False]

### Return type

[**WebsiteVerificationToken**](WebsiteVerificationToken.md)

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

# **switch_to_direct_upload_verification_app_id_switch_to_direct_upload_post**
> switch_to_direct_upload_verification_app_id_switch_to_direct_upload_post(app_id)

Switch To Direct Upload

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
    api_instance = openapi_client.VerificationApi(api_client)
    app_id = 'app_id_example' # str | 

    try:
        # Switch To Direct Upload
        api_instance.switch_to_direct_upload_verification_app_id_switch_to_direct_upload_post(app_id)
    except Exception as e:
        print("Exception when calling VerificationApi->switch_to_direct_upload_verification_app_id_switch_to_direct_upload_post: %s\n" % e)
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

# **unverify_verification_app_id_unverify_post**
> unverify_verification_app_id_unverify_post(app_id)

Unverify

If the current account has verified the given app, mark it as no longer verified.

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
    api_instance = openapi_client.VerificationApi(api_client)
    app_id = 'app_id_example' # str | 

    try:
        # Unverify
        api_instance.unverify_verification_app_id_unverify_post(app_id)
    except Exception as e:
        print("Exception when calling VerificationApi->unverify_verification_app_id_unverify_post: %s\n" % e)
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

# **verify_by_login_provider_verification_app_id_verify_by_login_provider_post**
> ErrorReturn verify_by_login_provider_verification_app_id_verify_by_login_provider_post(app_id, new_app=new_app)

Verify By Login Provider

If the current account is eligible to verify the given account via SSO, and the app is not already verified by
someone else, marks the app as verified.

### Example


```python
import openapi_client
from openapi_client.models.error_return import ErrorReturn
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
    api_instance = openapi_client.VerificationApi(api_client)
    app_id = 'app_id_example' # str | 
    new_app = False # bool |  (optional) (default to False)

    try:
        # Verify By Login Provider
        api_response = api_instance.verify_by_login_provider_verification_app_id_verify_by_login_provider_post(app_id, new_app=new_app)
        print("The response of VerificationApi->verify_by_login_provider_verification_app_id_verify_by_login_provider_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VerificationApi->verify_by_login_provider_verification_app_id_verify_by_login_provider_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **new_app** | **bool**|  | [optional] [default to False]

### Return type

[**ErrorReturn**](ErrorReturn.md)

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

