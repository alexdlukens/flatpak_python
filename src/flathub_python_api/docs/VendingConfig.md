# VendingConfig

Global vending environment configuration values

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**platforms** | [**Dict[str, Platform]**](Platform.md) |  | 
**fee_fixed_cost** | **int** |  | 
**fee_cost_percent** | **int** |  | 
**fee_prefer_percent** | **int** |  | 

## Example

```python
from openapi_client.models.vending_config import VendingConfig

# TODO update the JSON string below
json = "{}"
# create an instance of VendingConfig from a JSON string
vending_config_instance = VendingConfig.from_json(json)
# print the JSON string representation of the object
print(VendingConfig.to_json())

# convert the object into a dict
vending_config_dict = vending_config_instance.to_dict()
# create an instance of VendingConfig from a dict
vending_config_from_dict = VendingConfig.from_dict(vending_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


