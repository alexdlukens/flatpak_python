# OauthLoginResponseSuccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**state** | **str** |  | 

## Example

```python
from flathub_python_api.models.oauth_login_response_success import OauthLoginResponseSuccess

# TODO update the JSON string below
json = "{}"
# create an instance of OauthLoginResponseSuccess from a JSON string
oauth_login_response_success_instance = OauthLoginResponseSuccess.from_json(json)
# print the JSON string representation of the object
print(OauthLoginResponseSuccess.to_json())

# convert the object into a dict
oauth_login_response_success_dict = oauth_login_response_success_instance.to_dict()
# create an instance of OauthLoginResponseSuccess from a dict
oauth_login_response_success_from_dict = OauthLoginResponseSuccess.from_dict(oauth_login_response_success_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


