# WebsiteVerificationToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** |  | 
**token** | **str** |  | 

## Example

```python
from openapi_client.models.website_verification_token import WebsiteVerificationToken

# TODO update the JSON string below
json = "{}"
# create an instance of WebsiteVerificationToken from a JSON string
website_verification_token_instance = WebsiteVerificationToken.from_json(json)
# print the JSON string representation of the object
print(WebsiteVerificationToken.to_json())

# convert the object into a dict
website_verification_token_dict = website_verification_token_instance.to_dict()
# create an instance of WebsiteVerificationToken from a dict
website_verification_token_from_dict = WebsiteVerificationToken.from_dict(website_verification_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


