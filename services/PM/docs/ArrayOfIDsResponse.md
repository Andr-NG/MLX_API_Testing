# ArrayOfIDsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ResponseStatus**](ResponseStatus.md) |  | 
**data** | [**ArrayOfIDs**](ArrayOfIDs.md) |  | [optional] 

## Example

```python
from pm_api.models.array_of_ids_response import ArrayOfIDsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfIDsResponse from a JSON string
array_of_ids_response_instance = ArrayOfIDsResponse.from_json(json)
# print the JSON string representation of the object
print(ArrayOfIDsResponse.to_json())

# convert the object into a dict
array_of_ids_response_dict = array_of_ids_response_instance.to_dict()
# create an instance of ArrayOfIDsResponse from a dict
array_of_ids_response_from_dict = ArrayOfIDsResponse.from_dict(array_of_ids_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


