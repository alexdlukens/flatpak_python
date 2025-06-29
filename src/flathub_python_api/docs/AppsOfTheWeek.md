# AppsOfTheWeek


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apps** | [**List[AppOfTheWeek]**](AppOfTheWeek.md) |  | 

## Example

```python
from flathub_python_api.models.apps_of_the_week import AppsOfTheWeek

# TODO update the JSON string below
json = "{}"
# create an instance of AppsOfTheWeek from a JSON string
apps_of_the_week_instance = AppsOfTheWeek.from_json(json)
# print the JSON string representation of the object
print(AppsOfTheWeek.to_json())

# convert the object into a dict
apps_of_the_week_dict = apps_of_the_week_instance.to_dict()
# create an instance of AppsOfTheWeek from a dict
apps_of_the_week_from_dict = AppsOfTheWeek.from_dict(apps_of_the_week_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


