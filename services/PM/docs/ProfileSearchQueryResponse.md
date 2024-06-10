# ProfileSearchQueryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ResponseStatus**](ResponseStatus.md) |  | 
**data** | [**ProfileSearchQuery**](ProfileSearchQuery.md) |  | [optional] 

## Example

```python
from pm_api.models.profile_search_query_response import ProfileSearchQueryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileSearchQueryResponse from a JSON string
profile_search_query_response_instance = ProfileSearchQueryResponse.from_json(json)
# print the JSON string representation of the object
print(ProfileSearchQueryResponse.to_json())

# convert the object into a dict
profile_search_query_response_dict = profile_search_query_response_instance.to_dict()
# create an instance of ProfileSearchQueryResponse from a dict
profile_search_query_response_from_dict = ProfileSearchQueryResponse.from_dict(profile_search_query_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


