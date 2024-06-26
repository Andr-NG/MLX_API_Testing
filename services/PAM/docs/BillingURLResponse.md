# BillingURLResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ResponseStatus**](ResponseStatus.md) |  | 
**data** | [**BillingURL**](BillingURL.md) |  | [optional] 

## Example

```python
from services.PAM.pam_api_client.models.billing_url_response import BillingURLResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BillingURLResponse from a JSON string
billing_url_response_instance = BillingURLResponse.from_json(json)
# print the JSON string representation of the object
print(BillingURLResponse.to_json())

# convert the object into a dict
billing_url_response_dict = billing_url_response_instance.to_dict()
# create an instance of BillingURLResponse from a dict
billing_url_response_from_dict = BillingURLResponse.from_dict(billing_url_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


