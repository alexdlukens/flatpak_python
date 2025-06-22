# openapi_client.UploadTokensApi

All URIs are relative to *https://flathub.org/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_upload_token_upload_tokens_app_id_post**](UploadTokensApi.md#create_upload_token_upload_tokens_app_id_post) | **POST** /upload-tokens/{app_id} | Create Upload Token
[**get_upload_tokens_upload_tokens_app_id_get**](UploadTokensApi.md#get_upload_tokens_upload_tokens_app_id_get) | **GET** /upload-tokens/{app_id} | Get Upload Tokens
[**revoke_upload_token_upload_tokens_token_id_revoke_post**](UploadTokensApi.md#revoke_upload_token_upload_tokens_token_id_revoke_post) | **POST** /upload-tokens/{token_id}/revoke | Revoke Upload Token


# **create_upload_token_upload_tokens_app_id_post**
> NewTokenResponse create_upload_token_upload_tokens_app_id_post(app_id, upload_token_request)

Create Upload Token

### Example


```python
import openapi_client
from openapi_client.models.new_token_response import NewTokenResponse
from openapi_client.models.upload_token_request import UploadTokenRequest
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
    api_instance = openapi_client.UploadTokensApi(api_client)
    app_id = 'app_id_example' # str | 
    upload_token_request = openapi_client.UploadTokenRequest() # UploadTokenRequest | 

    try:
        # Create Upload Token
        api_response = api_instance.create_upload_token_upload_tokens_app_id_post(app_id, upload_token_request)
        print("The response of UploadTokensApi->create_upload_token_upload_tokens_app_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadTokensApi->create_upload_token_upload_tokens_app_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **upload_token_request** | [**UploadTokenRequest**](UploadTokenRequest.md)|  | 

### Return type

[**NewTokenResponse**](NewTokenResponse.md)

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

# **get_upload_tokens_upload_tokens_app_id_get**
> TokensResponse get_upload_tokens_upload_tokens_app_id_get(app_id, include_expired=include_expired)

Get Upload Tokens

Get all upload tokens for the given app

### Example


```python
import openapi_client
from openapi_client.models.tokens_response import TokensResponse
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
    api_instance = openapi_client.UploadTokensApi(api_client)
    app_id = 'app_id_example' # str | 
    include_expired = False # bool |  (optional) (default to False)

    try:
        # Get Upload Tokens
        api_response = api_instance.get_upload_tokens_upload_tokens_app_id_get(app_id, include_expired=include_expired)
        print("The response of UploadTokensApi->get_upload_tokens_upload_tokens_app_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadTokensApi->get_upload_tokens_upload_tokens_app_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **include_expired** | **bool**|  | [optional] [default to False]

### Return type

[**TokensResponse**](TokensResponse.md)

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

# **revoke_upload_token_upload_tokens_token_id_revoke_post**
> revoke_upload_token_upload_tokens_token_id_revoke_post(token_id)

Revoke Upload Token

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
    api_instance = openapi_client.UploadTokensApi(api_client)
    token_id = 56 # int | 

    try:
        # Revoke Upload Token
        api_instance.revoke_upload_token_upload_tokens_token_id_revoke_post(token_id)
    except Exception as e:
        print("Exception when calling UploadTokensApi->revoke_upload_token_upload_tokens_token_id_revoke_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **int**|  | 

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

