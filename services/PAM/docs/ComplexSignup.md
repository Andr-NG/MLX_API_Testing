# ComplexSignup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creds** | [**UserCreds**](UserCreds.md) |  | 
**settings** | [**Settings**](Settings.md) |  | [optional] 

## Example

```python
from services.PAM.pam_api_client.models.complex_signup import ComplexSignup

# TODO update the JSON string below
json = "{}"
# create an instance of ComplexSignup from a JSON string
complex_signup_instance = ComplexSignup.from_json(json)
# print the JSON string representation of the object
print(ComplexSignup.to_json())

# convert the object into a dict
complex_signup_dict = complex_signup_instance.to_dict()
# create an instance of ComplexSignup from a dict
complex_signup_from_dict = ComplexSignup.from_dict(complex_signup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


