# WalletInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**cards** | [**List[PaymentCardInfo]**](PaymentCardInfo.md) |  | 

## Example

```python
from flathub_python_api.models.wallet_info import WalletInfo

# TODO update the JSON string below
json = "{}"
# create an instance of WalletInfo from a JSON string
wallet_info_instance = WalletInfo.from_json(json)
# print the JSON string representation of the object
print(WalletInfo.to_json())

# convert the object into a dict
wallet_info_dict = wallet_info_instance.to_dict()
# create an instance of WalletInfo from a dict
wallet_info_from_dict = WalletInfo.from_dict(wallet_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


