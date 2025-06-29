# flathub_python_api.PurchaseApi

All URIs are relative to *https://flathub.org/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_purchases_purchases_check_purchases_post**](PurchaseApi.md#check_purchases_purchases_check_purchases_post) | **POST** /purchases/check-purchases | Check Purchases
[**get_download_token_purchases_generate_download_token_post**](PurchaseApi.md#get_download_token_purchases_generate_download_token_post) | **POST** /purchases/generate-download-token | Get Download Token
[**get_is_free_software_purchases_storefront_info_is_free_software_get**](PurchaseApi.md#get_is_free_software_purchases_storefront_info_is_free_software_get) | **GET** /purchases/storefront-info/is-free-software | Get Is Free Software
[**get_storefront_info_purchases_storefront_info_get**](PurchaseApi.md#get_storefront_info_purchases_storefront_info_get) | **GET** /purchases/storefront-info | Get Storefront Info
[**get_update_token_purchases_generate_update_token_post**](PurchaseApi.md#get_update_token_purchases_generate_update_token_post) | **POST** /purchases/generate-update-token | Get Update Token


# **check_purchases_purchases_check_purchases_post**
> CheckPurchasesResponseSuccess check_purchases_purchases_check_purchases_post(request_body)

Check Purchases

Checks whether the logged in user is able to download all of the given app refs.

App IDs can be in the form of full refs, e.g. "app/org.gnome.Maps/x86_64/stable", or just the app ID, e.g.
"org.gnome.Maps".

### Example


```python
import flathub_python_api
from flathub_python_api.models.check_purchases_response_success import CheckPurchasesResponseSuccess
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
    api_instance = flathub_python_api.PurchaseApi(api_client)
    request_body = ['request_body_example'] # List[Optional[str]] | 

    try:
        # Check Purchases
        api_response = api_instance.check_purchases_purchases_check_purchases_post(request_body)
        print("The response of PurchaseApi->check_purchases_purchases_check_purchases_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseApi->check_purchases_purchases_check_purchases_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[Optional[str]]**](str.md)|  | 

### Return type

[**CheckPurchasesResponseSuccess**](CheckPurchasesResponseSuccess.md)

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

# **get_download_token_purchases_generate_download_token_post**
> GetDownloadTokenResponse get_download_token_purchases_generate_download_token_post(body_get_download_token_purchases_generate_download_token_post)

Get Download Token

Generates a download token for the given app IDs. App IDs should be in the form of full refs, e.g.
"app/org.gnome.Maps/x86_64/stable".

### Example


```python
import flathub_python_api
from flathub_python_api.models.body_get_download_token_purchases_generate_download_token_post import BodyGetDownloadTokenPurchasesGenerateDownloadTokenPost
from flathub_python_api.models.get_download_token_response import GetDownloadTokenResponse
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
    api_instance = flathub_python_api.PurchaseApi(api_client)
    body_get_download_token_purchases_generate_download_token_post = flathub_python_api.BodyGetDownloadTokenPurchasesGenerateDownloadTokenPost() # BodyGetDownloadTokenPurchasesGenerateDownloadTokenPost | 

    try:
        # Get Download Token
        api_response = api_instance.get_download_token_purchases_generate_download_token_post(body_get_download_token_purchases_generate_download_token_post)
        print("The response of PurchaseApi->get_download_token_purchases_generate_download_token_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseApi->get_download_token_purchases_generate_download_token_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_get_download_token_purchases_generate_download_token_post** | [**BodyGetDownloadTokenPurchasesGenerateDownloadTokenPost**](BodyGetDownloadTokenPurchasesGenerateDownloadTokenPost.md)|  | 

### Return type

[**GetDownloadTokenResponse**](GetDownloadTokenResponse.md)

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

# **get_is_free_software_purchases_storefront_info_is_free_software_get**
> bool get_is_free_software_purchases_storefront_info_is_free_software_get(app_id, license=license)

Get Is Free Software

Gets whether the app is Free Software based on the app ID and license, even if the app is not in the appstream
database yet. This is needed in flat-manager-hooks to run validations the first time an app is uploaded.

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
    api_instance = flathub_python_api.PurchaseApi(api_client)
    app_id = 'app_id_example' # str | 
    license = 'license_example' # str |  (optional)

    try:
        # Get Is Free Software
        api_response = api_instance.get_is_free_software_purchases_storefront_info_is_free_software_get(app_id, license=license)
        print("The response of PurchaseApi->get_is_free_software_purchases_storefront_info_is_free_software_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseApi->get_is_free_software_purchases_storefront_info_is_free_software_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **license** | **str**|  | [optional] 

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

# **get_storefront_info_purchases_storefront_info_get**
> StorefrontInfo get_storefront_info_purchases_storefront_info_get(app_id)

Get Storefront Info

This endpoint is used by the flathub-hooks scripts to get information about an app to insert into the appstream
file and commit metadata.

### Example


```python
import flathub_python_api
from flathub_python_api.models.storefront_info import StorefrontInfo
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
    api_instance = flathub_python_api.PurchaseApi(api_client)
    app_id = 'app_id_example' # str | 

    try:
        # Get Storefront Info
        api_response = api_instance.get_storefront_info_purchases_storefront_info_get(app_id)
        print("The response of PurchaseApi->get_storefront_info_purchases_storefront_info_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseApi->get_storefront_info_purchases_storefront_info_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 

### Return type

[**StorefrontInfo**](StorefrontInfo.md)

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

# **get_update_token_purchases_generate_update_token_post**
> GenerateUpdateTokenResponse get_update_token_purchases_generate_update_token_post()

Get Update Token

Generates an update token for a user account. This token allows the user to generate download tokens for apps they
already own, but does not grant permission to do anything else. By storing this token, flathub-authenticator is
able to update apps without user interaction.

### Example


```python
import flathub_python_api
from flathub_python_api.models.generate_update_token_response import GenerateUpdateTokenResponse
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
    api_instance = flathub_python_api.PurchaseApi(api_client)

    try:
        # Get Update Token
        api_response = api_instance.get_update_token_purchases_generate_update_token_post()
        print("The response of PurchaseApi->get_update_token_purchases_generate_update_token_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseApi->get_update_token_purchases_generate_update_token_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GenerateUpdateTokenResponse**](GenerateUpdateTokenResponse.md)

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

