# AllowedScreenResolutions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_height** | **int** |  | 
**min_height** | **int** |  | 
**max_width** | **int** |  | 
**min_width** | **int** |  | 

## Example

```python
from pm_api.models.allowed_screen_resolutions import AllowedScreenResolutions

# TODO update the JSON string below
json = "{}"
# create an instance of AllowedScreenResolutions from a JSON string
allowed_screen_resolutions_instance = AllowedScreenResolutions.from_json(json)
# print the JSON string representation of the object
print(AllowedScreenResolutions.to_json())

# convert the object into a dict
allowed_screen_resolutions_dict = allowed_screen_resolutions_instance.to_dict()
# create an instance of AllowedScreenResolutions from a dict
allowed_screen_resolutions_from_dict = AllowedScreenResolutions.from_dict(allowed_screen_resolutions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


