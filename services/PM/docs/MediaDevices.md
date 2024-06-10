# MediaDevices


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**video_inputs** | **int** |  | 
**audio_inputs** | **int** |  | 
**audio_outputs** | **int** |  | 

## Example

```python
from pm_api.models.media_devices import MediaDevices

# TODO update the JSON string below
json = "{}"
# create an instance of MediaDevices from a JSON string
media_devices_instance = MediaDevices.from_json(json)
# print the JSON string representation of the object
print(MediaDevices.to_json())

# convert the object into a dict
media_devices_dict = media_devices_instance.to_dict()
# create an instance of MediaDevices from a dict
media_devices_from_dict = MediaDevices.from_dict(media_devices_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


