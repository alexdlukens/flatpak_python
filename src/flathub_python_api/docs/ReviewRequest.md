# ReviewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build_id** | **int** |  | 
**job_id** | **int** |  | 

## Example

```python
from openapi_client.models.review_request import ReviewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewRequest from a JSON string
review_request_instance = ReviewRequest.from_json(json)
# print the JSON string representation of the object
print(ReviewRequest.to_json())

# convert the object into a dict
review_request_dict = review_request_instance.to_dict()
# create an instance of ReviewRequest from a dict
review_request_from_dict = ReviewRequest.from_dict(review_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


