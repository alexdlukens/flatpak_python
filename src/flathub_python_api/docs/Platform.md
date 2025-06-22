# Platform

A platform is an expression of dependencies which an application may have. Applications nominally express a single platform key for themselves, or none at all if they do not need one.  But platforms may depend on one another.  If no platform is specified for an application, it's worth getting the default platform and using that.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**depends** | **str** |  | [optional] 
**aliases** | **List[str]** |  | 
**keep** | **int** |  | 
**stripe_account** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.platform import Platform

# TODO update the JSON string below
json = "{}"
# create an instance of Platform from a JSON string
platform_instance = Platform.from_json(json)
# print the JSON string representation of the object
print(Platform.to_json())

# convert the object into a dict
platform_dict = platform_instance.to_dict()
# create an instance of Platform from a dict
platform_from_dict = Platform.from_dict(platform_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


