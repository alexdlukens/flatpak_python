# AppOfTheDay


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** |  | 
**day** | **date** |  | 

## Example

```python
from openapi_client.models.app_of_the_day import AppOfTheDay

# TODO update the JSON string below
json = "{}"
# create an instance of AppOfTheDay from a JSON string
app_of_the_day_instance = AppOfTheDay.from_json(json)
# print the JSON string representation of the object
print(AppOfTheDay.to_json())

# convert the object into a dict
app_of_the_day_dict = app_of_the_day_instance.to_dict()
# create an instance of AppOfTheDay from a dict
app_of_the_day_from_dict = AppOfTheDay.from_dict(app_of_the_day_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


