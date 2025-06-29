# GoogleAccountResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | [**ConnectedAccountProvider**](ConnectedAccountProvider.md) |  | 
**id** | **int** |  | 
**google_userid** | **int** |  | 
**login** | **str** |  | 
**avatar_url** | **str** |  | 
**display_name** | **str** |  | 
**email** | **str** |  | 
**last_used** | **datetime** |  | 

## Example

```python
from flathub_python_api.models.google_account_result import GoogleAccountResult

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleAccountResult from a JSON string
google_account_result_instance = GoogleAccountResult.from_json(json)
# print the JSON string representation of the object
print(GoogleAccountResult.to_json())

# convert the object into a dict
google_account_result_dict = google_account_result_instance.to_dict()
# create an instance of GoogleAccountResult from a dict
google_account_result_from_dict = GoogleAccountResult.from_dict(google_account_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


