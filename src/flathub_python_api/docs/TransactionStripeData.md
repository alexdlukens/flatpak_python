# TransactionStripeData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**client_secret** | **str** |  | 
**card** | [**PaymentCardInfo**](PaymentCardInfo.md) |  | [optional] 

## Example

```python
from flathub_python_api.models.transaction_stripe_data import TransactionStripeData

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionStripeData from a JSON string
transaction_stripe_data_instance = TransactionStripeData.from_json(json)
# print the JSON string representation of the object
print(TransactionStripeData.to_json())

# convert the object into a dict
transaction_stripe_data_dict = transaction_stripe_data_instance.to_dict()
# create an instance of TransactionStripeData from a dict
transaction_stripe_data_from_dict = TransactionStripeData.from_dict(transaction_stripe_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


