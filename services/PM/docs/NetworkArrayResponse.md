# NetworkArrayResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ResponseStatus**](ResponseStatus.md) |  | 
**data** | [**NetworkArray**](NetworkArray.md) |  | [optional] 

## Example

```python
from pm_api.models.network_array_response import NetworkArrayResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkArrayResponse from a JSON string
network_array_response_instance = NetworkArrayResponse.from_json(json)
# print the JSON string representation of the object
print(NetworkArrayResponse.to_json())

# convert the object into a dict
network_array_response_dict = network_array_response_instance.to_dict()
# create an instance of NetworkArrayResponse from a dict
network_array_response_from_dict = NetworkArrayResponse.from_dict(network_array_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


