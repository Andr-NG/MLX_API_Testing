# ReadyProfileResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ResponseStatus**](ResponseStatus.md) |  | 
**data** | [**ReadyProfile**](ReadyProfile.md) |  | [optional] 

## Example

```python
from pm_api.models.ready_profile_response import ReadyProfileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadyProfileResponse from a JSON string
ready_profile_response_instance = ReadyProfileResponse.from_json(json)
# print the JSON string representation of the object
print(ReadyProfileResponse.to_json())

# convert the object into a dict
ready_profile_response_dict = ready_profile_response_instance.to_dict()
# create an instance of ReadyProfileResponse from a dict
ready_profile_response_from_dict = ReadyProfileResponse.from_dict(ready_profile_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


