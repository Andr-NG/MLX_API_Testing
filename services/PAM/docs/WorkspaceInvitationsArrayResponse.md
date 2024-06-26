# WorkspaceInvitationsArrayResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ResponseStatus**](ResponseStatus.md) |  | 
**data** | [**WorkspaceInvitationArray**](WorkspaceInvitationArray.md) |  | [optional] 

## Example

```python
from services.PAM.pam_api_client.models.workspace_invitations_array_response import WorkspaceInvitationsArrayResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceInvitationsArrayResponse from a JSON string
workspace_invitations_array_response_instance = WorkspaceInvitationsArrayResponse.from_json(json)
# print the JSON string representation of the object
print(WorkspaceInvitationsArrayResponse.to_json())

# convert the object into a dict
workspace_invitations_array_response_dict = workspace_invitations_array_response_instance.to_dict()
# create an instance of WorkspaceInvitationsArrayResponse from a dict
workspace_invitations_array_response_from_dict = WorkspaceInvitationsArrayResponse.from_dict(workspace_invitations_array_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


