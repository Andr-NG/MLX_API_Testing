# PartialUpdateProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**profile_id** | **str** |  | 
**auto_update_core** | **bool** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**notes** | **str** |  | [optional] 
**custom_start_urls** | **List[str]** |  | [optional] 
**custom_dns** | **str** |  | [optional] 
**proxy** | [**Proxy**](Proxy.md) |  | [optional] 
**parameters** | [**PartialProfileMetaUpdateParams**](PartialProfileMetaUpdateParams.md) |  | [optional] 

## Example

```python
from pm_api.models.partial_update_profile import PartialUpdateProfile

# TODO update the JSON string below
json = "{}"
# create an instance of PartialUpdateProfile from a JSON string
partial_update_profile_instance = PartialUpdateProfile.from_json(json)
# print the JSON string representation of the object
print(PartialUpdateProfile.to_json())

# convert the object into a dict
partial_update_profile_dict = partial_update_profile_instance.to_dict()
# create an instance of PartialUpdateProfile from a dict
partial_update_profile_from_dict = PartialUpdateProfile.from_dict(partial_update_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


