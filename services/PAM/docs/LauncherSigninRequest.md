# LauncherSigninRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**machine_id** | **str** |  | [optional] 

## Example

```python
from services.PAM.pam_api_client.models.launcher_signin_request import LauncherSigninRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LauncherSigninRequest from a JSON string
launcher_signin_request_instance = LauncherSigninRequest.from_json(json)
# print the JSON string representation of the object
print(LauncherSigninRequest.to_json())

# convert the object into a dict
launcher_signin_request_dict = launcher_signin_request_instance.to_dict()
# create an instance of LauncherSigninRequest from a dict
launcher_signin_request_from_dict = LauncherSigninRequest.from_dict(launcher_signin_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


