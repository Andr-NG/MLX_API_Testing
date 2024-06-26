# WorkspaceSendInvite


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** |  | 
**email** | **str** |  | 
**role** | **str** |  | 

## Example

```python
from services.PAM.pam_api_client.models.workspace_send_invite import WorkspaceSendInvite

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceSendInvite from a JSON string
workspace_send_invite_instance = WorkspaceSendInvite.from_json(json)
# print the JSON string representation of the object
print(WorkspaceSendInvite.to_json())

# convert the object into a dict
workspace_send_invite_dict = workspace_send_invite_instance.to_dict()
# create an instance of WorkspaceSendInvite from a dict
workspace_send_invite_from_dict = WorkspaceSendInvite.from_dict(workspace_send_invite_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


