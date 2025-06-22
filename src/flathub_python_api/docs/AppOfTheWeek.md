# AppOfTheWeek


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** |  | 
**position** | **int** |  | 
**is_fullscreen** | **bool** |  | 

## Example

```python
from openapi_client.models.app_of_the_week import AppOfTheWeek

# TODO update the JSON string below
json = "{}"
# create an instance of AppOfTheWeek from a JSON string
app_of_the_week_instance = AppOfTheWeek.from_json(json)
# print the JSON string representation of the object
print(AppOfTheWeek.to_json())

# convert the object into a dict
app_of_the_week_dict = app_of_the_week_instance.to_dict()
# create an instance of AppOfTheWeek from a dict
app_of_the_week_from_dict = AppOfTheWeek.from_dict(app_of_the_week_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


