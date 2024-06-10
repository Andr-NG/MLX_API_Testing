# UserWorkspaceArray


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspaces** | [**List[UserWorkspace]**](UserWorkspace.md) |  | 
**total_count** | **int** | Total number of workspaces that the user has | 

## Example

```python
from pam_api_client.models.user_workspace_array import UserWorkspaceArray

# TODO update the JSON string below
json = "{}"
# create an instance of UserWorkspaceArray from a JSON string
user_workspace_array_instance = UserWorkspaceArray.from_json(json)
# print the JSON string representation of the object
print(UserWorkspaceArray.to_json())

# convert the object into a dict
user_workspace_array_dict = user_workspace_array_instance.to_dict()
# create an instance of UserWorkspaceArray from a dict
user_workspace_array_from_dict = UserWorkspaceArray.from_dict(user_workspace_array_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


