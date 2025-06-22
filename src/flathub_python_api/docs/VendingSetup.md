# VendingSetup

Configuration for a vended application

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**currency** | **str** |  | 
**appshare** | **int** |  | 
**recommended_donation** | **int** |  | 
**minimum_payment** | **int** |  | 

## Example

```python
from openapi_client.models.vending_setup import VendingSetup

# TODO update the JSON string below
json = "{}"
# create an instance of VendingSetup from a JSON string
vending_setup_instance = VendingSetup.from_json(json)
# print the JSON string representation of the object
print(VendingSetup.to_json())

# convert the object into a dict
vending_setup_dict = vending_setup_instance.to_dict()
# create an instance of VendingSetup from a dict
vending_setup_from_dict = VendingSetup.from_dict(vending_setup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


