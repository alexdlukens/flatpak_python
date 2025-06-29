# PostTransactionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**id** | **str** |  | 

## Example

```python
from flathub_python_api.models.post_transaction_response import PostTransactionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostTransactionResponse from a JSON string
post_transaction_response_instance = PostTransactionResponse.from_json(json)
# print the JSON string representation of the object
print(PostTransactionResponse.to_json())

# convert the object into a dict
post_transaction_response_dict = post_transaction_response_instance.to_dict()
# create an instance of PostTransactionResponse from a dict
post_transaction_response_from_dict = PostTransactionResponse.from_dict(post_transaction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


