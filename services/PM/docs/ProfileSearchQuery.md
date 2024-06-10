# ProfileSearchQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | 
**profiles** | [**List[ProfileSearchQueryItem]**](ProfileSearchQueryItem.md) |  | 

## Example

```python
from pm_api.models.profile_search_query import ProfileSearchQuery

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileSearchQuery from a JSON string
profile_search_query_instance = ProfileSearchQuery.from_json(json)
# print the JSON string representation of the object
print(ProfileSearchQuery.to_json())

# convert the object into a dict
profile_search_query_dict = profile_search_query_instance.to_dict()
# create an instance of ProfileSearchQuery from a dict
profile_search_query_from_dict = ProfileSearchQuery.from_dict(profile_search_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


