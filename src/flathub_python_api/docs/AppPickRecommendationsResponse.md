# AppPickRecommendationsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recommendations** | [**List[AppPickRecommendation]**](AppPickRecommendation.md) |  | 

## Example

```python
from openapi_client.models.app_pick_recommendations_response import AppPickRecommendationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppPickRecommendationsResponse from a JSON string
app_pick_recommendations_response_instance = AppPickRecommendationsResponse.from_json(json)
# print the JSON string representation of the object
print(AppPickRecommendationsResponse.to_json())

# convert the object into a dict
app_pick_recommendations_response_dict = app_pick_recommendations_response_instance.to_dict()
# create an instance of AppPickRecommendationsResponse from a dict
app_pick_recommendations_response_from_dict = AppPickRecommendationsResponse.from_dict(app_pick_recommendations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


