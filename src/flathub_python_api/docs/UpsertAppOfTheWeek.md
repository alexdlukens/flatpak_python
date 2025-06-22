# UpsertAppOfTheWeek


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** |  | 
**week_number** | **int** |  | 
**year** | **int** |  | 
**position** | **int** |  | 

## Example

```python
from openapi_client.models.upsert_app_of_the_week import UpsertAppOfTheWeek

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertAppOfTheWeek from a JSON string
upsert_app_of_the_week_instance = UpsertAppOfTheWeek.from_json(json)
# print the JSON string representation of the object
print(UpsertAppOfTheWeek.to_json())

# convert the object into a dict
upsert_app_of_the_week_dict = upsert_app_of_the_week_instance.to_dict()
# create an instance of UpsertAppOfTheWeek from a dict
upsert_app_of_the_week_from_dict = UpsertAppOfTheWeek.from_dict(upsert_app_of_the_week_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


