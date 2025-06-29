# InviteStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_pending** | **bool** |  | 
**is_direct_upload_app** | **bool** |  | [optional] [default to True]

## Example

```python
from flathub_python_api.models.invite_status import InviteStatus

# TODO update the JSON string below
json = "{}"
# create an instance of InviteStatus from a JSON string
invite_status_instance = InviteStatus.from_json(json)
# print the JSON string representation of the object
print(InviteStatus.to_json())

# convert the object into a dict
invite_status_dict = invite_status_instance.to_dict()
# create an instance of InviteStatus from a dict
invite_status_from_dict = InviteStatus.from_dict(invite_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


