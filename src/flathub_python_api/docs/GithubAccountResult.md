# GithubAccountResult


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

## Example

```python
from flathub_python_api.models.github_account_result import GithubAccountResult

# TODO update the JSON string below
json = "{}"
# create an instance of GithubAccountResult from a JSON string
github_account_result_instance = GithubAccountResult.from_json(json)
# print the JSON string representation of the object
print(GithubAccountResult.to_json())

# convert the object into a dict
github_account_result_dict = github_account_result_instance.to_dict()
# create an instance of GithubAccountResult from a dict
github_account_result_from_dict = GithubAccountResult.from_dict(github_account_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


