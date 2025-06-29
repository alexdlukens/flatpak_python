# VendingSetupRequest

Configuration for a vended application

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** |  | 
**appshare** | **int** |  | 
**recommended_donation** | **int** |  | 
**minimum_payment** | **int** |  | 

## Example

```python
from flathub_python_api.models.vending_setup_request import VendingSetupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VendingSetupRequest from a JSON string
vending_setup_request_instance = VendingSetupRequest.from_json(json)
# print the JSON string representation of the object
print(VendingSetupRequest.to_json())

# convert the object into a dict
vending_setup_request_dict = vending_setup_request_instance.to_dict()
# create an instance of VendingSetupRequest from a dict
vending_setup_request_from_dict = VendingSetupRequest.from_dict(vending_setup_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


