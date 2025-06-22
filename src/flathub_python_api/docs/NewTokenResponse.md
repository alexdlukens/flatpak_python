# NewTokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | 
**details** | [**TokenResponse**](TokenResponse.md) |  | 

## Example

```python
from openapi_client.models.new_token_response import NewTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NewTokenResponse from a JSON string
new_token_response_instance = NewTokenResponse.from_json(json)
# print the JSON string representation of the object
print(NewTokenResponse.to_json())

# convert the object into a dict
new_token_response_dict = new_token_response_instance.to_dict()
# create an instance of NewTokenResponse from a dict
new_token_response_from_dict = NewTokenResponse.from_dict(new_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


