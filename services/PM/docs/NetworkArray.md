# NetworkArray


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | 
**networks** | [**List[Network]**](Network.md) |  | 

## Example

```python
from pm_api.models.network_array import NetworkArray

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkArray from a JSON string
network_array_instance = NetworkArray.from_json(json)
# print the JSON string representation of the object
print(NetworkArray.to_json())

# convert the object into a dict
network_array_dict = network_array_instance.to_dict()
# create an instance of NetworkArray from a dict
network_array_from_dict = NetworkArray.from_dict(network_array_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


