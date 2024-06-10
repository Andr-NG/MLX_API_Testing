# AutomationToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | JWT token | 

## Example

```python
from pam_api_client.models.automation_token import AutomationToken

# TODO update the JSON string below
json = "{}"
# create an instance of AutomationToken from a JSON string
automation_token_instance = AutomationToken.from_json(json)
# print the JSON string representation of the object
print(AutomationToken.to_json())

# convert the object into a dict
automation_token_dict = automation_token_instance.to_dict()
# create an instance of AutomationToken from a dict
automation_token_from_dict = AutomationToken.from_dict(automation_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


