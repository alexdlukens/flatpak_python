# TransactionRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipient** | **str** |  | 
**amount** | **int** |  | 
**currency** | **str** |  | 
**kind** | **str** |  | 

## Example

```python
from openapi_client.models.transaction_row import TransactionRow

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionRow from a JSON string
transaction_row_instance = TransactionRow.from_json(json)
# print the JSON string representation of the object
print(TransactionRow.to_json())

# convert the object into a dict
transaction_row_dict = transaction_row_instance.to_dict()
# create an instance of TransactionRow from a dict
transaction_row_from_dict = TransactionRow.from_dict(transaction_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


