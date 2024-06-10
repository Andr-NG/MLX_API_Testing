# ProfileMetaFlags


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**navigator_masking** | [**MaskingNCM**](MaskingNCM.md) |  | 
**audio_masking** | [**MaskingMN**](MaskingMN.md) |  | 
**localization_masking** | [**MaskingNCM**](MaskingNCM.md) |  | 
**geolocation_popup** | [**MaskingPAB**](MaskingPAB.md) |  | 
**geolocation_masking** | [**MaskingNCM**](MaskingNCM.md) |  | 
**timezone_masking** | [**MaskingNCM**](MaskingNCM.md) |  | 
**graphics_noise** | [**MaskingMN**](MaskingMN.md) |  | 
**graphics_masking** | [**MaskingNCM**](MaskingNCM.md) |  | 
**webrtc_masking** | [**MaskingNCMD**](MaskingNCMD.md) |  | 
**fonts_masking** | [**MaskingNCM**](MaskingNCM.md) |  | 
**media_devices_masking** | [**MaskingNCM**](MaskingNCM.md) |  | 
**screen_masking** | [**MaskingNCM**](MaskingNCM.md) |  | 
**proxy_masking** | [**MaskingCD**](MaskingCD.md) |  | 
**ports_masking** | [**MaskingMN**](MaskingMN.md) |  | 
**quic_mode** | [**MaskingND**](MaskingND.md) |  | [optional] 

## Example

```python
from pm_api.models.profile_meta_flags import ProfileMetaFlags

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileMetaFlags from a JSON string
profile_meta_flags_instance = ProfileMetaFlags.from_json(json)
# print the JSON string representation of the object
print(ProfileMetaFlags.to_json())

# convert the object into a dict
profile_meta_flags_dict = profile_meta_flags_instance.to_dict()
# create an instance of ProfileMetaFlags from a dict
profile_meta_flags_from_dict = ProfileMetaFlags.from_dict(profile_meta_flags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


