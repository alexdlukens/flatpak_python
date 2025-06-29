# TokensResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tokens** | [**List[TokenResponse]**](TokenResponse.md) |  | 
**is_direct_upload_app** | **bool** |  | 

## Example

```python
from flathub_python_api.models.tokens_response import TokensResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TokensResponse from a JSON string
tokens_response_instance = TokensResponse.from_json(json)
# print the JSON string representation of the object
print(TokensResponse.to_json())

# convert the object into a dict
tokens_response_dict = tokens_response_instance.to_dict()
# create an instance of TokensResponse from a dict
tokens_response_from_dict = TokensResponse.from_dict(tokens_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


