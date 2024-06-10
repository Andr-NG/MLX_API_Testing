# ReadyProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**is_local** | **bool** |  | 
**core** | [**ReadyProfileCore**](ReadyProfileCore.md) |  | 
**flags** | [**ProfileMetaFlags**](ProfileMetaFlags.md) |  | 
**fingerprint** | [**FingerprintData**](FingerprintData.md) |  | 
**custom_start_urls** | **List[str]** |  | [optional] 
**custom_dns** | **str** |  | [optional] 
**browser_extensions** | [**List[BrowserExtension]**](BrowserExtension.md) |  | [optional] 

## Example

```python
from pm_api.models.ready_profile import ReadyProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ReadyProfile from a JSON string
ready_profile_instance = ReadyProfile.from_json(json)
# print the JSON string representation of the object
print(ReadyProfile.to_json())

# convert the object into a dict
ready_profile_dict = ready_profile_instance.to_dict()
# create an instance of ReadyProfile from a dict
ready_profile_from_dict = ReadyProfile.from_dict(ready_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


