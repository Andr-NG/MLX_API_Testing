# UserFolder

One of folders of the given user in \"folders of user\" list

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
from pam_api_client.models.user_folder import UserFolder

# TODO update the JSON string below
json = "{}"
# create an instance of UserFolder from a JSON string
user_folder_instance = UserFolder.from_json(json)
# print the JSON string representation of the object
print(UserFolder.to_json())

# convert the object into a dict
user_folder_dict = user_folder_instance.to_dict()
# create an instance of UserFolder from a dict
user_folder_from_dict = UserFolder.from_dict(user_folder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


