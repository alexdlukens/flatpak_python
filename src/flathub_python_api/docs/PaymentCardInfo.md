# PaymentCardInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**brand** | **str** |  | 
**country** | **str** |  | 
**exp_month** | **int** |  | 
**exp_year** | **int** |  | 
**last4** | **str** |  | 

## Example

```python
from flathub_python_api.models.payment_card_info import PaymentCardInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentCardInfo from a JSON string
payment_card_info_instance = PaymentCardInfo.from_json(json)
# print the JSON string representation of the object
print(PaymentCardInfo.to_json())

# convert the object into a dict
payment_card_info_dict = payment_card_info_instance.to_dict()
# create an instance of PaymentCardInfo from a dict
payment_card_info_from_dict = PaymentCardInfo.from_dict(payment_card_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


