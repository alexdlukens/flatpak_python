# ModerationAppsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apps** | [**List[ModerationAppItem]**](ModerationAppItem.md) |  | 
**apps_count** | **int** |  | 

## Example

```python
from flathub_python_api.models.moderation_apps_response import ModerationAppsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModerationAppsResponse from a JSON string
moderation_apps_response_instance = ModerationAppsResponse.from_json(json)
# print the JSON string representation of the object
print(ModerationAppsResponse.to_json())

# convert the object into a dict
moderation_apps_response_dict = moderation_apps_response_instance.to_dict()
# create an instance of ModerationAppsResponse from a dict
moderation_apps_response_from_dict = ModerationAppsResponse.from_dict(moderation_apps_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


