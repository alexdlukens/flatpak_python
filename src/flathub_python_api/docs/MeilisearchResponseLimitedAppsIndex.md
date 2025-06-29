# MeilisearchResponseLimitedAppsIndex


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hits** | [**List[AppsIndex]**](AppsIndex.md) |  | 
**query** | **str** |  | 
**processing_time_ms** | **int** |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 
**estimated_total_hits** | **int** |  | 
**facet_distribution** | **Dict[str, Dict[str, int]]** |  | [optional] 
**facet_stats** | **Dict[str, Dict[str, int]]** |  | [optional] 

## Example

```python
from flathub_python_api.models.meilisearch_response_limited_apps_index import MeilisearchResponseLimitedAppsIndex

# TODO update the JSON string below
json = "{}"
# create an instance of MeilisearchResponseLimitedAppsIndex from a JSON string
meilisearch_response_limited_apps_index_instance = MeilisearchResponseLimitedAppsIndex.from_json(json)
# print the JSON string representation of the object
print(MeilisearchResponseLimitedAppsIndex.to_json())

# convert the object into a dict
meilisearch_response_limited_apps_index_dict = meilisearch_response_limited_apps_index_instance.to_dict()
# create an instance of MeilisearchResponseLimitedAppsIndex from a dict
meilisearch_response_limited_apps_index_from_dict = MeilisearchResponseLimitedAppsIndex.from_dict(meilisearch_response_limited_apps_index_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


