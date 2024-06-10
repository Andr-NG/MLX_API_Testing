# WorkspaceKeyResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pub** | **str** | Public bas64 encoded key | 
**prv** | **str** | Private bas64 encoded key | 
**key_type** | **str** | Private key type. Used to determine decription policy. Possible values are &#39;server_generated&#39;, &#39;client_generated&#39; | 

## Example

```python
from pam_api_client.models.workspace_key_response_data import WorkspaceKeyResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceKeyResponseData from a JSON string
workspace_key_response_data_instance = WorkspaceKeyResponseData.from_json(json)
# print the JSON string representation of the object
print(WorkspaceKeyResponseData.to_json())

# convert the object into a dict
workspace_key_response_data_dict = workspace_key_response_data_instance.to_dict()
# create an instance of WorkspaceKeyResponseData from a dict
workspace_key_response_data_from_dict = WorkspaceKeyResponseData.from_dict(workspace_key_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


