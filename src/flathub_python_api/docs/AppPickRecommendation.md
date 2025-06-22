# AppPickRecommendation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** |  | 
**number_of_times_app_of_the_week** | **int** |  | 
**last_time_app_of_the_week** | **date** |  | 
**number_of_times_app_of_the_day** | **int** |  | 
**last_time_app_of_the_day** | **date** |  | 

## Example

```python
from openapi_client.models.app_pick_recommendation import AppPickRecommendation

# TODO update the JSON string below
json = "{}"
# create an instance of AppPickRecommendation from a JSON string
app_pick_recommendation_instance = AppPickRecommendation.from_json(json)
# print the JSON string representation of the object
print(AppPickRecommendation.to_json())

# convert the object into a dict
app_pick_recommendation_dict = app_pick_recommendation_instance.to_dict()
# create an instance of AppPickRecommendation from a dict
app_pick_recommendation_from_dict = AppPickRecommendation.from_dict(app_pick_recommendation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


