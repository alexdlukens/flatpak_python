# GetDownloadTokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | 
**update_token** | **str** |  | 

## Example

```python
from openapi_client.models.get_download_token_response import GetDownloadTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDownloadTokenResponse from a JSON string
get_download_token_response_instance = GetDownloadTokenResponse.from_json(json)
# print the JSON string representation of the object
print(GetDownloadTokenResponse.to_json())

# convert the object into a dict
get_download_token_response_dict = get_download_token_response_instance.to_dict()
# create an instance of GetDownloadTokenResponse from a dict
get_download_token_response_from_dict = GetDownloadTokenResponse.from_dict(get_download_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


