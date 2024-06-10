# RateLimit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | **str** | is a specific operation for particular rate limit | [optional] 
**limit_size** | **int** | is how many requests allowed for particular window_size (period) | 
**window_size** | **str** | is a specific time interval during which a certain number of requests are allowed, e.g. 30s, 60s, 1m, 2m, etc | 

## Example

```python
from pam_api_client.models.rate_limit import RateLimit

# TODO update the JSON string below
json = "{}"
# create an instance of RateLimit from a JSON string
rate_limit_instance = RateLimit.from_json(json)
# print the JSON string representation of the object
print(RateLimit.to_json())

# convert the object into a dict
rate_limit_dict = rate_limit_instance.to_dict()
# create an instance of RateLimit from a dict
rate_limit_from_dict = RateLimit.from_dict(rate_limit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


