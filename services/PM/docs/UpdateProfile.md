# UpdateProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**profile_id** | **str** |  | 
**auto_update_core** | **bool** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**notes** | **str** |  | [optional] 
**parameters** | [**ProfileMetaUpdateParams**](ProfileMetaUpdateParams.md) |  | 

## Example

```python
from pm_api.models.update_profile import UpdateProfile

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProfile from a JSON string
update_profile_instance = UpdateProfile.from_json(json)
# print the JSON string representation of the object
print(UpdateProfile.to_json())

# convert the object into a dict
update_profile_dict = update_profile_instance.to_dict()
# create an instance of UpdateProfile from a dict
update_profile_from_dict = UpdateProfile.from_dict(update_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


