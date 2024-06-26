# GetRestriction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ResponseStatus**](ResponseStatus.md) |  | 
**data** | [**Restriction**](Restriction.md) |  | [optional] 

## Example

```python
from services.PAM.pam_api_client.models.get_restriction import GetRestriction

# TODO update the JSON string below
json = "{}"
# create an instance of GetRestriction from a JSON string
get_restriction_instance = GetRestriction.from_json(json)
# print the JSON string representation of the object
print(GetRestriction.to_json())

# convert the object into a dict
get_restriction_dict = get_restriction_instance.to_dict()
# create an instance of GetRestriction from a dict
get_restriction_from_dict = GetRestriction.from_dict(get_restriction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


