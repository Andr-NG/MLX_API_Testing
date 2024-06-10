# BrowserExtension


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** | Extension name | 
**url** | **str** | Extension store link | 
**store** | **str** | Chrome Web Store or Mozilla Addons | 

## Example

```python
from pm_api.models.browser_extension import BrowserExtension

# TODO update the JSON string below
json = "{}"
# create an instance of BrowserExtension from a JSON string
browser_extension_instance = BrowserExtension.from_json(json)
# print the JSON string representation of the object
print(BrowserExtension.to_json())

# convert the object into a dict
browser_extension_dict = browser_extension_instance.to_dict()
# create an instance of BrowserExtension from a dict
browser_extension_from_dict = BrowserExtension.from_dict(browser_extension_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


