# DeleteUserResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**message** | **str** |  | [optional] 

## Example

```python
from flathub_python_api.models.delete_user_result import DeleteUserResult

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteUserResult from a JSON string
delete_user_result_instance = DeleteUserResult.from_json(json)
# print the JSON string representation of the object
print(DeleteUserResult.to_json())

# convert the object into a dict
delete_user_result_dict = delete_user_result_instance.to_dict()
# create an instance of DeleteUserResult from a dict
delete_user_result_from_dict = DeleteUserResult.from_dict(delete_user_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


