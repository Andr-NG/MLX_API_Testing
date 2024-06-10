# ProfileSearchQueryItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Field used in text search | 
**id** | **str** |  | 
**is_local** | **bool** |  | 
**core_version** | **int** |  | 
**os_type** | **str** |  | 
**browser_type** | [**BrowserType**](BrowserType.md) |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**removed_at** | **datetime** |  | [optional] 
**removed_by** | **str** |  | [optional] 
**folder_id** | **str** |  | 
**notes** | **str** |  | [optional] 

## Example

```python
from pm_api.models.profile_search_query_item import ProfileSearchQueryItem

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileSearchQueryItem from a JSON string
profile_search_query_item_instance = ProfileSearchQueryItem.from_json(json)
# print the JSON string representation of the object
print(ProfileSearchQueryItem.to_json())

# convert the object into a dict
profile_search_query_item_dict = profile_search_query_item_instance.to_dict()
# create an instance of ProfileSearchQueryItem from a dict
profile_search_query_item_from_dict = ProfileSearchQueryItem.from_dict(profile_search_query_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


