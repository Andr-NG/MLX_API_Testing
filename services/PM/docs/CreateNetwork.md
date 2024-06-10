# CreateNetwork


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**proxy** | [**Proxy**](Proxy.md) |  | 

## Example

```python
from pm_api.models.create_network import CreateNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNetwork from a JSON string
create_network_instance = CreateNetwork.from_json(json)
# print the JSON string representation of the object
print(CreateNetwork.to_json())

# convert the object into a dict
create_network_dict = create_network_instance.to_dict()
# create an instance of CreateNetwork from a dict
create_network_from_dict = CreateNetwork.from_dict(create_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


