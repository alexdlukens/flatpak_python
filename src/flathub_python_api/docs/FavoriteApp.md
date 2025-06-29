# FavoriteApp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** |  | 
**created_at** | **datetime** |  | 

## Example

```python
from flathub_python_api.models.favorite_app import FavoriteApp

# TODO update the JSON string below
json = "{}"
# create an instance of FavoriteApp from a JSON string
favorite_app_instance = FavoriteApp.from_json(json)
# print the JSON string representation of the object
print(FavoriteApp.to_json())

# convert the object into a dict
favorite_app_dict = favorite_app_instance.to_dict()
# create an instance of FavoriteApp from a dict
favorite_app_from_dict = FavoriteApp.from_dict(favorite_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


