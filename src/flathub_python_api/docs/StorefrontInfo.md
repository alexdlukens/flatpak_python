# StorefrontInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verification** | [**VerificationStatus**](VerificationStatus.md) |  | [optional] 
**pricing** | [**PricingInfo**](PricingInfo.md) |  | [optional] 
**is_free_software** | **bool** |  | [optional] [default to False]

## Example

```python
from flathub_python_api.models.storefront_info import StorefrontInfo

# TODO update the JSON string below
json = "{}"
# create an instance of StorefrontInfo from a JSON string
storefront_info_instance = StorefrontInfo.from_json(json)
# print the JSON string representation of the object
print(StorefrontInfo.to_json())

# convert the object into a dict
storefront_info_dict = storefront_info_instance.to_dict()
# create an instance of StorefrontInfo from a dict
storefront_info_from_dict = StorefrontInfo.from_dict(storefront_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


