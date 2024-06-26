# Restriction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_name** | **str** |  | 
**cloud_profiles_count** | **int** |  | 
**local_profiles_count** | **int** |  | 
**folders_count** | **int** |  | 
**team_members_count** | **int** |  | 
**canceled** | **bool** |  | [optional] 
**expires_at** | **int** |  | [optional] 
**automation_available** | **bool** |  | [optional] 
**allowed_browser_types** | [**List[BrowserType]**](BrowserType.md) |  | 
**ratelimit** | [**List[RateLimit]**](RateLimit.md) |  | [optional] 

## Example

```python
from services.PAM.pam_api_client.models.restriction import Restriction

# TODO update the JSON string below
json = "{}"
# create an instance of Restriction from a JSON string
restriction_instance = Restriction.from_json(json)
# print the JSON string representation of the object
print(Restriction.to_json())

# convert the object into a dict
restriction_dict = restriction_instance.to_dict()
# create an instance of Restriction from a dict
restriction_from_dict = Restriction.from_dict(restriction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


