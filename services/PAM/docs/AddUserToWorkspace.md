# AddUserToWorkspace


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**role** | **str** |  | 

## Example

```python
from services.PAM.pam_api_client.models.add_user_to_workspace import AddUserToWorkspace

# TODO update the JSON string below
json = "{}"
# create an instance of AddUserToWorkspace from a JSON string
add_user_to_workspace_instance = AddUserToWorkspace.from_json(json)
# print the JSON string representation of the object
print(AddUserToWorkspace.to_json())

# convert the object into a dict
add_user_to_workspace_dict = add_user_to_workspace_instance.to_dict()
# create an instance of AddUserToWorkspace from a dict
add_user_to_workspace_from_dict = AddUserToWorkspace.from_dict(add_user_to_workspace_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


