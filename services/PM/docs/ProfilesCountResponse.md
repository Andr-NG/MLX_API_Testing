# ProfilesCountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ResponseStatus**](ResponseStatus.md) |  | 
**data** | [**ProfilesCount**](ProfilesCount.md) |  | [optional] 

## Example

```python
from pm_api.models.profiles_count_response import ProfilesCountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProfilesCountResponse from a JSON string
profiles_count_response_instance = ProfilesCountResponse.from_json(json)
# print the JSON string representation of the object
print(ProfilesCountResponse.to_json())

# convert the object into a dict
profiles_count_response_dict = profiles_count_response_instance.to_dict()
# create an instance of ProfilesCountResponse from a dict
profiles_count_response_from_dict = ProfilesCountResponse.from_dict(profiles_count_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


