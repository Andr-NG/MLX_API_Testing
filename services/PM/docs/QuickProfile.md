# QuickProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**browser_type** | [**BrowserType**](BrowserType.md) |  | 
**core_version** | **int** |  | [optional] 
**os_type** | **str** |  | 
**proxy** | [**Proxy**](Proxy.md) |  | [optional] 
**parameters** | [**QuickProfileMetaParams**](QuickProfileMetaParams.md) |  | 
**allowed_screen_resolutions** | [**AllowedScreenResolutions**](AllowedScreenResolutions.md) |  | [optional] 

## Example

```python
from pm_api.models.quick_profile import QuickProfile

# TODO update the JSON string below
json = "{}"
# create an instance of QuickProfile from a JSON string
quick_profile_instance = QuickProfile.from_json(json)
# print the JSON string representation of the object
print(QuickProfile.to_json())

# convert the object into a dict
quick_profile_dict = quick_profile_instance.to_dict()
# create an instance of QuickProfile from a dict
quick_profile_from_dict = QuickProfile.from_dict(quick_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


