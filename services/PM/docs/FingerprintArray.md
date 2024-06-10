# FingerprintArray


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fingerprints** | [**List[Fingerprint]**](Fingerprint.md) |  | 

## Example

```python
from pm_api.models.fingerprint_array import FingerprintArray

# TODO update the JSON string below
json = "{}"
# create an instance of FingerprintArray from a JSON string
fingerprint_array_instance = FingerprintArray.from_json(json)
# print the JSON string representation of the object
print(FingerprintArray.to_json())

# convert the object into a dict
fingerprint_array_dict = fingerprint_array_instance.to_dict()
# create an instance of FingerprintArray from a dict
fingerprint_array_from_dict = FingerprintArray.from_dict(fingerprint_array_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


