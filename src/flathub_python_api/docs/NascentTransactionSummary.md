# NascentTransactionSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **int** |  | 
**currency** | **str** |  | 
**kind** | **str** |  | 

## Example

```python
from openapi_client.models.nascent_transaction_summary import NascentTransactionSummary

# TODO update the JSON string below
json = "{}"
# create an instance of NascentTransactionSummary from a JSON string
nascent_transaction_summary_instance = NascentTransactionSummary.from_json(json)
# print the JSON string representation of the object
print(NascentTransactionSummary.to_json())

# convert the object into a dict
nascent_transaction_summary_dict = nascent_transaction_summary_instance.to_dict()
# create an instance of NascentTransactionSummary from a dict
nascent_transaction_summary_from_dict = NascentTransactionSummary.from_dict(nascent_transaction_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


