# PartialProfileMetaUpdateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flags** | [**ProfileMetaFlagsOptional**](ProfileMetaFlagsOptional.md) |  | [optional] 
**fingerprint** | [**FingerprintData**](FingerprintData.md) |  | [optional] 

## Example

```python
from pm_api.models.partial_profile_meta_update_params import PartialProfileMetaUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of PartialProfileMetaUpdateParams from a JSON string
partial_profile_meta_update_params_instance = PartialProfileMetaUpdateParams.from_json(json)
# print the JSON string representation of the object
print(PartialProfileMetaUpdateParams.to_json())

# convert the object into a dict
partial_profile_meta_update_params_dict = partial_profile_meta_update_params_instance.to_dict()
# create an instance of PartialProfileMetaUpdateParams from a dict
partial_profile_meta_update_params_from_dict = PartialProfileMetaUpdateParams.from_dict(partial_profile_meta_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


