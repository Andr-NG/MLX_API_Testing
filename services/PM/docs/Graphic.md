# Graphic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor** | **str** |  | 
**renderer** | **str** |  | 
**vendor_id** | **str** |  | [optional] 
**device_id** | **str** |  | [optional] 

## Example

```python
from pm_api.models.graphic import Graphic

# TODO update the JSON string below
json = "{}"
# create an instance of Graphic from a JSON string
graphic_instance = Graphic.from_json(json)
# print the JSON string representation of the object
print(Graphic.to_json())

# convert the object into a dict
graphic_dict = graphic_instance.to_dict()
# create an instance of Graphic from a dict
graphic_from_dict = Graphic.from_dict(graphic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


