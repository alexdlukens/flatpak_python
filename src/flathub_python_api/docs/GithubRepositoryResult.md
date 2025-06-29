# GithubRepositoryResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**reponame** | **str** |  | 

## Example

```python
from flathub_python_api.models.github_repository_result import GithubRepositoryResult

# TODO update the JSON string below
json = "{}"
# create an instance of GithubRepositoryResult from a JSON string
github_repository_result_instance = GithubRepositoryResult.from_json(json)
# print the JSON string representation of the object
print(GithubRepositoryResult.to_json())

# convert the object into a dict
github_repository_result_dict = github_repository_result_instance.to_dict()
# create an instance of GithubRepositoryResult from a dict
github_repository_result_from_dict = GithubRepositoryResult.from_dict(github_repository_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


