# FingerprintData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**navigator** | [**Navigator**](Navigator.md) |  | [optional] 
**localization** | [**Localization**](Localization.md) |  | [optional] 
**timezone** | [**Timezone**](Timezone.md) |  | [optional] 
**graphic** | [**Graphic**](Graphic.md) |  | [optional] 
**webrtc** | [**Webrtc**](Webrtc.md) |  | [optional] 
**fonts** | **List[str]** |  | [optional] 
**media_devices** | [**MediaDevices**](MediaDevices.md) |  | [optional] 
**screen** | [**Screen**](Screen.md) |  | [optional] 
**geolocation** | [**Geolocation**](Geolocation.md) |  | [optional] 
**ports** | **List[int]** |  | [optional] 
**cmd_params** | [**CmdParams**](CmdParams.md) |  | [optional] 

## Example

```python
from pm_api.models.fingerprint_data import FingerprintData

# TODO update the JSON string below
json = "{}"
# create an instance of FingerprintData from a JSON string
fingerprint_data_instance = FingerprintData.from_json(json)
# print the JSON string representation of the object
print(FingerprintData.to_json())

# convert the object into a dict
fingerprint_data_dict = fingerprint_data_instance.to_dict()
# create an instance of FingerprintData from a dict
fingerprint_data_from_dict = FingerprintData.from_dict(fingerprint_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


