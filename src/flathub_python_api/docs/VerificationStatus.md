# VerificationStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verified** | **bool** |  | 
**timestamp** | **str** |  | [optional] 
**method** | [**VerificationMethod**](VerificationMethod.md) |  | [optional] 
**website** | **str** |  | [optional] 
**login_provider** | [**LoginProvider**](LoginProvider.md) |  | [optional] 
**login_name** | **str** |  | [optional] 
**login_is_organization** | **bool** |  | [optional] 
**detail** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.verification_status import VerificationStatus

# TODO update the JSON string below
json = "{}"
# create an instance of VerificationStatus from a JSON string
verification_status_instance = VerificationStatus.from_json(json)
# print the JSON string representation of the object
print(VerificationStatus.to_json())

# convert the object into a dict
verification_status_dict = verification_status_instance.to_dict()
# create an instance of VerificationStatus from a dict
verification_status_from_dict = VerificationStatus.from_dict(verification_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


