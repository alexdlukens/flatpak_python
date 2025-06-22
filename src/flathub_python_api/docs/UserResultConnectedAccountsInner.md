# UserResultConnectedAccountsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | [**ConnectedAccountProvider**](ConnectedAccountProvider.md) |  | 
**id** | **int** |  | 
**github_userid** | **int** |  | 
**login** | **str** |  | 
**avatar_url** | **str** |  | 
**display_name** | **str** |  | 
**email** | **str** |  | 
**last_used** | **datetime** |  | 
**gitlab_userid** | **int** |  | 
**gnome_userid** | **int** |  | 
**google_userid** | **int** |  | 
**kde_userid** | **int** |  | 

## Example

```python
from openapi_client.models.user_result_connected_accounts_inner import UserResultConnectedAccountsInner

# TODO update the JSON string below
json = "{}"
# create an instance of UserResultConnectedAccountsInner from a JSON string
user_result_connected_accounts_inner_instance = UserResultConnectedAccountsInner.from_json(json)
# print the JSON string representation of the object
print(UserResultConnectedAccountsInner.to_json())

# convert the object into a dict
user_result_connected_accounts_inner_dict = user_result_connected_accounts_inner_instance.to_dict()
# create an instance of UserResultConnectedAccountsInner from a dict
user_result_connected_accounts_inner_from_dict = UserResultConnectedAccountsInner.from_dict(user_result_connected_accounts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


