# Signin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | JWT token | 
**refresh_token** | **str** | Refresh token | 

## Example

```python
from pam_api_client.models.signin import Signin

# TODO update the JSON string below
json = "{}"
# create an instance of Signin from a JSON string
signin_instance = Signin.from_json(json)
# print the JSON string representation of the object
print(Signin.to_json())

# convert the object into a dict
signin_dict = signin_instance.to_dict()
# create an instance of Signin from a dict
signin_from_dict = Signin.from_dict(signin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


