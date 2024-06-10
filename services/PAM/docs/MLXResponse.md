# MLXResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ResponseStatus**](ResponseStatus.md) |  | 
**data** | **bytearray** |  | [optional] 

## Example

```python
from pam_api_client.models.mlx_response import MLXResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MLXResponse from a JSON string
mlx_response_instance = MLXResponse.from_json(json)
# print the JSON string representation of the object
print(MLXResponse.to_json())

# convert the object into a dict
mlx_response_dict = mlx_response_instance.to_dict()
# create an instance of MLXResponse from a dict
mlx_response_from_dict = MLXResponse.from_dict(mlx_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


