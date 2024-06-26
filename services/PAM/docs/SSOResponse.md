# SSOResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ResponseStatus**](ResponseStatus.md) |  | 
**data** | [**SSO**](SSO.md) |  | [optional] 

## Example

```python
from services.PAM.pam_api_client.models.sso_response import SSOResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SSOResponse from a JSON string
sso_response_instance = SSOResponse.from_json(json)
# print the JSON string representation of the object
print(SSOResponse.to_json())

# convert the object into a dict
sso_response_dict = sso_response_instance.to_dict()
# create an instance of SSOResponse from a dict
sso_response_from_dict = SSOResponse.from_dict(sso_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


