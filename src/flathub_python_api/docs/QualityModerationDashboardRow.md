# QualityModerationDashboardRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**quality_moderation_status** | [**QualityModerationStatus**](QualityModerationStatus.md) |  | 
**appstream** | [**AnyOf**](AnyOf.md) |  | [optional] 
**installs_last_7_days** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.quality_moderation_dashboard_row import QualityModerationDashboardRow

# TODO update the JSON string below
json = "{}"
# create an instance of QualityModerationDashboardRow from a JSON string
quality_moderation_dashboard_row_instance = QualityModerationDashboardRow.from_json(json)
# print the JSON string representation of the object
print(QualityModerationDashboardRow.to_json())

# convert the object into a dict
quality_moderation_dashboard_row_dict = quality_moderation_dashboard_row_instance.to_dict()
# create an instance of QualityModerationDashboardRow from a dict
quality_moderation_dashboard_row_from_dict = QualityModerationDashboardRow.from_dict(quality_moderation_dashboard_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


