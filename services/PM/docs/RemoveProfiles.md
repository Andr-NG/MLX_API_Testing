# RemoveProfiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** |  | 
**permanently** | **bool** |  | 

## Example

```python
from pm_api.models.remove_profiles import RemoveProfiles

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveProfiles from a JSON string
remove_profiles_instance = RemoveProfiles.from_json(json)
# print the JSON string representation of the object
print(RemoveProfiles.to_json())

# convert the object into a dict
remove_profiles_dict = remove_profiles_instance.to_dict()
# create an instance of RemoveProfiles from a dict
remove_profiles_from_dict = RemoveProfiles.from_dict(remove_profiles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


