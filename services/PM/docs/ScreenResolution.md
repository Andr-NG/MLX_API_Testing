# ScreenResolution


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**width** | **int** |  | 
**height** | **int** |  | 

## Example

```python
from pm_api.models.screen_resolution import ScreenResolution

# TODO update the JSON string below
json = "{}"
# create an instance of ScreenResolution from a JSON string
screen_resolution_instance = ScreenResolution.from_json(json)
# print the JSON string representation of the object
print(ScreenResolution.to_json())

# convert the object into a dict
screen_resolution_dict = screen_resolution_instance.to_dict()
# create an instance of ScreenResolution from a dict
screen_resolution_from_dict = ScreenResolution.from_dict(screen_resolution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


