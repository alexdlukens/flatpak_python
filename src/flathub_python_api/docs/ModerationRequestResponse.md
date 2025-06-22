# ModerationRequestResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**app_id** | **str** |  | 
**created_at** | **datetime** |  | 
**build_id** | **int** |  | 
**job_id** | **int** |  | 
**is_outdated** | **bool** |  | 
**request_type** | [**ModerationRequestType**](ModerationRequestType.md) |  | 
**request_data** | [**RequestData**](RequestData.md) |  | [optional] 
**is_new_submission** | **bool** |  | 
**handled_by** | **str** |  | [optional] 
**handled_at** | **datetime** |  | [optional] 
**is_approved** | **bool** |  | [optional] 
**comment** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.moderation_request_response import ModerationRequestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModerationRequestResponse from a JSON string
moderation_request_response_instance = ModerationRequestResponse.from_json(json)
# print the JSON string representation of the object
print(ModerationRequestResponse.to_json())

# convert the object into a dict
moderation_request_response_dict = moderation_request_response_instance.to_dict()
# create an instance of ModerationRequestResponse from a dict
moderation_request_response_from_dict = ModerationRequestResponse.from_dict(moderation_request_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


