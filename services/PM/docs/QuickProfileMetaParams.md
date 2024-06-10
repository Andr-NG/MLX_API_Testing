# QuickProfileMetaParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flags** | [**ProfileMetaFlags**](ProfileMetaFlags.md) |  | 
**fingerprint** | [**FingerprintData**](FingerprintData.md) |  | 

## Example

```python
from pm_api.models.quick_profile_meta_params import QuickProfileMetaParams

# TODO update the JSON string below
json = "{}"
# create an instance of QuickProfileMetaParams from a JSON string
quick_profile_meta_params_instance = QuickProfileMetaParams.from_json(json)
# print the JSON string representation of the object
print(QuickProfileMetaParams.to_json())

# convert the object into a dict
quick_profile_meta_params_dict = quick_profile_meta_params_instance.to_dict()
# create an instance of QuickProfileMetaParams from a dict
quick_profile_meta_params_from_dict = QuickProfileMetaParams.from_dict(quick_profile_meta_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


