# TransactionSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**value** | **int** |  | 
**currency** | **str** |  | 
**kind** | **str** |  | 
**status** | **str** |  | 
**reason** | **str** |  | [optional] 
**created** | **int** |  | [optional] 
**updated** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.transaction_summary import TransactionSummary

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionSummary from a JSON string
transaction_summary_instance = TransactionSummary.from_json(json)
# print the JSON string representation of the object
print(TransactionSummary.to_json())

# convert the object into a dict
transaction_summary_dict = transaction_summary_instance.to_dict()
# create an instance of TransactionSummary from a dict
transaction_summary_from_dict = TransactionSummary.from_dict(transaction_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


