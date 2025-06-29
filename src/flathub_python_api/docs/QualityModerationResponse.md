# QualityModerationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guidelines** | [**List[QualityModerationType]**](QualityModerationType.md) |  | 
**is_fullscreen_app** | **bool** |  | 
**review_requested_at** | **datetime** |  | [optional] 

## Example

```python
from flathub_python_api.models.quality_moderation_response import QualityModerationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QualityModerationResponse from a JSON string
quality_moderation_response_instance = QualityModerationResponse.from_json(json)
# print the JSON string representation of the object
print(QualityModerationResponse.to_json())

# convert the object into a dict
quality_moderation_response_dict = quality_moderation_response_instance.to_dict()
# create an instance of QualityModerationResponse from a dict
quality_moderation_response_from_dict = QualityModerationResponse.from_dict(quality_moderation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


