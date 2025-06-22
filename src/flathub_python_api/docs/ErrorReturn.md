# ErrorReturn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | [**ErrorDetail**](ErrorDetail.md) |  | 

## Example

```python
from openapi_client.models.error_return import ErrorReturn

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorReturn from a JSON string
error_return_instance = ErrorReturn.from_json(json)
# print the JSON string representation of the object
print(ErrorReturn.to_json())

# convert the object into a dict
error_return_dict = error_return_instance.to_dict()
# create an instance of ErrorReturn from a dict
error_return_from_dict = ErrorReturn.from_dict(error_return_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


