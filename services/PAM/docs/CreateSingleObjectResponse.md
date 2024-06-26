# CreateSingleObjectResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ResponseStatus**](ResponseStatus.md) |  | 
**data** | [**CreateSingleObject**](CreateSingleObject.md) |  | [optional] 

## Example

```python
from services.PAM.pam_api_client.models.create_single_object_response import CreateSingleObjectResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSingleObjectResponse from a JSON string
create_single_object_response_instance = CreateSingleObjectResponse.from_json(json)
# print the JSON string representation of the object
print(CreateSingleObjectResponse.to_json())

# convert the object into a dict
create_single_object_response_dict = create_single_object_response_instance.to_dict()
# create an instance of CreateSingleObjectResponse from a dict
create_single_object_response_from_dict = CreateSingleObjectResponse.from_dict(create_single_object_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


