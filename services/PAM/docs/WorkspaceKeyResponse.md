# WorkspaceKeyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ResponseStatus**](ResponseStatus.md) |  | 
**data** | [**WorkspaceKeyResponseData**](WorkspaceKeyResponseData.md) |  | [optional] 

## Example

```python
from services.PAM.pam_api_client.models.workspace_key_response import WorkspaceKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceKeyResponse from a JSON string
workspace_key_response_instance = WorkspaceKeyResponse.from_json(json)
# print the JSON string representation of the object
print(WorkspaceKeyResponse.to_json())

# convert the object into a dict
workspace_key_response_dict = workspace_key_response_instance.to_dict()
# create an instance of WorkspaceKeyResponse from a dict
workspace_key_response_from_dict = WorkspaceKeyResponse.from_dict(workspace_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


