# ProfileMetaUpdateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flags** | [**ProfileMetaFlags**](ProfileMetaFlags.md) |  | 
**fingerprint** | [**FingerprintData**](FingerprintData.md) |  | 
**storage** | [**Storage**](Storage.md) |  | 
**proxy** | [**Proxy**](Proxy.md) |  | [optional] 
**custom_start_urls** | **List[str]** |  | [optional] 
**custom_dns** | **str** |  | [optional] 
**extension_ids** | **List[str]** |  | [optional] 

## Example

```python
from pm_api.models.profile_meta_update_params import ProfileMetaUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileMetaUpdateParams from a JSON string
profile_meta_update_params_instance = ProfileMetaUpdateParams.from_json(json)
# print the JSON string representation of the object
print(ProfileMetaUpdateParams.to_json())

# convert the object into a dict
profile_meta_update_params_dict = profile_meta_update_params_instance.to_dict()
# create an instance of ProfileMetaUpdateParams from a dict
profile_meta_update_params_from_dict = ProfileMetaUpdateParams.from_dict(profile_meta_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


