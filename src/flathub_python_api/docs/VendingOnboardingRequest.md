# VendingOnboardingRequest

A request to begin/continue the onboarding process for a user.  Any onboarding operation request a 'return' URL which we will tell Stripe to send us back to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**return_url** | **str** |  | 

## Example

```python
from openapi_client.models.vending_onboarding_request import VendingOnboardingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VendingOnboardingRequest from a JSON string
vending_onboarding_request_instance = VendingOnboardingRequest.from_json(json)
# print the JSON string representation of the object
print(VendingOnboardingRequest.to_json())

# convert the object into a dict
vending_onboarding_request_dict = vending_onboarding_request_instance.to_dict()
# create an instance of VendingOnboardingRequest from a dict
vending_onboarding_request_from_dict = VendingOnboardingRequest.from_dict(vending_onboarding_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


