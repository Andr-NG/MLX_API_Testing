# FingerprintDataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ResponseStatus**](ResponseStatus.md) |  | 
**data** | [**FingerprintData**](FingerprintData.md) |  | [optional] 

## Example

```python
from pm_api.models.fingerprint_data_response import FingerprintDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FingerprintDataResponse from a JSON string
fingerprint_data_response_instance = FingerprintDataResponse.from_json(json)
# print the JSON string representation of the object
print(FingerprintDataResponse.to_json())

# convert the object into a dict
fingerprint_data_response_dict = fingerprint_data_response_instance.to_dict()
# create an instance of FingerprintDataResponse from a dict
fingerprint_data_response_from_dict = FingerprintDataResponse.from_dict(fingerprint_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


