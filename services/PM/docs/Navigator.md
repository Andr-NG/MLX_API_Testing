# Navigator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_agent** | **str** |  | 
**hardware_concurrency** | **int** |  | 
**os_cpu** | **str** |  | [optional] 
**platform** | **str** |  | 

## Example

```python
from pm_api.models.navigator import Navigator

# TODO update the JSON string below
json = "{}"
# create an instance of Navigator from a JSON string
navigator_instance = Navigator.from_json(json)
# print the JSON string representation of the object
print(Navigator.to_json())

# convert the object into a dict
navigator_dict = navigator_instance.to_dict()
# create an instance of Navigator from a dict
navigator_from_dict = Navigator.from_dict(navigator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


