# StripeKeys


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**public_key** | **str** |  | 

## Example

```python
from openapi_client.models.stripe_keys import StripeKeys

# TODO update the JSON string below
json = "{}"
# create an instance of StripeKeys from a JSON string
stripe_keys_instance = StripeKeys.from_json(json)
# print the JSON string representation of the object
print(StripeKeys.to_json())

# convert the object into a dict
stripe_keys_dict = stripe_keys_instance.to_dict()
# create an instance of StripeKeys from a dict
stripe_keys_from_dict = StripeKeys.from_dict(stripe_keys_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


