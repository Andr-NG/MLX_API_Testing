# ProfileSearchCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** |  | 
**limit** | **int** |  | 
**search_text** | **str** |  | 
**storage_type** | **str** |  | 
**browser_type** | [**BrowserType**](BrowserType.md) |  | [optional] 
**os_type** | **str** |  | [optional] 
**core_version** | **int** |  | [optional] 
**is_removed** | **bool** |  | 
**folder_id** | **str** | Folder ID to filter profiles by | [optional] 
**order_by** | **str** | field used for sorting | [optional] 
**sort** | **str** | sorting direction, asc or desc | [optional] 

## Example

```python
from pm_api.models.profile_search_criteria import ProfileSearchCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileSearchCriteria from a JSON string
profile_search_criteria_instance = ProfileSearchCriteria.from_json(json)
# print the JSON string representation of the object
print(ProfileSearchCriteria.to_json())

# convert the object into a dict
profile_search_criteria_dict = profile_search_criteria_instance.to_dict()
# create an instance of ProfileSearchCriteria from a dict
profile_search_criteria_from_dict = ProfileSearchCriteria.from_dict(profile_search_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


