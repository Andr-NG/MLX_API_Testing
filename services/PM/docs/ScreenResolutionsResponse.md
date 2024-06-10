# ScreenResolutionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ResponseStatus**](ResponseStatus.md) |  | 
**data** | [**ScreenResolutions**](ScreenResolutions.md) |  | [optional] 

## Example

```python
from pm_api.models.screen_resolutions_response import ScreenResolutionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ScreenResolutionsResponse from a JSON string
screen_resolutions_response_instance = ScreenResolutionsResponse.from_json(json)
# print the JSON string representation of the object
print(ScreenResolutionsResponse.to_json())

# convert the object into a dict
screen_resolutions_response_dict = screen_resolutions_response_instance.to_dict()
# create an instance of ScreenResolutionsResponse from a dict
screen_resolutions_response_from_dict = ScreenResolutionsResponse.from_dict(screen_resolutions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


