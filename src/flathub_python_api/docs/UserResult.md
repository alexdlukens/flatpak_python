# UserResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**display_name** | **str** |  | 
**default_account** | [**DefaultAccount**](DefaultAccount.md) |  | 
**connected_accounts** | [**List[UserResultConnectedAccountsInner]**](UserResultConnectedAccountsInner.md) |  | 
**accepted_publisher_agreement_at** | **datetime** |  | 
**roles** | [**List[UserRoleResult]**](UserRoleResult.md) |  | 
**github_repos** | [**List[GithubRepositoryResult]**](GithubRepositoryResult.md) |  | 
**owned_apps** | [**List[UserOwnedAppResult]**](UserOwnedAppResult.md) |  | 

## Example

```python
from openapi_client.models.user_result import UserResult

# TODO update the JSON string below
json = "{}"
# create an instance of UserResult from a JSON string
user_result_instance = UserResult.from_json(json)
# print the JSON string representation of the object
print(UserResult.to_json())

# convert the object into a dict
user_result_dict = user_result_instance.to_dict()
# create an instance of UserResult from a dict
user_result_from_dict = UserResult.from_dict(user_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


