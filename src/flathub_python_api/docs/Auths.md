# Auths


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**github** | [**AuthInfo**](AuthInfo.md) |  | [optional] 
**gitlab** | [**AuthInfo**](AuthInfo.md) |  | [optional] 
**gnome** | [**AuthInfo**](AuthInfo.md) |  | [optional] 
**kde** | [**AuthInfo**](AuthInfo.md) |  | [optional] 

## Example

```python
from flathub_python_api.models.auths import Auths

# TODO update the JSON string below
json = "{}"
# create an instance of Auths from a JSON string
auths_instance = Auths.from_json(json)
# print the JSON string representation of the object
print(Auths.to_json())

# convert the object into a dict
auths_dict = auths_instance.to_dict()
# create an instance of Auths from a dict
auths_from_dict = Auths.from_dict(auths_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


