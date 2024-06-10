# CloneProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_id** | **str** |  | 
**times** | **int** |  | [optional] 

## Example

```python
from pm_api.models.clone_profile import CloneProfile

# TODO update the JSON string below
json = "{}"
# create an instance of CloneProfile from a JSON string
clone_profile_instance = CloneProfile.from_json(json)
# print the JSON string representation of the object
print(CloneProfile.to_json())

# convert the object into a dict
clone_profile_dict = clone_profile_instance.to_dict()
# create an instance of CloneProfile from a dict
clone_profile_from_dict = CloneProfile.from_dict(clone_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


