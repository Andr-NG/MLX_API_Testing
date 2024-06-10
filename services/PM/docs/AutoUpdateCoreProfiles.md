# AutoUpdateCoreProfiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** |  | 
**auto_update_core** | **bool** |  | 

## Example

```python
from pm_api.models.auto_update_core_profiles import AutoUpdateCoreProfiles

# TODO update the JSON string below
json = "{}"
# create an instance of AutoUpdateCoreProfiles from a JSON string
auto_update_core_profiles_instance = AutoUpdateCoreProfiles.from_json(json)
# print the JSON string representation of the object
print(AutoUpdateCoreProfiles.to_json())

# convert the object into a dict
auto_update_core_profiles_dict = auto_update_core_profiles_instance.to_dict()
# create an instance of AutoUpdateCoreProfiles from a dict
auto_update_core_profiles_from_dict = AutoUpdateCoreProfiles.from_dict(auto_update_core_profiles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


