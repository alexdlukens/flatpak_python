# KdeAccountResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | [**ConnectedAccountProvider**](ConnectedAccountProvider.md) |  | 
**id** | **int** |  | 
**kde_userid** | **int** |  | 
**login** | **str** |  | 
**avatar_url** | **str** |  | 
**display_name** | **str** |  | 
**email** | **str** |  | 
**last_used** | **datetime** |  | 

## Example

```python
from flathub_python_api.models.kde_account_result import KdeAccountResult

# TODO update the JSON string below
json = "{}"
# create an instance of KdeAccountResult from a JSON string
kde_account_result_instance = KdeAccountResult.from_json(json)
# print the JSON string representation of the object
print(KdeAccountResult.to_json())

# convert the object into a dict
kde_account_result_dict = kde_account_result_instance.to_dict()
# create an instance of KdeAccountResult from a dict
kde_account_result_from_dict = KdeAccountResult.from_dict(kde_account_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


