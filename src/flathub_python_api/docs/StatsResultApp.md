# StatsResultApp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**installs_total** | **int** |  | 
**installs_per_day** | **Dict[str, int]** |  | 
**installs_per_country** | **Dict[str, int]** |  | 
**installs_last_month** | **int** |  | 
**installs_last_7_days** | **int** |  | 
**id** | **str** |  | 

## Example

```python
from flathub_python_api.models.stats_result_app import StatsResultApp

# TODO update the JSON string below
json = "{}"
# create an instance of StatsResultApp from a JSON string
stats_result_app_instance = StatsResultApp.from_json(json)
# print the JSON string representation of the object
print(StatsResultApp.to_json())

# convert the object into a dict
stats_result_app_dict = stats_result_app_instance.to_dict()
# create an instance of StatsResultApp from a dict
stats_result_app_from_dict = StatsResultApp.from_dict(stats_result_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


