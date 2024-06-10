# Localization


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accept_languages** | **str** | used for generating locale and languages | 
**languages** | **str** | deprecated. pass empty string. | 
**locale** | **str** | deprecated. pass empty string. | 

## Example

```python
from pm_api.models.localization import Localization

# TODO update the JSON string below
json = "{}"
# create an instance of Localization from a JSON string
localization_instance = Localization.from_json(json)
# print the JSON string representation of the object
print(Localization.to_json())

# convert the object into a dict
localization_dict = localization_instance.to_dict()
# create an instance of Localization from a dict
localization_from_dict = Localization.from_dict(localization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


