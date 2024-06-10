# UserWorkspaceArrayResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ResponseStatus**](ResponseStatus.md) |  | 
**data** | [**UserWorkspaceArray**](UserWorkspaceArray.md) |  | [optional] 

## Example

```python
from pam_api_client.models.user_workspace_array_response import UserWorkspaceArrayResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserWorkspaceArrayResponse from a JSON string
user_workspace_array_response_instance = UserWorkspaceArrayResponse.from_json(json)
# print the JSON string representation of the object
print(UserWorkspaceArrayResponse.to_json())

# convert the object into a dict
user_workspace_array_response_dict = user_workspace_array_response_instance.to_dict()
# create an instance of UserWorkspaceArrayResponse from a dict
user_workspace_array_response_from_dict = UserWorkspaceArrayResponse.from_dict(user_workspace_array_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


