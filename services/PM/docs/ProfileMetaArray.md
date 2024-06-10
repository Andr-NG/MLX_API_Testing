# ProfileMetaArray


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profiles** | [**List[ProfileMeta]**](ProfileMeta.md) |  | 

## Example

```python
from pm_api.models.profile_meta_array import ProfileMetaArray

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileMetaArray from a JSON string
profile_meta_array_instance = ProfileMetaArray.from_json(json)
# print the JSON string representation of the object
print(ProfileMetaArray.to_json())

# convert the object into a dict
profile_meta_array_dict = profile_meta_array_instance.to_dict()
# create an instance of ProfileMetaArray from a dict
profile_meta_array_from_dict = ProfileMetaArray.from_dict(profile_meta_array_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


