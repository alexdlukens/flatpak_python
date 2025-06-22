# GitlabAccountResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | [**ConnectedAccountProvider**](ConnectedAccountProvider.md) |  | 
**id** | **int** |  | 
**gitlab_userid** | **int** |  | 
**login** | **str** |  | 
**avatar_url** | **str** |  | 
**display_name** | **str** |  | 
**email** | **str** |  | 
**last_used** | **datetime** |  | 

## Example

```python
from openapi_client.models.gitlab_account_result import GitlabAccountResult

# TODO update the JSON string below
json = "{}"
# create an instance of GitlabAccountResult from a JSON string
gitlab_account_result_instance = GitlabAccountResult.from_json(json)
# print the JSON string representation of the object
print(GitlabAccountResult.to_json())

# convert the object into a dict
gitlab_account_result_dict = gitlab_account_result_instance.to_dict()
# create an instance of GitlabAccountResult from a dict
gitlab_account_result_from_dict = GitlabAccountResult.from_dict(gitlab_account_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


