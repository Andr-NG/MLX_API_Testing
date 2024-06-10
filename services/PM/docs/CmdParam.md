# CmdParam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flag** | **str** |  | 
**value** | **str** |  | [optional] 

## Example

```python
from pm_api.models.cmd_param import CmdParam

# TODO update the JSON string below
json = "{}"
# create an instance of CmdParam from a JSON string
cmd_param_instance = CmdParam.from_json(json)
# print the JSON string representation of the object
print(CmdParam.to_json())

# convert the object into a dict
cmd_param_dict = cmd_param_instance.to_dict()
# create an instance of CmdParam from a dict
cmd_param_from_dict = CmdParam.from_dict(cmd_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


