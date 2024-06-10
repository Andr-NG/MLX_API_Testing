# Folder

One of folders

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of folder | 
**folder_id** | **str** | Folder ID | 
**profiles_count** | **int** | Number of profiles in the folder | 
**created_at** | **datetime** | The time and date of folder when it was created | 
**comment** | **str** | Comment for folder | [optional] 

## Example

```python
from pam_api_client.models.folder import Folder

# TODO update the JSON string below
json = "{}"
# create an instance of Folder from a JSON string
folder_instance = Folder.from_json(json)
# print the JSON string representation of the object
print(Folder.to_json())

# convert the object into a dict
folder_dict = folder_instance.to_dict()
# create an instance of Folder from a dict
folder_from_dict = Folder.from_dict(folder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


