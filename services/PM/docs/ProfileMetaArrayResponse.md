# ProfileMetaArrayResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ResponseStatus**](ResponseStatus.md) |  | 
**data** | [**ProfileMetaArray**](ProfileMetaArray.md) |  | [optional] 

## Example

```python
from pm_api.models.profile_meta_array_response import ProfileMetaArrayResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileMetaArrayResponse from a JSON string
profile_meta_array_response_instance = ProfileMetaArrayResponse.from_json(json)
# print the JSON string representation of the object
print(ProfileMetaArrayResponse.to_json())

# convert the object into a dict
profile_meta_array_response_dict = profile_meta_array_response_instance.to_dict()
# create an instance of ProfileMetaArrayResponse from a dict
profile_meta_array_response_from_dict = ProfileMetaArrayResponse.from_dict(profile_meta_array_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


