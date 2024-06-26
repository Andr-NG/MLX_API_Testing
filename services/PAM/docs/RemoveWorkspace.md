# RemoveWorkspace


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** |  | 

## Example

```python
from services.PAM.pam_api_client.models.remove_workspace import RemoveWorkspace

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveWorkspace from a JSON string
remove_workspace_instance = RemoveWorkspace.from_json(json)
# print the JSON string representation of the object
print(RemoveWorkspace.to_json())

# convert the object into a dict
remove_workspace_dict = remove_workspace_instance.to_dict()
# create an instance of RemoveWorkspace from a dict
remove_workspace_from_dict = RemoveWorkspace.from_dict(remove_workspace_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


