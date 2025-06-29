# SearchQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** |  | 
**filters** | [**List[Filter]**](Filter.md) |  | [optional] 

## Example

```python
from flathub_python_api.models.search_query import SearchQuery

# TODO update the JSON string below
json = "{}"
# create an instance of SearchQuery from a JSON string
search_query_instance = SearchQuery.from_json(json)
# print the JSON string representation of the object
print(SearchQuery.to_json())

# convert the object into a dict
search_query_dict = search_query_instance.to_dict()
# create an instance of SearchQuery from a dict
search_query_from_dict = SearchQuery.from_dict(search_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


