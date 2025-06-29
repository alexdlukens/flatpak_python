# CheckPurchasesResponseSuccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] [default to 'ok']

## Example

```python
from flathub_python_api.models.check_purchases_response_success import CheckPurchasesResponseSuccess

# TODO update the JSON string below
json = "{}"
# create an instance of CheckPurchasesResponseSuccess from a JSON string
check_purchases_response_success_instance = CheckPurchasesResponseSuccess.from_json(json)
# print the JSON string representation of the object
print(CheckPurchasesResponseSuccess.to_json())

# convert the object into a dict
check_purchases_response_success_dict = check_purchases_response_success_instance.to_dict()
# create an instance of CheckPurchasesResponseSuccess from a dict
check_purchases_response_success_from_dict = CheckPurchasesResponseSuccess.from_dict(check_purchases_response_success_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


