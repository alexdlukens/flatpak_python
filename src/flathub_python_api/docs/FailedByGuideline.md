# FailedByGuideline


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guideline_id** | **str** |  | 
**not_passed** | **int** |  | 

## Example

```python
from flathub_python_api.models.failed_by_guideline import FailedByGuideline

# TODO update the JSON string below
json = "{}"
# create an instance of FailedByGuideline from a JSON string
failed_by_guideline_instance = FailedByGuideline.from_json(json)
# print the JSON string representation of the object
print(FailedByGuideline.to_json())

# convert the object into a dict
failed_by_guideline_dict = failed_by_guideline_instance.to_dict()
# create an instance of FailedByGuideline from a dict
failed_by_guideline_from_dict = FailedByGuideline.from_dict(failed_by_guideline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


