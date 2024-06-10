# MoveProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** |  | 
**dest_folder_id** | **str** |  | 

## Example

```python
from pm_api.models.move_profile import MoveProfile

# TODO update the JSON string below
json = "{}"
# create an instance of MoveProfile from a JSON string
move_profile_instance = MoveProfile.from_json(json)
# print the JSON string representation of the object
print(MoveProfile.to_json())

# convert the object into a dict
move_profile_dict = move_profile_instance.to_dict()
# create an instance of MoveProfile from a dict
move_profile_from_dict = MoveProfile.from_dict(move_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


