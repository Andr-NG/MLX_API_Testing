# FolderUserArrayResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ResponseStatus**](ResponseStatus.md) |  | 
**data** | [**FolderUserArray**](FolderUserArray.md) |  | [optional] 

## Example

```python
from pam_api_client.models.folder_user_array_response import FolderUserArrayResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FolderUserArrayResponse from a JSON string
folder_user_array_response_instance = FolderUserArrayResponse.from_json(json)
# print the JSON string representation of the object
print(FolderUserArrayResponse.to_json())

# convert the object into a dict
folder_user_array_response_dict = folder_user_array_response_instance.to_dict()
# create an instance of FolderUserArrayResponse from a dict
folder_user_array_response_from_dict = FolderUserArrayResponse.from_dict(folder_user_array_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


