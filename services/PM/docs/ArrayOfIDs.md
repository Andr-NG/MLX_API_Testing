# ArrayOfIDs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | [optional] 
**ids** | **List[str]** |  | 

## Example

```python
from pm_api.models.array_of_ids import ArrayOfIDs

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfIDs from a JSON string
array_of_ids_instance = ArrayOfIDs.from_json(json)
# print the JSON string representation of the object
print(ArrayOfIDs.to_json())

# convert the object into a dict
array_of_ids_dict = array_of_ids_instance.to_dict()
# create an instance of ArrayOfIDs from a dict
array_of_ids_from_dict = ArrayOfIDs.from_dict(array_of_ids_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


