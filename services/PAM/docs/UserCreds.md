# UserCreds


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**password** | **str** |  | 

## Example

```python
from pam_api_client.models.user_creds import UserCreds

# TODO update the JSON string below
json = "{}"
# create an instance of UserCreds from a JSON string
user_creds_instance = UserCreds.from_json(json)
# print the JSON string representation of the object
print(UserCreds.to_json())

# convert the object into a dict
user_creds_dict = user_creds_instance.to_dict()
# create an instance of UserCreds from a dict
user_creds_from_dict = UserCreds.from_dict(user_creds_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


