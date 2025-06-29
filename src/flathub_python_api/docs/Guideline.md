# Guideline


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**url** | **str** |  | 
**needed_to_pass_since** | **datetime** |  | 
**category** | **str** |  | 
**read_only** | **bool** |  | [optional] [default to False]

## Example

```python
from flathub_python_api.models.guideline import Guideline

# TODO update the JSON string below
json = "{}"
# create an instance of Guideline from a JSON string
guideline_instance = Guideline.from_json(json)
# print the JSON string representation of the object
print(Guideline.to_json())

# convert the object into a dict
guideline_dict = guideline_instance.to_dict()
# create an instance of Guideline from a dict
guideline_from_dict = Guideline.from_dict(guideline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


