# FolderUserArray


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | 
**users** | [**List[FolderUser]**](FolderUser.md) |  | 

## Example

```python
from pam_api_client.models.folder_user_array import FolderUserArray

# TODO update the JSON string below
json = "{}"
# create an instance of FolderUserArray from a JSON string
folder_user_array_instance = FolderUserArray.from_json(json)
# print the JSON string representation of the object
print(FolderUserArray.to_json())

# convert the object into a dict
folder_user_array_dict = folder_user_array_instance.to_dict()
# create an instance of FolderUserArray from a dict
folder_user_array_from_dict = FolderUserArray.from_dict(folder_user_array_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


