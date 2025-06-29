# StatsResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**totals** | **Dict[str, int]** |  | 
**countries** | **Dict[str, int]** |  | 
**downloads_per_day** | **Dict[str, int]** |  | 
**updates_per_day** | **Dict[str, int]** |  | 
**delta_downloads_per_day** | **Dict[str, int]** |  | 
**category_totals** | [**List[StatsResultCategoryTotals]**](StatsResultCategoryTotals.md) |  | 

## Example

```python
from flathub_python_api.models.stats_result import StatsResult

# TODO update the JSON string below
json = "{}"
# create an instance of StatsResult from a JSON string
stats_result_instance = StatsResult.from_json(json)
# print the JSON string representation of the object
print(StatsResult.to_json())

# convert the object into a dict
stats_result_dict = stats_result_instance.to_dict()
# create an instance of StatsResult from a dict
stats_result_from_dict = StatsResult.from_dict(stats_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


