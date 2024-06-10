# ReadyProfileCore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**browser** | [**ProfileMetaCore**](ProfileMetaCore.md) |  | 
**proxy** | [**Proxy**](Proxy.md) |  | [optional] 
**browser_version** | **str** |  | 
**abort_start_if_proxy_leaks** | **bool** |  | [optional] 
**timezone_fill_based_on_external_ip** | **bool** |  | [optional] 
**geolocation_fill_based_on_external_ip** | **bool** |  | [optional] 
**auto_update_core** | **bool** |  | 

## Example

```python
from pm_api.models.ready_profile_core import ReadyProfileCore

# TODO update the JSON string below
json = "{}"
# create an instance of ReadyProfileCore from a JSON string
ready_profile_core_instance = ReadyProfileCore.from_json(json)
# print the JSON string representation of the object
print(ReadyProfileCore.to_json())

# convert the object into a dict
ready_profile_core_dict = ready_profile_core_instance.to_dict()
# create an instance of ReadyProfileCore from a dict
ready_profile_core_from_dict = ReadyProfileCore.from_dict(ready_profile_core_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


