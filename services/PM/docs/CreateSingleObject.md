# CreateSingleObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 

## Example

```python
from pm_api.models.create_single_object import CreateSingleObject

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSingleObject from a JSON string
create_single_object_instance = CreateSingleObject.from_json(json)
# print the JSON string representation of the object
print(CreateSingleObject.to_json())

# convert the object into a dict
create_single_object_dict = create_single_object_instance.to_dict()
# create an instance of CreateSingleObject from a dict
create_single_object_from_dict = CreateSingleObject.from_dict(create_single_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


