# QualityModerationStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**passes** | **bool** |  | 
**unrated** | **int** |  | 
**passed** | **int** |  | 
**not_passed** | **int** |  | 
**last_updated** | **datetime** |  | 
**review_requested_at** | **datetime** |  | [optional] 

## Example

```python
from flathub_python_api.models.quality_moderation_status import QualityModerationStatus

# TODO update the JSON string below
json = "{}"
# create an instance of QualityModerationStatus from a JSON string
quality_moderation_status_instance = QualityModerationStatus.from_json(json)
# print the JSON string representation of the object
print(QualityModerationStatus.to_json())

# convert the object into a dict
quality_moderation_status_dict = quality_moderation_status_instance.to_dict()
# create an instance of QualityModerationStatus from a dict
quality_moderation_status_from_dict = QualityModerationStatus.from_dict(quality_moderation_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


