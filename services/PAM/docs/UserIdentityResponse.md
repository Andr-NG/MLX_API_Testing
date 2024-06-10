# UserIdentityResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ResponseStatus**](ResponseStatus.md) |  | 
**data** | [**UserIdentity**](UserIdentity.md) |  | [optional] 

## Example

```python
from pam_api_client.models.user_identity_response import UserIdentityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserIdentityResponse from a JSON string
user_identity_response_instance = UserIdentityResponse.from_json(json)
# print the JSON string representation of the object
print(UserIdentityResponse.to_json())

# convert the object into a dict
user_identity_response_dict = user_identity_response_instance.to_dict()
# create an instance of UserIdentityResponse from a dict
user_identity_response_from_dict = UserIdentityResponse.from_dict(user_identity_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


