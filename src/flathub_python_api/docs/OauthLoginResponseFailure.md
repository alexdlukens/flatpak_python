# OauthLoginResponseFailure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** |  | 
**error** | **str** |  | 
**error_description** | **str** |  | [optional] 
**error_uri** | **str** |  | [optional] 

## Example

```python
from flathub_python_api.models.oauth_login_response_failure import OauthLoginResponseFailure

# TODO update the JSON string below
json = "{}"
# create an instance of OauthLoginResponseFailure from a JSON string
oauth_login_response_failure_instance = OauthLoginResponseFailure.from_json(json)
# print the JSON string representation of the object
print(OauthLoginResponseFailure.to_json())

# convert the object into a dict
oauth_login_response_failure_dict = oauth_login_response_failure_instance.to_dict()
# create an instance of OauthLoginResponseFailure from a dict
oauth_login_response_failure_from_dict = OauthLoginResponseFailure.from_dict(oauth_login_response_failure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


