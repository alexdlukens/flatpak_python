# SimpleQualityModerationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apps** | **List[str]** |  | 
**pagination** | [**Pagination**](Pagination.md) |  | 

## Example

```python
from flathub_python_api.models.simple_quality_moderation_response import SimpleQualityModerationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleQualityModerationResponse from a JSON string
simple_quality_moderation_response_instance = SimpleQualityModerationResponse.from_json(json)
# print the JSON string representation of the object
print(SimpleQualityModerationResponse.to_json())

# convert the object into a dict
simple_quality_moderation_response_dict = simple_quality_moderation_response_instance.to_dict()
# create an instance of SimpleQualityModerationResponse from a dict
simple_quality_moderation_response_from_dict = SimpleQualityModerationResponse.from_dict(simple_quality_moderation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


