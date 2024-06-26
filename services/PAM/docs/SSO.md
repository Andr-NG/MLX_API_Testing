# SSO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | UserID | 
**verified** | **bool** | Is verified | 

## Example

```python
from services.PAM.pam_api_client.models.sso import SSO

# TODO update the JSON string below
json = "{}"
# create an instance of SSO from a JSON string
sso_instance = SSO.from_json(json)
# print the JSON string representation of the object
print(SSO.to_json())

# convert the object into a dict
sso_dict = sso_instance.to_dict()
# create an instance of SSO from a dict
sso_from_dict = SSO.from_dict(sso_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


