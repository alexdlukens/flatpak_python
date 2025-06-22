# ModerationApp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**List[ModerationRequestResponse]**](ModerationRequestResponse.md) |  | 
**requests_count** | **int** |  | 

## Example

```python
from openapi_client.models.moderation_app import ModerationApp

# TODO update the JSON string below
json = "{}"
# create an instance of ModerationApp from a JSON string
moderation_app_instance = ModerationApp.from_json(json)
# print the JSON string representation of the object
print(ModerationApp.to_json())

# convert the object into a dict
moderation_app_dict = moderation_app_instance.to_dict()
# create an instance of ModerationApp from a dict
moderation_app_from_dict = ModerationApp.from_dict(moderation_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


