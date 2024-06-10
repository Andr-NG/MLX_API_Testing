# CreateProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**browser_type** | [**BrowserType**](BrowserType.md) |  | 
**core_version** | **int** |  | [optional] 
**os_type** | **str** |  | 
**times** | **int** |  | [optional] 
**folder_id** | **str** |  | 
**auto_update_core** | **bool** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**notes** | **str** |  | [optional] 
**parameters** | [**ProfileMetaUpdateParams**](ProfileMetaUpdateParams.md) |  | 
**allowed_screen_resolutions** | [**AllowedScreenResolutions**](AllowedScreenResolutions.md) |  | [optional] 

## Example

```python
from pm_api.models.create_profile import CreateProfile

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProfile from a JSON string
create_profile_instance = CreateProfile.from_json(json)
# print the JSON string representation of the object
print(CreateProfile.to_json())

# convert the object into a dict
create_profile_dict = create_profile_instance.to_dict()
# create an instance of CreateProfile from a dict
create_profile_from_dict = CreateProfile.from_dict(create_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


