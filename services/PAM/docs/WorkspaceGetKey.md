# WorkspaceGetKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_id** | **str** |  | [optional] 

## Example

```python
from services.PAM.pam_api_client.models.workspace_get_key import WorkspaceGetKey

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceGetKey from a JSON string
workspace_get_key_instance = WorkspaceGetKey.from_json(json)
# print the JSON string representation of the object
print(WorkspaceGetKey.to_json())

# convert the object into a dict
workspace_get_key_dict = workspace_get_key_instance.to_dict()
# create an instance of WorkspaceGetKey from a dict
workspace_get_key_from_dict = WorkspaceGetKey.from_dict(workspace_get_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


