# AutomationTokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ResponseStatus**](ResponseStatus.md) |  | 
**data** | [**AutomationToken**](AutomationToken.md) |  | [optional] 

## Example

```python
from services.PAM.pam_api_client.models.automation_token_response import AutomationTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AutomationTokenResponse from a JSON string
automation_token_response_instance = AutomationTokenResponse.from_json(json)
# print the JSON string representation of the object
print(AutomationTokenResponse.to_json())

# convert the object into a dict
automation_token_response_dict = automation_token_response_instance.to_dict()
# create an instance of AutomationTokenResponse from a dict
automation_token_response_from_dict = AutomationTokenResponse.from_dict(automation_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


