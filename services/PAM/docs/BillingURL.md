# BillingURL


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Bulling URL | 

## Example

```python
from services.PAM.pam_api_client.models.billing_url import BillingURL

# TODO update the JSON string below
json = "{}"
# create an instance of BillingURL from a JSON string
billing_url_instance = BillingURL.from_json(json)
# print the JSON string representation of the object
print(BillingURL.to_json())

# convert the object into a dict
billing_url_dict = billing_url_instance.to_dict()
# create an instance of BillingURL from a dict
billing_url_from_dict = BillingURL.from_dict(billing_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


