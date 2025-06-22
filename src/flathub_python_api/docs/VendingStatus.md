# VendingStatus

The status object says whether the user is capable of receiving payments, and also whether or not there are pending onboarding operations to complete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**can_take_payments** | **bool** |  | 
**needs_attention** | **bool** |  | 
**details_submitted** | **bool** |  | 

## Example

```python
from openapi_client.models.vending_status import VendingStatus

# TODO update the JSON string below
json = "{}"
# create an instance of VendingStatus from a JSON string
vending_status_instance = VendingStatus.from_json(json)
# print the JSON string representation of the object
print(VendingStatus.to_json())

# convert the object into a dict
vending_status_dict = vending_status_instance.to_dict()
# create an instance of VendingStatus from a dict
vending_status_from_dict = VendingStatus.from_dict(vending_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


