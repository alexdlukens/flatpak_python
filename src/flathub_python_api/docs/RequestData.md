# RequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keys** | [**Dict[str, KeysValue]**](KeysValue.md) |  | 
**current_values** | [**Dict[str, KeysValue]**](KeysValue.md) |  | 

## Example

```python
from flathub_python_api.models.request_data import RequestData

# TODO update the JSON string below
json = "{}"
# create an instance of RequestData from a JSON string
request_data_instance = RequestData.from_json(json)
# print the JSON string representation of the object
print(RequestData.to_json())

# convert the object into a dict
request_data_dict = request_data_instance.to_dict()
# create an instance of RequestData from a dict
request_data_from_dict = RequestData.from_dict(request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


