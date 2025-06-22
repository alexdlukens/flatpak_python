# VendingApplicationInformation

Information about an app, including tax code etc

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** |  | 
**kind** | **str** |  | 
**kind_reason** | **str** |  | 
**foss** | **bool** |  | 
**foss_reason** | **str** |  | 

## Example

```python
from openapi_client.models.vending_application_information import VendingApplicationInformation

# TODO update the JSON string below
json = "{}"
# create an instance of VendingApplicationInformation from a JSON string
vending_application_information_instance = VendingApplicationInformation.from_json(json)
# print the JSON string representation of the object
print(VendingApplicationInformation.to_json())

# convert the object into a dict
vending_application_information_dict = vending_application_information_instance.to_dict()
# create an instance of VendingApplicationInformation from a dict
vending_application_information_from_dict = VendingApplicationInformation.from_dict(vending_application_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


