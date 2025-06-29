# VendingRedirect

Any redirect the vending system needs to create will be returned like this.  Status will be \"ok\" otherwise you cannot rely on target_url and instead something look for like error.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**target_url** | **str** |  | 

## Example

```python
from flathub_python_api.models.vending_redirect import VendingRedirect

# TODO update the JSON string below
json = "{}"
# create an instance of VendingRedirect from a JSON string
vending_redirect_instance = VendingRedirect.from_json(json)
# print the JSON string representation of the object
print(VendingRedirect.to_json())

# convert the object into a dict
vending_redirect_dict = vending_redirect_instance.to_dict()
# create an instance of VendingRedirect from a dict
vending_redirect_from_dict = VendingRedirect.from_dict(vending_redirect_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


