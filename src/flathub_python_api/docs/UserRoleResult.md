# UserRoleResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**has_role** | **bool** |  | 

## Example

```python
from openapi_client.models.user_role_result import UserRoleResult

# TODO update the JSON string below
json = "{}"
# create an instance of UserRoleResult from a JSON string
user_role_result_instance = UserRoleResult.from_json(json)
# print the JSON string representation of the object
print(UserRoleResult.to_json())

# convert the object into a dict
user_role_result_dict = user_role_result_instance.to_dict()
# create an instance of UserRoleResult from a dict
user_role_result_from_dict = UserRoleResult.from_dict(user_role_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


