# FlathubUsersResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[UserResult]**](UserResult.md) |  | 
**pagination** | [**Pagination**](Pagination.md) |  | 

## Example

```python
from openapi_client.models.flathub_users_result import FlathubUsersResult

# TODO update the JSON string below
json = "{}"
# create an instance of FlathubUsersResult from a JSON string
flathub_users_result_instance = FlathubUsersResult.from_json(json)
# print the JSON string representation of the object
print(FlathubUsersResult.to_json())

# convert the object into a dict
flathub_users_result_dict = flathub_users_result_instance.to_dict()
# create an instance of FlathubUsersResult from a dict
flathub_users_result_from_dict = FlathubUsersResult.from_dict(flathub_users_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


