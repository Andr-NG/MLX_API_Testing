# FolderUser

One of users of the given folder in \"users of folder\" list

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Email | 
**role** | [**UserFolderRole**](UserFolderRole.md) |  | 
**user_id** | **str** | User ID | 

## Example

```python
from services.PAM.pam_api_client.models.folder_user import FolderUser

# TODO update the JSON string below
json = "{}"
# create an instance of FolderUser from a JSON string
folder_user_instance = FolderUser.from_json(json)
# print the JSON string representation of the object
print(FolderUser.to_json())

# convert the object into a dict
folder_user_dict = folder_user_instance.to_dict()
# create an instance of FolderUser from a dict
folder_user_from_dict = FolderUser.from_dict(folder_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


