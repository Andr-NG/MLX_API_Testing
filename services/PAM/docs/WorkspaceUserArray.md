# WorkspaceUserArray


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[WorkspaceUser]**](WorkspaceUser.md) |  | 
**total_count** | **int** | Total number of users that the workspace has | 

## Example

```python
from services.PAM.pam_api_client.models.workspace_user_array import WorkspaceUserArray

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceUserArray from a JSON string
workspace_user_array_instance = WorkspaceUserArray.from_json(json)
# print the JSON string representation of the object
print(WorkspaceUserArray.to_json())

# convert the object into a dict
workspace_user_array_dict = workspace_user_array_instance.to_dict()
# create an instance of WorkspaceUserArray from a dict
workspace_user_array_from_dict = WorkspaceUserArray.from_dict(workspace_user_array_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


