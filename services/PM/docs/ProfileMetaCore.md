# ProfileMetaCore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**browser_type** | [**BrowserType**](BrowserType.md) |  | 
**os_type** | **str** |  | 
**core_version** | **int** |  | 

## Example

```python
from pm_api.models.profile_meta_core import ProfileMetaCore

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileMetaCore from a JSON string
profile_meta_core_instance = ProfileMetaCore.from_json(json)
# print the JSON string representation of the object
print(ProfileMetaCore.to_json())

# convert the object into a dict
profile_meta_core_dict = profile_meta_core_instance.to_dict()
# create an instance of ProfileMetaCore from a dict
profile_meta_core_from_dict = ProfileMetaCore.from_dict(profile_meta_core_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


