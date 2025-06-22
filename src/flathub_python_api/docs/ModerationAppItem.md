# ModerationAppItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appid** | **str** |  | 
**is_new_submission** | **bool** |  | 
**updated_at** | **datetime** |  | [optional] 
**request_types** | [**List[ModerationRequestType]**](ModerationRequestType.md) |  | 

## Example

```python
from openapi_client.models.moderation_app_item import ModerationAppItem

# TODO update the JSON string below
json = "{}"
# create an instance of ModerationAppItem from a JSON string
moderation_app_item_instance = ModerationAppItem.from_json(json)
# print the JSON string representation of the object
print(ModerationAppItem.to_json())

# convert the object into a dict
moderation_app_item_dict = moderation_app_item_instance.to_dict()
# create an instance of ModerationAppItem from a dict
moderation_app_item_from_dict = ModerationAppItem.from_dict(moderation_app_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


