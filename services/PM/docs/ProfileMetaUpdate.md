# ProfileMetaUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**notes** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**parameters** | [**ProfileMetaUpdateParams**](ProfileMetaUpdateParams.md) |  | 

## Example

```python
from pm_api.models.profile_meta_update import ProfileMetaUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileMetaUpdate from a JSON string
profile_meta_update_instance = ProfileMetaUpdate.from_json(json)
# print the JSON string representation of the object
print(ProfileMetaUpdate.to_json())

# convert the object into a dict
profile_meta_update_dict = profile_meta_update_instance.to_dict()
# create an instance of ProfileMetaUpdate from a dict
profile_meta_update_from_dict = ProfileMetaUpdate.from_dict(profile_meta_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


