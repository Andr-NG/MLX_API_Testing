# UserWorkspace

One of workspaces of the given user in \"workspaces of user\" list

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of Workspace | 
**workspace_id** | **str** | Workspace ID | 
**role** | **str** | Role of user in workspace | 

## Example

```python
from services.PAM.pam_api_client.models.user_workspace import UserWorkspace

# TODO update the JSON string below
json = "{}"
# create an instance of UserWorkspace from a JSON string
user_workspace_instance = UserWorkspace.from_json(json)
# print the JSON string representation of the object
print(UserWorkspace.to_json())

# convert the object into a dict
user_workspace_dict = user_workspace_instance.to_dict()
# create an instance of UserWorkspace from a dict
user_workspace_from_dict = UserWorkspace.from_dict(user_workspace_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


