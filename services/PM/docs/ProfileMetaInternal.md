# ProfileMetaInternal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**created_at** | **datetime** |  | 
**last_update_at** | **datetime** |  | 
**removed_at** | **datetime** |  | 
**removed_by** | **str** |  | 

## Example

```python
from pm_api.models.profile_meta_internal import ProfileMetaInternal

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileMetaInternal from a JSON string
profile_meta_internal_instance = ProfileMetaInternal.from_json(json)
# print the JSON string representation of the object
print(ProfileMetaInternal.to_json())

# convert the object into a dict
profile_meta_internal_dict = profile_meta_internal_instance.to_dict()
# create an instance of ProfileMetaInternal from a dict
profile_meta_internal_from_dict = ProfileMetaInternal.from_dict(profile_meta_internal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


