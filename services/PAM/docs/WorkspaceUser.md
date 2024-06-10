# WorkspaceUser

One of users of the given workspace in \"users of workspace\" list

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Email | 
**role** | **str** | Role of the user in workspace | 
**user_id** | **str** | User ID | 
**folders_count** | **int** | Number of folders the user has access to | 
**joined_at** | **datetime** | Date and time of user joined the workspace | 

## Example

```python
from pam_api_client.models.workspace_user import WorkspaceUser

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceUser from a JSON string
workspace_user_instance = WorkspaceUser.from_json(json)
# print the JSON string representation of the object
print(WorkspaceUser.to_json())

# convert the object into a dict
workspace_user_dict = workspace_user_instance.to_dict()
# create an instance of WorkspaceUser from a dict
workspace_user_from_dict = WorkspaceUser.from_dict(workspace_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


