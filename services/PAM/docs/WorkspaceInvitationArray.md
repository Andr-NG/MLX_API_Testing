# WorkspaceInvitationArray


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invitations** | [**List[WorkspaceInvitation]**](WorkspaceInvitation.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from pam_api_client.models.workspace_invitation_array import WorkspaceInvitationArray

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceInvitationArray from a JSON string
workspace_invitation_array_instance = WorkspaceInvitationArray.from_json(json)
# print the JSON string representation of the object
print(WorkspaceInvitationArray.to_json())

# convert the object into a dict
workspace_invitation_array_dict = workspace_invitation_array_instance.to_dict()
# create an instance of WorkspaceInvitationArray from a dict
workspace_invitation_array_from_dict = WorkspaceInvitationArray.from_dict(workspace_invitation_array_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


