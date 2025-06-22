# PricingInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recommended_donation** | **int** |  | [optional] 
**minimum_payment** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.pricing_info import PricingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PricingInfo from a JSON string
pricing_info_instance = PricingInfo.from_json(json)
# print the JSON string representation of the object
print(PricingInfo.to_json())

# convert the object into a dict
pricing_info_dict = pricing_info_instance.to_dict()
# create an instance of PricingInfo from a dict
pricing_info_from_dict = PricingInfo.from_dict(pricing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


