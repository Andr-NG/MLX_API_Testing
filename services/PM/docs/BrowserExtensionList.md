# BrowserExtensionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**browser_extensions** | [**List[BrowserExtension]**](BrowserExtension.md) |  | 

## Example

```python
from pm_api.models.browser_extension_list import BrowserExtensionList

# TODO update the JSON string below
json = "{}"
# create an instance of BrowserExtensionList from a JSON string
browser_extension_list_instance = BrowserExtensionList.from_json(json)
# print the JSON string representation of the object
print(BrowserExtensionList.to_json())

# convert the object into a dict
browser_extension_list_dict = browser_extension_list_instance.to_dict()
# create an instance of BrowserExtensionList from a dict
browser_extension_list_from_dict = BrowserExtensionList.from_dict(browser_extension_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


