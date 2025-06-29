# NascentTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**summary** | [**NascentTransactionSummary**](NascentTransactionSummary.md) |  | 
**details** | [**List[TransactionRow]**](TransactionRow.md) |  | 

## Example

```python
from flathub_python_api.models.nascent_transaction import NascentTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of NascentTransaction from a JSON string
nascent_transaction_instance = NascentTransaction.from_json(json)
# print the JSON string representation of the object
print(NascentTransaction.to_json())

# convert the object into a dict
nascent_transaction_dict = nascent_transaction_instance.to_dict()
# create an instance of NascentTransaction from a dict
nascent_transaction_from_dict = NascentTransaction.from_dict(nascent_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


