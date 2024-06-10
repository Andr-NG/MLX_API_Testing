# WorkspaceUserBalance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profiles_balance** | **int** |  | 
**members_balance** | **int** |  | [optional] 

## Example

```python
from pam_api_client.models.workspace_user_balance import WorkspaceUserBalance

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceUserBalance from a JSON string
workspace_user_balance_instance = WorkspaceUserBalance.from_json(json)
# print the JSON string representation of the object
print(WorkspaceUserBalance.to_json())

# convert the object into a dict
workspace_user_balance_dict = workspace_user_balance_instance.to_dict()
# create an instance of WorkspaceUserBalance from a dict
workspace_user_balance_from_dict = WorkspaceUserBalance.from_dict(workspace_user_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


