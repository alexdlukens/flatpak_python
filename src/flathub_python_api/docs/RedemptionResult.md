# RedemptionResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**reason** | **str** |  | 

## Example

```python
from flathub_python_api.models.redemption_result import RedemptionResult

# TODO update the JSON string below
json = "{}"
# create an instance of RedemptionResult from a JSON string
redemption_result_instance = RedemptionResult.from_json(json)
# print the JSON string representation of the object
print(RedemptionResult.to_json())

# convert the object into a dict
redemption_result_dict = redemption_result_instance.to_dict()
# create an instance of RedemptionResult from a dict
redemption_result_from_dict = RedemptionResult.from_dict(redemption_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


