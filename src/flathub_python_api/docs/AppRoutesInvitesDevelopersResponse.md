# AppRoutesInvitesDevelopersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**developers** | [**List[Developer]**](Developer.md) |  | 
**invites** | [**List[Developer]**](Developer.md) |  | 

## Example

```python
from flathub_python_api.models.app_routes_invites_developers_response import AppRoutesInvitesDevelopersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppRoutesInvitesDevelopersResponse from a JSON string
app_routes_invites_developers_response_instance = AppRoutesInvitesDevelopersResponse.from_json(json)
# print the JSON string representation of the object
print(AppRoutesInvitesDevelopersResponse.to_json())

# convert the object into a dict
app_routes_invites_developers_response_dict = app_routes_invites_developers_response_instance.to_dict()
# create an instance of AppRoutesInvitesDevelopersResponse from a dict
app_routes_invites_developers_response_from_dict = AppRoutesInvitesDevelopersResponse.from_dict(app_routes_invites_developers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


