# UserOwnedAppResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** |  | 
**created** | **datetime** |  | 

## Example

```python
from flathub_python_api.models.user_owned_app_result import UserOwnedAppResult

# TODO update the JSON string below
json = "{}"
# create an instance of UserOwnedAppResult from a JSON string
user_owned_app_result_instance = UserOwnedAppResult.from_json(json)
# print the JSON string representation of the object
print(UserOwnedAppResult.to_json())

# convert the object into a dict
user_owned_app_result_dict = user_owned_app_result_instance.to_dict()
# create an instance of UserOwnedAppResult from a dict
user_owned_app_result_from_dict = UserOwnedAppResult.from_dict(user_owned_app_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


