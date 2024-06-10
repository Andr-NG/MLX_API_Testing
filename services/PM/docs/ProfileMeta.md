# ProfileMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder_id** | **str** |  | 
**workspace_id** | **str** |  | 
**status** | **str** |  | 
**created_at** | **datetime** |  | 
**last_update_at** | **datetime** |  | 
**removed_at** | **datetime** |  | 
**removed_by** | **str** |  | 
**browser_type** | [**BrowserType**](BrowserType.md) |  | 
**os_type** | **str** |  | 
**core_version** | **int** |  | 
**name** | **str** |  | 
**notes** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**parameters** | [**ProfileMetaUpdateParams**](ProfileMetaUpdateParams.md) |  | 
**id** | **str** |  | 

## Example

```python
from pm_api.models.profile_meta import ProfileMeta

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileMeta from a JSON string
profile_meta_instance = ProfileMeta.from_json(json)
# print the JSON string representation of the object
print(ProfileMeta.to_json())

# convert the object into a dict
profile_meta_dict = profile_meta_instance.to_dict()
# create an instance of ProfileMeta from a dict
profile_meta_from_dict = ProfileMeta.from_dict(profile_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


