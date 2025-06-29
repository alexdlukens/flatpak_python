# flathub_python_api.VendingApi

All URIs are relative to *https://flathub.org/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_info_vendingapp_app_id_info_get**](VendingApi.md#app_info_vendingapp_app_id_info_get) | **GET** /vendingapp/{app_id}/info | App Info
[**cancel_tokens_vendingapp_app_id_tokens_cancel_post**](VendingApi.md#cancel_tokens_vendingapp_app_id_tokens_cancel_post) | **POST** /vendingapp/{app_id}/tokens/cancel | Cancel Tokens
[**create_tokens_vendingapp_app_id_tokens_post**](VendingApi.md#create_tokens_vendingapp_app_id_tokens_post) | **POST** /vendingapp/{app_id}/tokens | Create Tokens
[**get_app_vending_setup_vendingapp_app_id_setup_get**](VendingApi.md#get_app_vending_setup_vendingapp_app_id_setup_get) | **GET** /vendingapp/{app_id}/setup | Get App Vending Setup
[**get_dashboard_link_vending_status_dashboardlink_get**](VendingApi.md#get_dashboard_link_vending_status_dashboardlink_get) | **GET** /vending/status/dashboardlink | Get Dashboard Link
[**get_global_vending_config_vending_config_get**](VendingApi.md#get_global_vending_config_vending_config_get) | **GET** /vending/config | Get Global Vending Config
[**get_redeemable_tokens_vendingapp_app_id_tokens_get**](VendingApi.md#get_redeemable_tokens_vendingapp_app_id_tokens_get) | **GET** /vendingapp/{app_id}/tokens | Get Redeemable Tokens
[**post_app_vending_setup_vendingapp_app_id_setup_post**](VendingApi.md#post_app_vending_setup_vendingapp_app_id_setup_post) | **POST** /vendingapp/{app_id}/setup | Post App Vending Setup
[**post_app_vending_status_vendingapp_app_id_post**](VendingApi.md#post_app_vending_status_vendingapp_app_id_post) | **POST** /vendingapp/{app_id} | Post App Vending Status
[**redeem_token_vendingapp_app_id_tokens_redeem_token_post**](VendingApi.md#redeem_token_vendingapp_app_id_tokens_redeem_token_post) | **POST** /vendingapp/{app_id}/tokens/redeem/{token} | Redeem Token
[**start_onboarding_vending_status_onboarding_post**](VendingApi.md#start_onboarding_vending_status_onboarding_post) | **POST** /vending/status/onboarding | Start Onboarding
[**status_vending_status_get**](VendingApi.md#status_vending_status_get) | **GET** /vending/status | Status


# **app_info_vendingapp_app_id_info_get**
> VendingApplicationInformation app_info_vendingapp_app_id_info_get(app_id)

App Info

This determines the vending info for the app and returns it

### Example


```python
import flathub_python_api
from flathub_python_api.models.vending_application_information import VendingApplicationInformation
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
    api_instance = flathub_python_api.VendingApi(api_client)
    app_id = 'app_id_example' # str | 

    try:
        # App Info
        api_response = api_instance.app_info_vendingapp_app_id_info_get(app_id)
        print("The response of VendingApi->app_info_vendingapp_app_id_info_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VendingApi->app_info_vendingapp_app_id_info_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 

### Return type

[**VendingApplicationInformation**](VendingApplicationInformation.md)

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

# **cancel_tokens_vendingapp_app_id_tokens_cancel_post**
> List[TokenCancellation] cancel_tokens_vendingapp_app_id_tokens_cancel_post(app_id, request_body)

Cancel Tokens

Cancel a set of tokens

### Example


```python
import flathub_python_api
from flathub_python_api.models.token_cancellation import TokenCancellation
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
    api_instance = flathub_python_api.VendingApi(api_client)
    app_id = 'app_id_example' # str | 
    request_body = ['request_body_example'] # List[str] | 

    try:
        # Cancel Tokens
        api_response = api_instance.cancel_tokens_vendingapp_app_id_tokens_cancel_post(app_id, request_body)
        print("The response of VendingApi->cancel_tokens_vendingapp_app_id_tokens_cancel_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VendingApi->cancel_tokens_vendingapp_app_id_tokens_cancel_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **request_body** | [**List[str]**](str.md)|  | 

### Return type

[**List[TokenCancellation]**](TokenCancellation.md)

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

# **create_tokens_vendingapp_app_id_tokens_post**
> List[TokenModel] create_tokens_vendingapp_app_id_tokens_post(app_id, request_body)

Create Tokens

Create some tokens for the given appid.

The calling user must own the vending config for this application

### Example


```python
import flathub_python_api
from flathub_python_api.models.token_model import TokenModel
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
    api_instance = flathub_python_api.VendingApi(api_client)
    app_id = 'app_id_example' # str | 
    request_body = ['request_body_example'] # List[Optional[str]] | 

    try:
        # Create Tokens
        api_response = api_instance.create_tokens_vendingapp_app_id_tokens_post(app_id, request_body)
        print("The response of VendingApi->create_tokens_vendingapp_app_id_tokens_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VendingApi->create_tokens_vendingapp_app_id_tokens_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **request_body** | [**List[Optional[str]]**](str.md)|  | 

### Return type

[**List[TokenModel]**](TokenModel.md)

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

# **get_app_vending_setup_vendingapp_app_id_setup_get**
> VendingSetup get_app_vending_setup_vendingapp_app_id_setup_get(app_id)

Get App Vending Setup

Retrieve the vending status for a given application.

### Example


```python
import flathub_python_api
from flathub_python_api.models.vending_setup import VendingSetup
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
    api_instance = flathub_python_api.VendingApi(api_client)
    app_id = 'app_id_example' # str | 

    try:
        # Get App Vending Setup
        api_response = api_instance.get_app_vending_setup_vendingapp_app_id_setup_get(app_id)
        print("The response of VendingApi->get_app_vending_setup_vendingapp_app_id_setup_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VendingApi->get_app_vending_setup_vendingapp_app_id_setup_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 

### Return type

[**VendingSetup**](VendingSetup.md)

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

# **get_dashboard_link_vending_status_dashboardlink_get**
> VendingRedirect get_dashboard_link_vending_status_dashboardlink_get()

Get Dashboard Link

Retrieve a link to the logged in user's Stripe express dashboard.

The user must be logged in and must have onboarded.

### Example


```python
import flathub_python_api
from flathub_python_api.models.vending_redirect import VendingRedirect
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
    api_instance = flathub_python_api.VendingApi(api_client)

    try:
        # Get Dashboard Link
        api_response = api_instance.get_dashboard_link_vending_status_dashboardlink_get()
        print("The response of VendingApi->get_dashboard_link_vending_status_dashboardlink_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VendingApi->get_dashboard_link_vending_status_dashboardlink_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**VendingRedirect**](VendingRedirect.md)

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

# **get_global_vending_config_vending_config_get**
> VendingConfig get_global_vending_config_vending_config_get()

Get Global Vending Config

Retrieve the configuration values needed to calculate application
vending splits client-side.

Configuration includes:
- Fee values
- Platform values

### Example


```python
import flathub_python_api
from flathub_python_api.models.vending_config import VendingConfig
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
    api_instance = flathub_python_api.VendingApi(api_client)

    try:
        # Get Global Vending Config
        api_response = api_instance.get_global_vending_config_vending_config_get()
        print("The response of VendingApi->get_global_vending_config_vending_config_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VendingApi->get_global_vending_config_vending_config_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**VendingConfig**](VendingConfig.md)

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

# **get_redeemable_tokens_vendingapp_app_id_tokens_get**
> TokenList get_redeemable_tokens_vendingapp_app_id_tokens_get(app_id)

Get Redeemable Tokens

Retrieve the redeemable tokens for the given application.

The caller must have control of the app at some level

For now, there is no pagination or filtering, all tokens will be returned

### Example


```python
import flathub_python_api
from flathub_python_api.models.token_list import TokenList
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
    api_instance = flathub_python_api.VendingApi(api_client)
    app_id = 'app_id_example' # str | 

    try:
        # Get Redeemable Tokens
        api_response = api_instance.get_redeemable_tokens_vendingapp_app_id_tokens_get(app_id)
        print("The response of VendingApi->get_redeemable_tokens_vendingapp_app_id_tokens_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VendingApi->get_redeemable_tokens_vendingapp_app_id_tokens_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 

### Return type

[**TokenList**](TokenList.md)

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

# **post_app_vending_setup_vendingapp_app_id_setup_post**
> VendingSetup post_app_vending_setup_vendingapp_app_id_setup_post(app_id, vending_setup_request)

Post App Vending Setup

Create/update the vending status for a given application.  Returns an error
if the appid is not known, or if it's already set up for vending with a
user other than the one calling this API.

If you do not have the right to set the vending status for this application
then you will also be refused.

In addition, if any of the currency or amount values constraints are violated
then you will get an error

### Example


```python
import flathub_python_api
from flathub_python_api.models.vending_setup import VendingSetup
from flathub_python_api.models.vending_setup_request import VendingSetupRequest
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
    api_instance = flathub_python_api.VendingApi(api_client)
    app_id = 'app_id_example' # str | 
    vending_setup_request = flathub_python_api.VendingSetupRequest() # VendingSetupRequest | 

    try:
        # Post App Vending Setup
        api_response = api_instance.post_app_vending_setup_vendingapp_app_id_setup_post(app_id, vending_setup_request)
        print("The response of VendingApi->post_app_vending_setup_vendingapp_app_id_setup_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VendingApi->post_app_vending_setup_vendingapp_app_id_setup_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **vending_setup_request** | [**VendingSetupRequest**](VendingSetupRequest.md)|  | 

### Return type

[**VendingSetup**](VendingSetup.md)

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

# **post_app_vending_status_vendingapp_app_id_post**
> VendingOutput post_app_vending_status_vendingapp_app_id_post(app_id, proposed_payment)

Post App Vending Status

Construct a transaction for the given application with the proposed payment.
If the proposed payment is unacceptable then an error will be returned.
If the user is not logged in, then an error will be returned.

Otherwise a transaction will be created and the information about it will be
returned in the output of the call.

### Example


```python
import flathub_python_api
from flathub_python_api.models.proposed_payment import ProposedPayment
from flathub_python_api.models.vending_output import VendingOutput
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
    api_instance = flathub_python_api.VendingApi(api_client)
    app_id = 'app_id_example' # str | 
    proposed_payment = flathub_python_api.ProposedPayment() # ProposedPayment | 

    try:
        # Post App Vending Status
        api_response = api_instance.post_app_vending_status_vendingapp_app_id_post(app_id, proposed_payment)
        print("The response of VendingApi->post_app_vending_status_vendingapp_app_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VendingApi->post_app_vending_status_vendingapp_app_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **proposed_payment** | [**ProposedPayment**](ProposedPayment.md)|  | 

### Return type

[**VendingOutput**](VendingOutput.md)

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

# **redeem_token_vendingapp_app_id_tokens_redeem_token_post**
> RedemptionResult redeem_token_vendingapp_app_id_tokens_redeem_token_post(app_id, token)

Redeem Token

This redeems the given token for the logged in user.

If the logged in user already owns the app then the token will not be redeemed

### Example


```python
import flathub_python_api
from flathub_python_api.models.redemption_result import RedemptionResult
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
    api_instance = flathub_python_api.VendingApi(api_client)
    app_id = 'app_id_example' # str | 
    token = 'token_example' # str | 

    try:
        # Redeem Token
        api_response = api_instance.redeem_token_vendingapp_app_id_tokens_redeem_token_post(app_id, token)
        print("The response of VendingApi->redeem_token_vendingapp_app_id_tokens_redeem_token_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VendingApi->redeem_token_vendingapp_app_id_tokens_redeem_token_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **token** | **str**|  | 

### Return type

[**RedemptionResult**](RedemptionResult.md)

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

# **start_onboarding_vending_status_onboarding_post**
> VendingRedirect start_onboarding_vending_status_onboarding_post(vending_onboarding_request)

Start Onboarding

Start or continue the onboarding process.

### Example


```python
import flathub_python_api
from flathub_python_api.models.vending_onboarding_request import VendingOnboardingRequest
from flathub_python_api.models.vending_redirect import VendingRedirect
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
    api_instance = flathub_python_api.VendingApi(api_client)
    vending_onboarding_request = flathub_python_api.VendingOnboardingRequest() # VendingOnboardingRequest | 

    try:
        # Start Onboarding
        api_response = api_instance.start_onboarding_vending_status_onboarding_post(vending_onboarding_request)
        print("The response of VendingApi->start_onboarding_vending_status_onboarding_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VendingApi->start_onboarding_vending_status_onboarding_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vending_onboarding_request** | [**VendingOnboardingRequest**](VendingOnboardingRequest.md)|  | 

### Return type

[**VendingRedirect**](VendingRedirect.md)

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

# **status_vending_status_get**
> VendingStatus status_vending_status_get()

Status

Retrieve the vending status of the logged in user.

This will return `201` if the logged in user has never begun the onboarding
flow to be a vendor on Flathub.

### Example


```python
import flathub_python_api
from flathub_python_api.models.vending_status import VendingStatus
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
    api_instance = flathub_python_api.VendingApi(api_client)

    try:
        # Status
        api_response = api_instance.status_vending_status_get()
        print("The response of VendingApi->status_vending_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VendingApi->status_vending_status_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**VendingStatus**](VendingStatus.md)

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

