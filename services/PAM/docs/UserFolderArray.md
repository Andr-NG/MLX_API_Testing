# UserFolderArray


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folders** | [**List[UserFolder]**](UserFolder.md) |  | 

## Example

```python
from pam_api_client.models.user_folder_array import UserFolderArray

# TODO update the JSON string below
json = "{}"
# create an instance of UserFolderArray from a JSON string
user_folder_array_instance = UserFolderArray.from_json(json)
# print the JSON string representation of the object
print(UserFolderArray.to_json())

# convert the object into a dict
user_folder_array_dict = user_folder_array_instance.to_dict()
# create an instance of UserFolderArray from a dict
user_folder_array_from_dict = UserFolderArray.from_dict(user_folder_array_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


