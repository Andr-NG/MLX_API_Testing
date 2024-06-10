# ScreenResolutions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resolutions** | [**List[ScreenResolution]**](ScreenResolution.md) |  | 

## Example

```python
from pm_api.models.screen_resolutions import ScreenResolutions

# TODO update the JSON string below
json = "{}"
# create an instance of ScreenResolutions from a JSON string
screen_resolutions_instance = ScreenResolutions.from_json(json)
# print the JSON string representation of the object
print(ScreenResolutions.to_json())

# convert the object into a dict
screen_resolutions_dict = screen_resolutions_instance.to_dict()
# create an instance of ScreenResolutions from a dict
screen_resolutions_from_dict = ScreenResolutions.from_dict(screen_resolutions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


