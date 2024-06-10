# Storage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_local** | **bool** | Folder ID | 
**save_service_worker** | **bool** | Service worker behaviour | [optional] 

## Example

```python
from pm_api.models.storage import Storage

# TODO update the JSON string below
json = "{}"
# create an instance of Storage from a JSON string
storage_instance = Storage.from_json(json)
# print the JSON string representation of the object
print(Storage.to_json())

# convert the object into a dict
storage_dict = storage_instance.to_dict()
# create an instance of Storage from a dict
storage_from_dict = Storage.from_dict(storage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


