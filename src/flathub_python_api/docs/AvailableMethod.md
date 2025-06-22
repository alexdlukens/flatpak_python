# AvailableMethod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | [**AvailableMethodType**](AvailableMethodType.md) |  | 
**website** | **str** |  | [optional] 
**website_token** | **str** |  | [optional] 
**login_provider** | [**LoginProvider**](LoginProvider.md) |  | [optional] 
**login_name** | **str** |  | [optional] 
**login_is_organization** | **bool** |  | [optional] 
**login_status** | [**AvailableLoginMethodStatus**](AvailableLoginMethodStatus.md) |  | [optional] 

## Example

```python
from openapi_client.models.available_method import AvailableMethod

# TODO update the JSON string below
json = "{}"
# create an instance of AvailableMethod from a JSON string
available_method_instance = AvailableMethod.from_json(json)
# print the JSON string representation of the object
print(AvailableMethod.to_json())

# convert the object into a dict
available_method_dict = available_method_instance.to_dict()
# create an instance of AvailableMethod from a dict
available_method_from_dict = AvailableMethod.from_dict(available_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


