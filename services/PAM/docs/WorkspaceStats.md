# WorkspaceStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users_count** | **int** | Count of workspace users except owner | 
**users_limit** | **int** | How many users workspace can hold according to the plan | 
**profiles_local_count** | **int** | Count of created local profiles including trash-bin | 
**profiles_cloud_count** | **int** | Count of created cloud profiles including trash-bin | 
**profiles_local_limit** | **int** | How many local profiles workspace can hold according to the plan | 
**profiles_cloud_limit** | **int** | How many cloud profiles workspace can hold according to the plan | 

## Example

```python
from services.PAM.pam_api_client.models.workspace_stats import WorkspaceStats

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceStats from a JSON string
workspace_stats_instance = WorkspaceStats.from_json(json)
# print the JSON string representation of the object
print(WorkspaceStats.to_json())

# convert the object into a dict
workspace_stats_dict = workspace_stats_instance.to_dict()
# create an instance of WorkspaceStats from a dict
workspace_stats_from_dict = WorkspaceStats.from_dict(workspace_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


