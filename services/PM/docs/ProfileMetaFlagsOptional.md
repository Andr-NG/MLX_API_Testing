# ProfileMetaFlagsOptional


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**navigator_masking** | [**MaskingNCM**](MaskingNCM.md) |  | [optional] 
**audio_masking** | [**MaskingMN**](MaskingMN.md) |  | [optional] 
**localization_masking** | [**MaskingNCM**](MaskingNCM.md) |  | [optional] 
**geolocation_popup** | [**MaskingPAB**](MaskingPAB.md) |  | [optional] 
**geolocation_masking** | [**MaskingNCM**](MaskingNCM.md) |  | [optional] 
**timezone_masking** | [**MaskingNCM**](MaskingNCM.md) |  | [optional] 
**graphics_noise** | [**MaskingMN**](MaskingMN.md) |  | [optional] 
**graphics_masking** | [**MaskingNCM**](MaskingNCM.md) |  | [optional] 
**webrtc_masking** | [**MaskingNCMD**](MaskingNCMD.md) |  | [optional] 
**fonts_masking** | [**MaskingNCM**](MaskingNCM.md) |  | [optional] 
**media_devices_masking** | [**MaskingNCM**](MaskingNCM.md) |  | [optional] 
**screen_masking** | [**MaskingNCM**](MaskingNCM.md) |  | [optional] 
**proxy_masking** | [**MaskingCD**](MaskingCD.md) |  | [optional] 
**ports_masking** | [**MaskingMN**](MaskingMN.md) |  | [optional] 
**quic_mode** | [**MaskingND**](MaskingND.md) |  | [optional] 

## Example

```python
from pm_api.models.profile_meta_flags_optional import ProfileMetaFlagsOptional

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileMetaFlagsOptional from a JSON string
profile_meta_flags_optional_instance = ProfileMetaFlagsOptional.from_json(json)
# print the JSON string representation of the object
print(ProfileMetaFlagsOptional.to_json())

# convert the object into a dict
profile_meta_flags_optional_dict = profile_meta_flags_optional_instance.to_dict()
# create an instance of ProfileMetaFlagsOptional from a dict
profile_meta_flags_optional_from_dict = ProfileMetaFlagsOptional.from_dict(profile_meta_flags_optional_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


