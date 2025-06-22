# AvailableMethods


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**methods** | [**List[AvailableMethod]**](AvailableMethod.md) |  | [optional] 
**detail** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.available_methods import AvailableMethods

# TODO update the JSON string below
json = "{}"
# create an instance of AvailableMethods from a JSON string
available_methods_instance = AvailableMethods.from_json(json)
# print the JSON string representation of the object
print(AvailableMethods.to_json())

# convert the object into a dict
available_methods_dict = available_methods_instance.to_dict()
# create an instance of AvailableMethods from a dict
available_methods_from_dict = AvailableMethods.from_dict(available_methods_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


