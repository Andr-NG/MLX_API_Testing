# RemoveUserFromFolder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**folder_id** | **str** |  | 

## Example

```python
from services.PAM.pam_api_client.models.remove_user_from_folder import RemoveUserFromFolder

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveUserFromFolder from a JSON string
remove_user_from_folder_instance = RemoveUserFromFolder.from_json(json)
# print the JSON string representation of the object
print(RemoveUserFromFolder.to_json())

# convert the object into a dict
remove_user_from_folder_dict = remove_user_from_folder_instance.to_dict()
# create an instance of RemoveUserFromFolder from a dict
remove_user_from_folder_from_dict = RemoveUserFromFolder.from_dict(remove_user_from_folder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


