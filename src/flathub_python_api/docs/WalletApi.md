# flathub_python_api.WalletApi

All URIs are relative to *https://flathub.org/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_transaction_wallet_transactions_txn_cancel_post**](WalletApi.md#cancel_transaction_wallet_transactions_txn_cancel_post) | **POST** /wallet/transactions/{txn}/cancel | Cancel Transaction
[**create_transaction_wallet_transactions_post**](WalletApi.md#create_transaction_wallet_transactions_post) | **POST** /wallet/transactions | Create Transaction
[**get_stripedata_wallet_stripedata_get**](WalletApi.md#get_stripedata_wallet_stripedata_get) | **GET** /wallet/stripedata | Get Stripedata
[**get_transaction_by_id_wallet_transactions_txn_get**](WalletApi.md#get_transaction_by_id_wallet_transactions_txn_get) | **GET** /wallet/transactions/{txn} | Get Transaction By Id
[**get_transactions_wallet_transactions_get**](WalletApi.md#get_transactions_wallet_transactions_get) | **GET** /wallet/transactions | Get Transactions
[**get_txn_stripedata_wallet_transactions_txn_stripe_get**](WalletApi.md#get_txn_stripedata_wallet_transactions_txn_stripe_get) | **GET** /wallet/transactions/{txn}/stripe | Get Txn Stripedata
[**get_walletinfo_wallet_walletinfo_get**](WalletApi.md#get_walletinfo_wallet_walletinfo_get) | **GET** /wallet/walletinfo | Get Walletinfo
[**post_removecard_wallet_removecard_post**](WalletApi.md#post_removecard_wallet_removecard_post) | **POST** /wallet/removecard | Post Removecard
[**set_pending_wallet_transactions_txn_setpending_post**](WalletApi.md#set_pending_wallet_transactions_txn_setpending_post) | **POST** /wallet/transactions/{txn}/setpending | Set Pending
[**set_savecard_wallet_transactions_txn_savecard_post**](WalletApi.md#set_savecard_wallet_transactions_txn_savecard_post) | **POST** /wallet/transactions/{txn}/savecard | Set Savecard
[**set_transaction_card_wallet_transactions_txn_setcard_post**](WalletApi.md#set_transaction_card_wallet_transactions_txn_setcard_post) | **POST** /wallet/transactions/{txn}/setcard | Set Transaction Card
[**webhook_wallet_webhook_stripe_post**](WalletApi.md#webhook_wallet_webhook_stripe_post) | **POST** /wallet/webhook/stripe | Webhook


# **cancel_transaction_wallet_transactions_txn_cancel_post**
> object cancel_transaction_wallet_transactions_txn_cancel_post(txn)

Cancel Transaction

Cancel a transaction in the `new` or `retry` states.

Note that this may actually not cancel if a webhook fires asynchronously
and updates the transaction.  This API will not attempt to prevent stripe
payments from completing.

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
    api_instance = flathub_python_api.WalletApi(api_client)
    txn = 'txn_example' # str | 

    try:
        # Cancel Transaction
        api_response = api_instance.cancel_transaction_wallet_transactions_txn_cancel_post(txn)
        print("The response of WalletApi->cancel_transaction_wallet_transactions_txn_cancel_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->cancel_transaction_wallet_transactions_txn_cancel_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **txn** | **str**|  | 

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

# **create_transaction_wallet_transactions_post**
> PostTransactionResponse create_transaction_wallet_transactions_post(nascent_transaction)

Create Transaction

Create a new transaction, return the ID.

If the passed in nascent transaction is valid, this will create a transaction and
return the ID of the newly created wallet, otherwise it'll return an error

### Example


```python
import flathub_python_api
from flathub_python_api.models.nascent_transaction import NascentTransaction
from flathub_python_api.models.post_transaction_response import PostTransactionResponse
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
    api_instance = flathub_python_api.WalletApi(api_client)
    nascent_transaction = flathub_python_api.NascentTransaction() # NascentTransaction | 

    try:
        # Create Transaction
        api_response = api_instance.create_transaction_wallet_transactions_post(nascent_transaction)
        print("The response of WalletApi->create_transaction_wallet_transactions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->create_transaction_wallet_transactions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nascent_transaction** | [**NascentTransaction**](NascentTransaction.md)|  | 

### Return type

[**PostTransactionResponse**](PostTransactionResponse.md)

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

# **get_stripedata_wallet_stripedata_get**
> StripeKeys get_stripedata_wallet_stripedata_get()

Get Stripedata

Return the stripe public key to use in the frontend.  Since this is not
considered secret, we don't need a login or anything for this

### Example


```python
import flathub_python_api
from flathub_python_api.models.stripe_keys import StripeKeys
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
    api_instance = flathub_python_api.WalletApi(api_client)

    try:
        # Get Stripedata
        api_response = api_instance.get_stripedata_wallet_stripedata_get()
        print("The response of WalletApi->get_stripedata_wallet_stripedata_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->get_stripedata_wallet_stripedata_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**StripeKeys**](StripeKeys.md)

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

# **get_transaction_by_id_wallet_transactions_txn_get**
> Transaction get_transaction_by_id_wallet_transactions_txn_get(txn)

Get Transaction By Id

Retrieve a transaction by its ID

If the transaction ID is valid, and owned by the calling user, then this will
retrieve the whole transaction, including card details and disbursement information
if available.

### Example


```python
import flathub_python_api
from flathub_python_api.models.transaction import Transaction
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
    api_instance = flathub_python_api.WalletApi(api_client)
    txn = 'txn_example' # str | 

    try:
        # Get Transaction By Id
        api_response = api_instance.get_transaction_by_id_wallet_transactions_txn_get(txn)
        print("The response of WalletApi->get_transaction_by_id_wallet_transactions_txn_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->get_transaction_by_id_wallet_transactions_txn_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **txn** | **str**|  | 

### Return type

[**Transaction**](Transaction.md)

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

# **get_transactions_wallet_transactions_get**
> List[TransactionSummary] get_transactions_wallet_transactions_get(sort=sort, since=since, limit=limit)

Get Transactions

Return a list of transactions associated with this user.

If anything goes wrong, an error will be returned, otherwise a list of transaction
summaries will be returned.

### Example


```python
import flathub_python_api
from flathub_python_api.models.transaction_sort_order import TransactionSortOrder
from flathub_python_api.models.transaction_summary import TransactionSummary
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
    api_instance = flathub_python_api.WalletApi(api_client)
    sort = flathub_python_api.TransactionSortOrder() # TransactionSortOrder |  (optional)
    since = 'since_example' # str |  (optional)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # Get Transactions
        api_response = api_instance.get_transactions_wallet_transactions_get(sort=sort, since=since, limit=limit)
        print("The response of WalletApi->get_transactions_wallet_transactions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->get_transactions_wallet_transactions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | [**TransactionSortOrder**](.md)|  | [optional] 
 **since** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**List[TransactionSummary]**](TransactionSummary.md)

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

# **get_txn_stripedata_wallet_transactions_txn_stripe_get**
> TransactionStripeData get_txn_stripedata_wallet_transactions_txn_stripe_get(txn)

Get Txn Stripedata

Return the Stripe data associated with the given transaction.

This is only applicable to transactions in the `new` or `retry` state and
will only work for transactions which *are* Stripe transactions.

### Example


```python
import flathub_python_api
from flathub_python_api.models.transaction_stripe_data import TransactionStripeData
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
    api_instance = flathub_python_api.WalletApi(api_client)
    txn = 'txn_example' # str | 

    try:
        # Get Txn Stripedata
        api_response = api_instance.get_txn_stripedata_wallet_transactions_txn_stripe_get(txn)
        print("The response of WalletApi->get_txn_stripedata_wallet_transactions_txn_stripe_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->get_txn_stripedata_wallet_transactions_txn_stripe_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **txn** | **str**|  | 

### Return type

[**TransactionStripeData**](TransactionStripeData.md)

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

# **get_walletinfo_wallet_walletinfo_get**
> WalletInfo get_walletinfo_wallet_walletinfo_get()

Get Walletinfo

Retrieve the wallet for the currently logged in user.

This will return a list of cards which the user has saved to their account.

### Example


```python
import flathub_python_api
from flathub_python_api.models.wallet_info import WalletInfo
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
    api_instance = flathub_python_api.WalletApi(api_client)

    try:
        # Get Walletinfo
        api_response = api_instance.get_walletinfo_wallet_walletinfo_get()
        print("The response of WalletApi->get_walletinfo_wallet_walletinfo_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->get_walletinfo_wallet_walletinfo_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WalletInfo**](WalletInfo.md)

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

# **post_removecard_wallet_removecard_post**
> object post_removecard_wallet_removecard_post(payment_card_info)

Post Removecard

Remove a card from a user's wallet.

The provided information must exactly match a card as would be returned from the
wallet info endpoint.

### Example


```python
import flathub_python_api
from flathub_python_api.models.payment_card_info import PaymentCardInfo
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
    api_instance = flathub_python_api.WalletApi(api_client)
    payment_card_info = flathub_python_api.PaymentCardInfo() # PaymentCardInfo | 

    try:
        # Post Removecard
        api_response = api_instance.post_removecard_wallet_removecard_post(payment_card_info)
        print("The response of WalletApi->post_removecard_wallet_removecard_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->post_removecard_wallet_removecard_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_card_info** | [**PaymentCardInfo**](PaymentCardInfo.md)|  | 

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

# **set_pending_wallet_transactions_txn_setpending_post**
> object set_pending_wallet_transactions_txn_setpending_post(txn)

Set Pending

Set the transaction as 'pending' so that we can recover if Stripe
flows don't quite work (e.g. webhook goes missing)

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
    api_instance = flathub_python_api.WalletApi(api_client)
    txn = 'txn_example' # str | 

    try:
        # Set Pending
        api_response = api_instance.set_pending_wallet_transactions_txn_setpending_post(txn)
        print("The response of WalletApi->set_pending_wallet_transactions_txn_setpending_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->set_pending_wallet_transactions_txn_setpending_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **txn** | **str**|  | 

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

# **set_savecard_wallet_transactions_txn_savecard_post**
> object set_savecard_wallet_transactions_txn_savecard_post(txn, transaction_save_card)

Set Savecard

Set the save-card status.

This is only applicable to transactions in the `new` or `retry` state
and will only work for transactions which are backed by stripe or similar.

If the `save_card` parameter is null, then the card will not be saved,
otherwise it will be saved.  If it's set to `off_session` then an attempt
will be made to create a saved method which can be used without the user
re-authenticating

### Example


```python
import flathub_python_api
from flathub_python_api.models.transaction_save_card import TransactionSaveCard
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
    api_instance = flathub_python_api.WalletApi(api_client)
    txn = 'txn_example' # str | 
    transaction_save_card = flathub_python_api.TransactionSaveCard() # TransactionSaveCard | 

    try:
        # Set Savecard
        api_response = api_instance.set_savecard_wallet_transactions_txn_savecard_post(txn, transaction_save_card)
        print("The response of WalletApi->set_savecard_wallet_transactions_txn_savecard_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->set_savecard_wallet_transactions_txn_savecard_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **txn** | **str**|  | 
 **transaction_save_card** | [**TransactionSaveCard**](TransactionSaveCard.md)|  | 

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

# **set_transaction_card_wallet_transactions_txn_setcard_post**
> object set_transaction_card_wallet_transactions_txn_setcard_post(txn, payment_card_info)

Set Transaction Card

Set the card associated with a transaction.

The posted card must exactly match one of the cards returned by the wallet
info endpoint or else the update may not succeed

### Example


```python
import flathub_python_api
from flathub_python_api.models.payment_card_info import PaymentCardInfo
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
    api_instance = flathub_python_api.WalletApi(api_client)
    txn = 'txn_example' # str | 
    payment_card_info = flathub_python_api.PaymentCardInfo() # PaymentCardInfo | 

    try:
        # Set Transaction Card
        api_response = api_instance.set_transaction_card_wallet_transactions_txn_setcard_post(txn, payment_card_info)
        print("The response of WalletApi->set_transaction_card_wallet_transactions_txn_setcard_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->set_transaction_card_wallet_transactions_txn_setcard_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **txn** | **str**|  | 
 **payment_card_info** | [**PaymentCardInfo**](PaymentCardInfo.md)|  | 

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

# **webhook_wallet_webhook_stripe_post**
> object webhook_wallet_webhook_stripe_post()

Webhook

This endpoint is intended to deal with webhooks coming back from payment
mechanisms etc.  It exists only for the deployed wallet, so its name
will vary with the deployed wallet kind.

The exact form of the content posted to the webhook will vary from wallet
kind to wallet kind.

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
    api_instance = flathub_python_api.WalletApi(api_client)

    try:
        # Webhook
        api_response = api_instance.webhook_wallet_webhook_stripe_post()
        print("The response of WalletApi->webhook_wallet_webhook_stripe_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletApi->webhook_wallet_webhook_stripe_post: %s\n" % e)
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

