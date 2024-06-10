# CmdParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**params** | [**List[CmdParam]**](CmdParam.md) |  | 

## Example

```python
from pm_api.models.cmd_params import CmdParams

# TODO update the JSON string below
json = "{}"
# create an instance of CmdParams from a JSON string
cmd_params_instance = CmdParams.from_json(json)
# print the JSON string representation of the object
print(CmdParams.to_json())

# convert the object into a dict
cmd_params_dict = cmd_params_instance.to_dict()
# create an instance of CmdParams from a dict
cmd_params_from_dict = CmdParams.from_dict(cmd_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


