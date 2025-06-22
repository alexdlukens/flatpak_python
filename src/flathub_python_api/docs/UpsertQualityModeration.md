# UpsertQualityModeration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guideline_id** | **str** |  | 
**passed** | **bool** |  | 

## Example

```python
from openapi_client.models.upsert_quality_moderation import UpsertQualityModeration

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertQualityModeration from a JSON string
upsert_quality_moderation_instance = UpsertQualityModeration.from_json(json)
# print the JSON string representation of the object
print(UpsertQualityModeration.to_json())

# convert the object into a dict
upsert_quality_moderation_dict = upsert_quality_moderation_instance.to_dict()
# create an instance of UpsertQualityModeration from a dict
upsert_quality_moderation_from_dict = UpsertQualityModeration.from_dict(upsert_quality_moderation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


