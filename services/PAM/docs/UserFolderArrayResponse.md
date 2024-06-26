# UserFolderArrayResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ResponseStatus**](ResponseStatus.md) |  | 
**data** | [**UserFolderArray**](UserFolderArray.md) |  | [optional] 

## Example

```python
from services.PAM.pam_api_client.models.user_folder_array_response import UserFolderArrayResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserFolderArrayResponse from a JSON string
user_folder_array_response_instance = UserFolderArrayResponse.from_json(json)
# print the JSON string representation of the object
print(UserFolderArrayResponse.to_json())

# convert the object into a dict
user_folder_array_response_dict = user_folder_array_response_instance.to_dict()
# create an instance of UserFolderArrayResponse from a dict
user_folder_array_response_from_dict = UserFolderArrayResponse.from_dict(user_folder_array_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


