# AddUserToFolder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**folder_id** | **str** |  | 

## Example

```python
from pam_api_client.models.add_user_to_folder import AddUserToFolder

# TODO update the JSON string below
json = "{}"
# create an instance of AddUserToFolder from a JSON string
add_user_to_folder_instance = AddUserToFolder.from_json(json)
# print the JSON string representation of the object
print(AddUserToFolder.to_json())

# convert the object into a dict
add_user_to_folder_dict = add_user_to_folder_instance.to_dict()
# create an instance of AddUserToFolder from a dict
add_user_to_folder_from_dict = AddUserToFolder.from_dict(add_user_to_folder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


