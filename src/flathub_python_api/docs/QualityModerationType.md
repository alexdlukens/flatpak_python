# QualityModerationType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guideline_id** | **str** |  | 
**guideline** | [**Guideline**](Guideline.md) |  | 
**app_id** | **str** |  | 
**updated_at** | **datetime** |  | 
**updated_by** | **int** |  | 
**passed** | **bool** |  | 
**comment** | **str** |  | 
**needed_to_pass_since** | **datetime** |  | 

## Example

```python
from flathub_python_api.models.quality_moderation_type import QualityModerationType

# TODO update the JSON string below
json = "{}"
# create an instance of QualityModerationType from a JSON string
quality_moderation_type_instance = QualityModerationType.from_json(json)
# print the JSON string representation of the object
print(QualityModerationType.to_json())

# convert the object into a dict
quality_moderation_type_dict = quality_moderation_type_instance.to_dict()
# create an instance of QualityModerationType from a dict
quality_moderation_type_from_dict = QualityModerationType.from_dict(quality_moderation_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


