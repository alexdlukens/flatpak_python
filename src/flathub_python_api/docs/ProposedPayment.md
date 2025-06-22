# ProposedPayment

Proposed payment to be made for an application

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** |  | 
**amount** | **int** |  | 

## Example

```python
from openapi_client.models.proposed_payment import ProposedPayment

# TODO update the JSON string below
json = "{}"
# create an instance of ProposedPayment from a JSON string
proposed_payment_instance = ProposedPayment.from_json(json)
# print the JSON string representation of the object
print(ProposedPayment.to_json())

# convert the object into a dict
proposed_payment_dict = proposed_payment_instance.to_dict()
# create an instance of ProposedPayment from a dict
proposed_payment_from_dict = ProposedPayment.from_dict(proposed_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


