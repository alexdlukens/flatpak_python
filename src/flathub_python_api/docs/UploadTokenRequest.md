# UploadTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** |  | 
**scopes** | **List[str]** |  | 
**repos** | **List[str]** |  | 

## Example

```python
from openapi_client.models.upload_token_request import UploadTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UploadTokenRequest from a JSON string
upload_token_request_instance = UploadTokenRequest.from_json(json)
# print the JSON string representation of the object
print(UploadTokenRequest.to_json())

# convert the object into a dict
upload_token_request_dict = upload_token_request_instance.to_dict()
# create an instance of UploadTokenRequest from a dict
upload_token_request_from_dict = UploadTokenRequest.from_dict(upload_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


