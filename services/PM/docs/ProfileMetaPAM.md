# ProfileMetaPAM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder_id** | **str** |  | 
**workspace_id** | **str** |  | 

## Example

```python
from pm_api.models.profile_meta_pam import ProfileMetaPAM

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileMetaPAM from a JSON string
profile_meta_pam_instance = ProfileMetaPAM.from_json(json)
# print the JSON string representation of the object
print(ProfileMetaPAM.to_json())

# convert the object into a dict
profile_meta_pam_dict = profile_meta_pam_instance.to_dict()
# create an instance of ProfileMetaPAM from a dict
profile_meta_pam_from_dict = ProfileMetaPAM.from_dict(profile_meta_pam_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


