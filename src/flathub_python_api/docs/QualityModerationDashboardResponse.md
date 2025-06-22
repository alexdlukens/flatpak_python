# QualityModerationDashboardResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apps** | [**List[QualityModerationDashboardRow]**](QualityModerationDashboardRow.md) |  | 
**pagination** | [**Pagination**](Pagination.md) |  | 

## Example

```python
from openapi_client.models.quality_moderation_dashboard_response import QualityModerationDashboardResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QualityModerationDashboardResponse from a JSON string
quality_moderation_dashboard_response_instance = QualityModerationDashboardResponse.from_json(json)
# print the JSON string representation of the object
print(QualityModerationDashboardResponse.to_json())

# convert the object into a dict
quality_moderation_dashboard_response_dict = quality_moderation_dashboard_response_instance.to_dict()
# create an instance of QualityModerationDashboardResponse from a dict
quality_moderation_dashboard_response_from_dict = QualityModerationDashboardResponse.from_dict(quality_moderation_dashboard_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


