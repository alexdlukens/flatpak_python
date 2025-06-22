# AppSearchDevelopersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**developers** | **List[str]** |  | 
**total** | **int** |  | 
**page** | **int** |  | 
**per_page** | **int** |  | 

## Example

```python
from openapi_client.models.app_search_developers_response import AppSearchDevelopersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppSearchDevelopersResponse from a JSON string
app_search_developers_response_instance = AppSearchDevelopersResponse.from_json(json)
# print the JSON string representation of the object
print(AppSearchDevelopersResponse.to_json())

# convert the object into a dict
app_search_developers_response_dict = app_search_developers_response_instance.to_dict()
# create an instance of AppSearchDevelopersResponse from a dict
app_search_developers_response_from_dict = AppSearchDevelopersResponse.from_dict(app_search_developers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


