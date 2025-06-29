# TokenList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**total** | **int** |  | 
**tokens** | [**List[TokenModel]**](TokenModel.md) |  | 

## Example

```python
from flathub_python_api.models.token_list import TokenList

# TODO update the JSON string below
json = "{}"
# create an instance of TokenList from a JSON string
token_list_instance = TokenList.from_json(json)
# print the JSON string representation of the object
print(TokenList.to_json())

# convert the object into a dict
token_list_dict = token_list_instance.to_dict()
# create an instance of TokenList from a dict
token_list_from_dict = TokenList.from_dict(token_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


