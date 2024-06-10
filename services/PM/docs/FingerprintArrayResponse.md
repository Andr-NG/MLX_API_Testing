# FingerprintArrayResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ResponseStatus**](ResponseStatus.md) |  | 
**data** | [**FingerprintArray**](FingerprintArray.md) |  | [optional] 

## Example

```python
from pm_api.models.fingerprint_array_response import FingerprintArrayResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FingerprintArrayResponse from a JSON string
fingerprint_array_response_instance = FingerprintArrayResponse.from_json(json)
# print the JSON string representation of the object
print(FingerprintArrayResponse.to_json())

# convert the object into a dict
fingerprint_array_response_dict = fingerprint_array_response_instance.to_dict()
# create an instance of FingerprintArrayResponse from a dict
fingerprint_array_response_from_dict = FingerprintArrayResponse.from_dict(fingerprint_array_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


