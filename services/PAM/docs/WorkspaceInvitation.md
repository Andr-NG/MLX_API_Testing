# WorkspaceInvitation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Email of the invited user | 
**workspace_id** | **str** | Workspace ID to which he was invited | 
**role** | **str** | Role of the user in workspace | 
**invited_at** | **datetime** | Date and Time of invitation sent | 
**expires_at** | **datetime** | Date and Time of invitation expiration | 

## Example

```python
from services.PAM.pam_api_client.models.workspace_invitation import WorkspaceInvitation

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceInvitation from a JSON string
workspace_invitation_instance = WorkspaceInvitation.from_json(json)
# print the JSON string representation of the object
print(WorkspaceInvitation.to_json())

# convert the object into a dict
workspace_invitation_dict = workspace_invitation_instance.to_dict()
# create an instance of WorkspaceInvitation from a dict
workspace_invitation_from_dict = WorkspaceInvitation.from_dict(workspace_invitation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


