# GnomeAccountResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | [**ConnectedAccountProvider**](ConnectedAccountProvider.md) |  | 
**id** | **int** |  | 
**gnome_userid** | **int** |  | 
**login** | **str** |  | 
**avatar_url** | **str** |  | 
**display_name** | **str** |  | 
**email** | **str** |  | 
**last_used** | **datetime** |  | 

## Example

```python
from flathub_python_api.models.gnome_account_result import GnomeAccountResult

# TODO update the JSON string below
json = "{}"
# create an instance of GnomeAccountResult from a JSON string
gnome_account_result_instance = GnomeAccountResult.from_json(json)
# print the JSON string representation of the object
print(GnomeAccountResult.to_json())

# convert the object into a dict
gnome_account_result_dict = gnome_account_result_instance.to_dict()
# create an instance of GnomeAccountResult from a dict
gnome_account_result_from_dict = GnomeAccountResult.from_dict(gnome_account_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


