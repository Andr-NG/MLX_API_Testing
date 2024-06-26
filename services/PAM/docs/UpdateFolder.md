# UpdateFolder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder_id** | **str** |  | 
**name** | **str** |  | 
**comment** | **str** |  | [optional] 

## Example

```python
from services.PAM.pam_api_client.models.update_folder import UpdateFolder

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFolder from a JSON string
update_folder_instance = UpdateFolder.from_json(json)
# print the JSON string representation of the object
print(UpdateFolder.to_json())

# convert the object into a dict
update_folder_dict = update_folder_instance.to_dict()
# create an instance of UpdateFolder from a dict
update_folder_from_dict = UpdateFolder.from_dict(update_folder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


