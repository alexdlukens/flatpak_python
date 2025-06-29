# BuildNotificationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** |  | 
**build_id** | **int** |  | 
**build_repo** | **str** |  | 
**diagnostics** | **List[object]** |  | 

## Example

```python
from flathub_python_api.models.build_notification_request import BuildNotificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BuildNotificationRequest from a JSON string
build_notification_request_instance = BuildNotificationRequest.from_json(json)
# print the JSON string representation of the object
print(BuildNotificationRequest.to_json())

# convert the object into a dict
build_notification_request_dict = build_notification_request_instance.to_dict()
# create an instance of BuildNotificationRequest from a dict
build_notification_request_from_dict = BuildNotificationRequest.from_dict(build_notification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


