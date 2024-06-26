# WorkspaceUserBalanceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ResponseStatus**](ResponseStatus.md) |  | 
**data** | [**WorkspaceUserBalance**](WorkspaceUserBalance.md) |  | [optional] 

## Example

```python
from services.PAM.pam_api_client.models.workspace_user_balance_response import WorkspaceUserBalanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceUserBalanceResponse from a JSON string
workspace_user_balance_response_instance = WorkspaceUserBalanceResponse.from_json(json)
# print the JSON string representation of the object
print(WorkspaceUserBalanceResponse.to_json())

# convert the object into a dict
workspace_user_balance_response_dict = workspace_user_balance_response_instance.to_dict()
# create an instance of WorkspaceUserBalanceResponse from a dict
workspace_user_balance_response_from_dict = WorkspaceUserBalanceResponse.from_dict(workspace_user_balance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


