# MeilisearchResponseAppsIndex


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hits** | [**List[AppsIndex]**](AppsIndex.md) |  | 
**query** | **str** |  | 
**processing_time_ms** | **int** |  | 
**hits_per_page** | **int** |  | 
**page** | **int** |  | 
**total_pages** | **int** |  | 
**total_hits** | **int** |  | 

## Example

```python
from flathub_python_api.models.meilisearch_response_apps_index import MeilisearchResponseAppsIndex

# TODO update the JSON string below
json = "{}"
# create an instance of MeilisearchResponseAppsIndex from a JSON string
meilisearch_response_apps_index_instance = MeilisearchResponseAppsIndex.from_json(json)
# print the JSON string representation of the object
print(MeilisearchResponseAppsIndex.to_json())

# convert the object into a dict
meilisearch_response_apps_index_dict = meilisearch_response_apps_index_instance.to_dict()
# create an instance of MeilisearchResponseAppsIndex from a dict
meilisearch_response_apps_index_from_dict = MeilisearchResponseAppsIndex.from_dict(meilisearch_response_apps_index_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


