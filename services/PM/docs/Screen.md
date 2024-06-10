# Screen


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**width** | **int** |  | 
**height** | **int** |  | 
**pixel_ratio** | **float** |  | 

## Example

```python
from pm_api.models.screen import Screen

# TODO update the JSON string below
json = "{}"
# create an instance of Screen from a JSON string
screen_instance = Screen.from_json(json)
# print the JSON string representation of the object
print(Screen.to_json())

# convert the object into a dict
screen_dict = screen_instance.to_dict()
# create an instance of Screen from a dict
screen_from_dict = Screen.from_dict(screen_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


