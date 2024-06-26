# WorkspaceStatsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ResponseStatus**](ResponseStatus.md) |  | 
**data** | [**WorkspaceStats**](WorkspaceStats.md) |  | [optional] 

## Example

```python
from services.PAM.pam_api_client.models.workspace_stats_response import WorkspaceStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceStatsResponse from a JSON string
workspace_stats_response_instance = WorkspaceStatsResponse.from_json(json)
# print the JSON string representation of the object
print(WorkspaceStatsResponse.to_json())

# convert the object into a dict
workspace_stats_response_dict = workspace_stats_response_instance.to_dict()
# create an instance of WorkspaceStatsResponse from a dict
workspace_stats_response_from_dict = WorkspaceStatsResponse.from_dict(workspace_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


