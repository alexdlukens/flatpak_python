# AppsIndex


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**keywords** | **List[str]** |  | 
**summary** | **str** |  | 
**description** | **str** |  | 
**id** | **str** |  | 
**type** | **str** |  | 
**translations** | **Dict[str, Dict[str, str]]** |  | [optional] 
**project_license** | **str** |  | 
**is_free_license** | **bool** |  | 
**app_id** | **str** |  | 
**icon** | **str** |  | 
**main_categories** | [**MainCategories**](MainCategories.md) |  | 
**sub_categories** | **List[str]** |  | [optional] 
**developer_name** | **str** |  | 
**verification_verified** | **bool** |  | 
**verification_method** | [**VerificationMethod**](VerificationMethod.md) |  | 
**verification_login_name** | **str** |  | 
**verification_login_provider** | **str** |  | 
**verification_login_is_organization** | **str** |  | 
**verification_website** | **str** |  | 
**verification_timestamp** | **str** |  | 
**runtime** | **str** |  | 
**updated_at** | **int** |  | 
**arches** | **List[str]** |  | 
**added_at** | **int** |  | 
**trending** | **float** |  | [optional] 
**installs_last_month** | **int** |  | [optional] 
**is_mobile_friendly** | **bool** |  | 

## Example

```python
from openapi_client.models.apps_index import AppsIndex

# TODO update the JSON string below
json = "{}"
# create an instance of AppsIndex from a JSON string
apps_index_instance = AppsIndex.from_json(json)
# print the JSON string representation of the object
print(AppsIndex.to_json())

# convert the object into a dict
apps_index_dict = apps_index_instance.to_dict()
# create an instance of AppsIndex from a dict
apps_index_from_dict = AppsIndex.from_dict(apps_index_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


