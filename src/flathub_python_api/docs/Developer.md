# Developer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**is_self** | **bool** |  | 
**name** | **str** |  | 
**is_primary** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.developer import Developer

# TODO update the JSON string below
json = "{}"
# create an instance of Developer from a JSON string
developer_instance = Developer.from_json(json)
# print the JSON string representation of the object
print(Developer.to_json())

# convert the object into a dict
developer_dict = developer_instance.to_dict()
# create an instance of Developer from a dict
developer_from_dict = Developer.from_dict(developer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


