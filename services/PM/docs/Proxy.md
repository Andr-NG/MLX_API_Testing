# Proxy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | url - loads proxy object from remote url provided in host field before browser profile start | 
**host** | **str** |  | 
**port** | **int** |  | [optional] 
**username** | **str** |  | [optional] 
**password** | **str** |  | [optional] 

## Example

```python
from pm_api.models.proxy import Proxy

# TODO update the JSON string below
json = "{}"
# create an instance of Proxy from a JSON string
proxy_instance = Proxy.from_json(json)
# print the JSON string representation of the object
print(Proxy.to_json())

# convert the object into a dict
proxy_dict = proxy_instance.to_dict()
# create an instance of Proxy from a dict
proxy_from_dict = Proxy.from_dict(proxy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


