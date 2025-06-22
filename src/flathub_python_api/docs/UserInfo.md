# UserInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayname** | **str** |  | [optional] 
**dev_flatpaks** | **List[str]** |  | [optional] [default to []]
**permissions** | [**List[Permission]**](Permission.md) |  | [optional] [default to []]
**owned_flatpaks** | **List[str]** |  | [optional] [default to []]
**invited_flatpaks** | **List[str]** |  | [optional] [default to []]
**invite_code** | **str** |  | 
**accepted_publisher_agreement_at** | **datetime** |  | 
**default_account** | [**AuthInfo**](AuthInfo.md) |  | 
**auths** | [**Auths**](Auths.md) |  | 

## Example

```python
from openapi_client.models.user_info import UserInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UserInfo from a JSON string
user_info_instance = UserInfo.from_json(json)
# print the JSON string representation of the object
print(UserInfo.to_json())

# convert the object into a dict
user_info_dict = user_info_instance.to_dict()
# create an instance of UserInfo from a dict
user_info_from_dict = UserInfo.from_dict(user_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


