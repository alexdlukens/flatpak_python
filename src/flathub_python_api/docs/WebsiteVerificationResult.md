# WebsiteVerificationResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verified** | **bool** |  | 
**detail** | [**ErrorDetail**](ErrorDetail.md) |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.website_verification_result import WebsiteVerificationResult

# TODO update the JSON string below
json = "{}"
# create an instance of WebsiteVerificationResult from a JSON string
website_verification_result_instance = WebsiteVerificationResult.from_json(json)
# print the JSON string representation of the object
print(WebsiteVerificationResult.to_json())

# convert the object into a dict
website_verification_result_dict = website_verification_result_instance.to_dict()
# create an instance of WebsiteVerificationResult from a dict
website_verification_result_from_dict = WebsiteVerificationResult.from_dict(website_verification_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


