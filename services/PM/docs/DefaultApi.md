# pm_api.DefaultApi

All URIs are relative to *https://api.multilogin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**baked**](DefaultApi.md#baked) | **GET** /profile/baked | Baked
[**create_extensions**](DefaultApi.md#create_extensions) | **POST** /extensions/create | Store Browser Extensions for Workspace
[**get_extensions**](DefaultApi.md#get_extensions) | **GET** /extensions | Retrieve Browser Extensions for Workspace
[**network_create**](DefaultApi.md#network_create) | **POST** /network/create | Network Create
[**network_remove**](DefaultApi.md#network_remove) | **POST** /network/remove | Network Remove
[**networks**](DefaultApi.md#networks) | **GET** /network | Networks
[**partial_profile_update**](DefaultApi.md#partial_profile_update) | **POST** /profile/partial_update | Partial Profile Update
[**profile_auto_update_core**](DefaultApi.md#profile_auto_update_core) | **POST** /profile/auto_update_core | Profile Auto Update Core
[**profile_clone**](DefaultApi.md#profile_clone) | **POST** /profile/clone | Profile Clone
[**profile_count_by_workspace**](DefaultApi.md#profile_count_by_workspace) | **GET** /profile/workspace_count | Profile Count By Workspace
[**profile_create**](DefaultApi.md#profile_create) | **POST** /profile/create | Profile Create
[**profile_fingerprints**](DefaultApi.md#profile_fingerprints) | **POST** /profile/fingerprints | Profile Fingerprints
[**profile_meta_ids_by_workspace_folder**](DefaultApi.md#profile_meta_ids_by_workspace_folder) | **GET** /profile/workspace_meta_ids | Profile Meta IDs By Workspace Folder
[**profile_metas**](DefaultApi.md#profile_metas) | **POST** /profile/metas | Profile Metas
[**profile_move**](DefaultApi.md#profile_move) | **POST** /profile/move | Profile Move
[**profile_quick**](DefaultApi.md#profile_quick) | **POST** /profile/quick | Quick Profile
[**profile_remove**](DefaultApi.md#profile_remove) | **POST** /profile/remove | Profile Remove
[**profile_restore**](DefaultApi.md#profile_restore) | **POST** /profile/restore | Profile Restore
[**profile_update**](DefaultApi.md#profile_update) | **POST** /profile/update | Profile Update
[**remove_extensions**](DefaultApi.md#remove_extensions) | **DELETE** /extensions/remove | Remove Browser Extensions for Workspace
[**screen_resolution**](DefaultApi.md#screen_resolution) | **GET** /fpb/resolutions | Screen Resolution
[**search_profiles**](DefaultApi.md#search_profiles) | **POST** /profile/search | Search Profiles
[**summary**](DefaultApi.md#summary) | **GET** /profile/summary | Summary


# **baked**
> ReadyProfileResponse baked(meta_id)

Baked

(Private API) Provides all required profile data for starting a browser profile. Endpoint is for client side internal use. In case of modification make sure to verify it is working inside 5 projects<`:` 1. gateway | 2. profile manager 3. launcher 4. adapter-sf 5. adapter-mimic

### Example


```python
import pm_api
from pm_api.models.ready_profile_response import ReadyProfileResponse
from pm_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pm_api.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pm_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pm_api.DefaultApi(api_client)
    meta_id = 'meta_id_example' # str | ID of the profile meta

    try:
        # Baked
        api_response = api_instance.baked(meta_id)
        print("The response of DefaultApi->baked:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->baked: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meta_id** | **str**| ID of the profile meta | 

### Return type

[**ReadyProfileResponse**](ReadyProfileResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Baked browser profiles that are ready to start |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_extensions**
> MLXResponse create_extensions(extensions_create)

Store Browser Extensions for Workspace

Takes list of browser extension links from Chrome Web Store or Mozilla Addons and returns saved ids

### Example


```python
import pm_api
from pm_api.models.extensions_create import ExtensionsCreate
from pm_api.models.mlx_response import MLXResponse
from pm_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pm_api.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pm_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pm_api.DefaultApi(api_client)
    extensions_create = pm_api.ExtensionsCreate() # ExtensionsCreate | List of browser extension links from Chrome Web Store or Mozilla Addons

    try:
        # Store Browser Extensions for Workspace
        api_response = api_instance.create_extensions(extensions_create)
        print("The response of DefaultApi->create_extensions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_extensions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extensions_create** | [**ExtensionsCreate**](ExtensionsCreate.md)| List of browser extension links from Chrome Web Store or Mozilla Addons | 

### Return type

[**MLXResponse**](MLXResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | List of ids of stored Extensions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_extensions**
> BrowserExtensionList get_extensions()

Retrieve Browser Extensions for Workspace

Returns list of browser extensions for workspace

### Example


```python
import pm_api
from pm_api.models.browser_extension_list import BrowserExtensionList
from pm_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pm_api.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pm_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pm_api.DefaultApi(api_client)

    try:
        # Retrieve Browser Extensions for Workspace
        api_response = api_instance.get_extensions()
        print("The response of DefaultApi->get_extensions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_extensions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BrowserExtensionList**](BrowserExtensionList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | List stored Extensions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_create**
> CreateSingleObjectResponse network_create(create_network)

Network Create

Add a new network

### Example


```python
import pm_api
from pm_api.models.create_network import CreateNetwork
from pm_api.models.create_single_object_response import CreateSingleObjectResponse
from pm_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pm_api.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pm_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pm_api.DefaultApi(api_client)
    create_network = pm_api.CreateNetwork() # CreateNetwork | Parameters of new network

    try:
        # Network Create
        api_response = api_instance.network_create(create_network)
        print("The response of DefaultApi->network_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->network_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_network** | [**CreateNetwork**](CreateNetwork.md)| Parameters of new network | 

### Return type

[**CreateSingleObjectResponse**](CreateSingleObjectResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Id of created network |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_remove**
> MLXResponse network_remove(remove_network)

Network Remove

Remove networks by ids from selected workspace

### Example


```python
import pm_api
from pm_api.models.mlx_response import MLXResponse
from pm_api.models.remove_network import RemoveNetwork
from pm_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pm_api.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pm_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pm_api.DefaultApi(api_client)
    remove_network = pm_api.RemoveNetwork() # RemoveNetwork | Ids of networks for remove from selected workspace

    try:
        # Network Remove
        api_response = api_instance.network_remove(remove_network)
        print("The response of DefaultApi->network_remove:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->network_remove: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remove_network** | [**RemoveNetwork**](RemoveNetwork.md)| Ids of networks for remove from selected workspace | 

### Return type

[**MLXResponse**](MLXResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Response message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **networks**
> NetworkArrayResponse networks(limit, offset)

Networks

Get networks for the workspace

### Example


```python
import pm_api
from pm_api.models.network_array_response import NetworkArrayResponse
from pm_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pm_api.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pm_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pm_api.DefaultApi(api_client)
    limit = 56 # int | Amount of folders.
    offset = 56 # int | Offset says to skip that many rows.

    try:
        # Networks
        api_response = api_instance.networks(limit, offset)
        print("The response of DefaultApi->networks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->networks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Amount of folders. | 
 **offset** | **int**| Offset says to skip that many rows. | 

### Return type

[**NetworkArrayResponse**](NetworkArrayResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Number of profiles in selected folder |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_profile_update**
> MLXResponse partial_profile_update(partial_update_profile)

Partial Profile Update

Update the profile partially

### Example


```python
import pm_api
from pm_api.models.mlx_response import MLXResponse
from pm_api.models.partial_update_profile import PartialUpdateProfile
from pm_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pm_api.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pm_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pm_api.DefaultApi(api_client)
    partial_update_profile = pm_api.PartialUpdateProfile() # PartialUpdateProfile | New parameters for exist profile

    try:
        # Partial Profile Update
        api_response = api_instance.partial_profile_update(partial_update_profile)
        print("The response of DefaultApi->partial_profile_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->partial_profile_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partial_update_profile** | [**PartialUpdateProfile**](PartialUpdateProfile.md)| New parameters for exist profile | 

### Return type

[**MLXResponse**](MLXResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Response message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profile_auto_update_core**
> MLXResponse profile_auto_update_core(auto_update_core_profiles)

Profile Auto Update Core

Set auto update core for profiles in a bulk

### Example


```python
import pm_api
from pm_api.models.auto_update_core_profiles import AutoUpdateCoreProfiles
from pm_api.models.mlx_response import MLXResponse
from pm_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pm_api.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pm_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pm_api.DefaultApi(api_client)
    auto_update_core_profiles = pm_api.AutoUpdateCoreProfiles() # AutoUpdateCoreProfiles | Ids of profiles to change the auto update core flag

    try:
        # Profile Auto Update Core
        api_response = api_instance.profile_auto_update_core(auto_update_core_profiles)
        print("The response of DefaultApi->profile_auto_update_core:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->profile_auto_update_core: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_update_core_profiles** | [**AutoUpdateCoreProfiles**](AutoUpdateCoreProfiles.md)| Ids of profiles to change the auto update core flag | 

### Return type

[**MLXResponse**](MLXResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Response message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profile_clone**
> ArrayOfIDsResponse profile_clone(clone_profile)

Profile Clone

Clone profile

### Example


```python
import pm_api
from pm_api.models.array_of_ids_response import ArrayOfIDsResponse
from pm_api.models.clone_profile import CloneProfile
from pm_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pm_api.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pm_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pm_api.DefaultApi(api_client)
    clone_profile = pm_api.CloneProfile() # CloneProfile | Id of profile and amount of times for clone

    try:
        # Profile Clone
        api_response = api_instance.profile_clone(clone_profile)
        print("The response of DefaultApi->profile_clone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->profile_clone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clone_profile** | [**CloneProfile**](CloneProfile.md)| Id of profile and amount of times for clone | 

### Return type

[**ArrayOfIDsResponse**](ArrayOfIDsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | List with ids of cloned profiles |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profile_count_by_workspace**
> ProfilesCountResponse profile_count_by_workspace(folder_id=folder_id)

Profile Count By Workspace

Get count of profiles for the workspace

### Example


```python
import pm_api
from pm_api.models.profiles_count_response import ProfilesCountResponse
from pm_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pm_api.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pm_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pm_api.DefaultApi(api_client)
    folder_id = 'folder_id_example' # str | ID of the folder (optional)

    try:
        # Profile Count By Workspace
        api_response = api_instance.profile_count_by_workspace(folder_id=folder_id)
        print("The response of DefaultApi->profile_count_by_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->profile_count_by_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**| ID of the folder | [optional] 

### Return type

[**ProfilesCountResponse**](ProfilesCountResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Number of profiles in selected folder |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profile_create**
> ArrayOfIDsResponse profile_create(create_profile)

Profile Create

Add a new profile

### Example


```python
import pm_api
from pm_api.models.array_of_ids_response import ArrayOfIDsResponse
from pm_api.models.create_profile import CreateProfile
from pm_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pm_api.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pm_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pm_api.DefaultApi(api_client)
    create_profile = pm_api.CreateProfile() # CreateProfile | Parameters of new profile

    try:
        # Profile Create
        api_response = api_instance.profile_create(create_profile)
        print("The response of DefaultApi->profile_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->profile_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_profile** | [**CreateProfile**](CreateProfile.md)| Parameters of new profile | 

### Return type

[**ArrayOfIDsResponse**](ArrayOfIDsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | List with ids of created profiles |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profile_fingerprints**
> FingerprintArrayResponse profile_fingerprints(get_profile_parts)

Profile Fingerprints

Get list of fingerprints for selected profile metas

### Example


```python
import pm_api
from pm_api.models.fingerprint_array_response import FingerprintArrayResponse
from pm_api.models.get_profile_parts import GetProfileParts
from pm_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pm_api.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pm_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pm_api.DefaultApi(api_client)
    get_profile_parts = pm_api.GetProfileParts() # GetProfileParts | List of ids of profiles

    try:
        # Profile Fingerprints
        api_response = api_instance.profile_fingerprints(get_profile_parts)
        print("The response of DefaultApi->profile_fingerprints:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->profile_fingerprints: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_profile_parts** | [**GetProfileParts**](GetProfileParts.md)| List of ids of profiles | 

### Return type

[**FingerprintArrayResponse**](FingerprintArrayResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | List with fingerprints for selected profile metas |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profile_meta_ids_by_workspace_folder**
> ArrayOfIDsResponse profile_meta_ids_by_workspace_folder(limit, offset, is_local, is_removed, folder_id=folder_id)

Profile Meta IDs By Workspace Folder

Get list of profile meta ids for the folder in workspace

### Example


```python
import pm_api
from pm_api.models.array_of_ids_response import ArrayOfIDsResponse
from pm_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pm_api.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pm_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pm_api.DefaultApi(api_client)
    limit = 56 # int | Amount of profiles.
    offset = 56 # int | Offset says to skip that many rows.
    is_local = True # bool | Type of profiles.
    is_removed = True # bool | Type of profiles.
    folder_id = 'folder_id_example' # str | ID of the folder. If not set we return profiles regardless of folder (optional)

    try:
        # Profile Meta IDs By Workspace Folder
        api_response = api_instance.profile_meta_ids_by_workspace_folder(limit, offset, is_local, is_removed, folder_id=folder_id)
        print("The response of DefaultApi->profile_meta_ids_by_workspace_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->profile_meta_ids_by_workspace_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Amount of profiles. | 
 **offset** | **int**| Offset says to skip that many rows. | 
 **is_local** | **bool**| Type of profiles. | 
 **is_removed** | **bool**| Type of profiles. | 
 **folder_id** | **str**| ID of the folder. If not set we return profiles regardless of folder | [optional] 

### Return type

[**ArrayOfIDsResponse**](ArrayOfIDsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | List of ids of profiles |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profile_metas**
> ProfileMetaArrayResponse profile_metas(get_profile_parts)

Profile Metas

Get profile metas

### Example


```python
import pm_api
from pm_api.models.get_profile_parts import GetProfileParts
from pm_api.models.profile_meta_array_response import ProfileMetaArrayResponse
from pm_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pm_api.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pm_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pm_api.DefaultApi(api_client)
    get_profile_parts = pm_api.GetProfileParts() # GetProfileParts | Get list with profiles metas by ids

    try:
        # Profile Metas
        api_response = api_instance.profile_metas(get_profile_parts)
        print("The response of DefaultApi->profile_metas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->profile_metas: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_profile_parts** | [**GetProfileParts**](GetProfileParts.md)| Get list with profiles metas by ids | 

### Return type

[**ProfileMetaArrayResponse**](ProfileMetaArrayResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | List with metadata of selected profiles |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profile_move**
> MLXResponse profile_move(move_profile)

Profile Move

Move profile

### Example


```python
import pm_api
from pm_api.models.mlx_response import MLXResponse
from pm_api.models.move_profile import MoveProfile
from pm_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pm_api.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pm_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pm_api.DefaultApi(api_client)
    move_profile = pm_api.MoveProfile() # MoveProfile | Id of profile for moving and destination place

    try:
        # Profile Move
        api_response = api_instance.profile_move(move_profile)
        print("The response of DefaultApi->profile_move:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->profile_move: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_profile** | [**MoveProfile**](MoveProfile.md)| Id of profile for moving and destination place | 

### Return type

[**MLXResponse**](MLXResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Response message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profile_quick**
> ReadyProfileResponse profile_quick(quick_profile)

Quick Profile

Get profile for quick start

### Example


```python
import pm_api
from pm_api.models.quick_profile import QuickProfile
from pm_api.models.ready_profile_response import ReadyProfileResponse
from pm_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pm_api.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pm_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pm_api.DefaultApi(api_client)
    quick_profile = pm_api.QuickProfile() # QuickProfile | Parameters of quick profile

    try:
        # Quick Profile
        api_response = api_instance.profile_quick(quick_profile)
        print("The response of DefaultApi->profile_quick:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->profile_quick: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quick_profile** | [**QuickProfile**](QuickProfile.md)| Parameters of quick profile | 

### Return type

[**ReadyProfileResponse**](ReadyProfileResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Profile data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profile_remove**
> MLXResponse profile_remove(remove_profiles)

Profile Remove

Remove profiles

### Example


```python
import pm_api
from pm_api.models.mlx_response import MLXResponse
from pm_api.models.remove_profiles import RemoveProfiles
from pm_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pm_api.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pm_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pm_api.DefaultApi(api_client)
    remove_profiles = pm_api.RemoveProfiles() # RemoveProfiles | Ids of profiles for remove

    try:
        # Profile Remove
        api_response = api_instance.profile_remove(remove_profiles)
        print("The response of DefaultApi->profile_remove:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->profile_remove: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remove_profiles** | [**RemoveProfiles**](RemoveProfiles.md)| Ids of profiles for remove | 

### Return type

[**MLXResponse**](MLXResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Response message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profile_restore**
> MLXResponse profile_restore(restore_profiles)

Profile Restore

Restore profiles

### Example


```python
import pm_api
from pm_api.models.mlx_response import MLXResponse
from pm_api.models.restore_profiles import RestoreProfiles
from pm_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pm_api.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pm_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pm_api.DefaultApi(api_client)
    restore_profiles = pm_api.RestoreProfiles() # RestoreProfiles | Ids of profiles for restore

    try:
        # Profile Restore
        api_response = api_instance.profile_restore(restore_profiles)
        print("The response of DefaultApi->profile_restore:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->profile_restore: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **restore_profiles** | [**RestoreProfiles**](RestoreProfiles.md)| Ids of profiles for restore | 

### Return type

[**MLXResponse**](MLXResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Response message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profile_update**
> MLXResponse profile_update(update_profile)

Profile Update

Update the profile

### Example


```python
import pm_api
from pm_api.models.mlx_response import MLXResponse
from pm_api.models.update_profile import UpdateProfile
from pm_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pm_api.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pm_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pm_api.DefaultApi(api_client)
    update_profile = pm_api.UpdateProfile() # UpdateProfile | New parameters for exist profile

    try:
        # Profile Update
        api_response = api_instance.profile_update(update_profile)
        print("The response of DefaultApi->profile_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->profile_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_profile** | [**UpdateProfile**](UpdateProfile.md)| New parameters for exist profile | 

### Return type

[**MLXResponse**](MLXResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Response message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_extensions**
> MLXResponse remove_extensions(list_of_string_ids)

Remove Browser Extensions for Workspace

Takes list of browser extension ids and removes them from workspace

### Example


```python
import pm_api
from pm_api.models.list_of_string_ids import ListOfStringIDs
from pm_api.models.mlx_response import MLXResponse
from pm_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pm_api.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pm_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pm_api.DefaultApi(api_client)
    list_of_string_ids = pm_api.ListOfStringIDs() # ListOfStringIDs | List of browser extension ids

    try:
        # Remove Browser Extensions for Workspace
        api_response = api_instance.remove_extensions(list_of_string_ids)
        print("The response of DefaultApi->remove_extensions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->remove_extensions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_of_string_ids** | [**ListOfStringIDs**](ListOfStringIDs.md)| List of browser extension ids | 

### Return type

[**MLXResponse**](MLXResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Response message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **screen_resolution**
> ScreenResolutionsResponse screen_resolution()

Screen Resolution

Returns a list of available screen resolutions

### Example


```python
import pm_api
from pm_api.models.screen_resolutions_response import ScreenResolutionsResponse
from pm_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pm_api.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pm_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pm_api.DefaultApi(api_client)

    try:
        # Screen Resolution
        api_response = api_instance.screen_resolution()
        print("The response of DefaultApi->screen_resolution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->screen_resolution: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ScreenResolutionsResponse**](ScreenResolutionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | List of available screen resolutions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_profiles**
> ProfileSearchQueryResponse search_profiles(profile_search_criteria)

Search Profiles

Search profiles based on the search request

### Example


```python
import pm_api
from pm_api.models.profile_search_criteria import ProfileSearchCriteria
from pm_api.models.profile_search_query_response import ProfileSearchQueryResponse
from pm_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pm_api.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pm_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pm_api.DefaultApi(api_client)
    profile_search_criteria = pm_api.ProfileSearchCriteria() # ProfileSearchCriteria | 

    try:
        # Search Profiles
        api_response = api_instance.search_profiles(profile_search_criteria)
        print("The response of DefaultApi->search_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->search_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_search_criteria** | [**ProfileSearchCriteria**](ProfileSearchCriteria.md)|  | 

### Return type

[**ProfileSearchQueryResponse**](ProfileSearchQueryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Response message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **summary**
> FingerprintDataResponse summary(meta_id)

Summary

Baked profile without metadata to show in profile summary

### Example


```python
import pm_api
from pm_api.models.fingerprint_data_response import FingerprintDataResponse
from pm_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pm_api.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pm_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pm_api.DefaultApi(api_client)
    meta_id = 'meta_id_example' # str | ID of the profile meta

    try:
        # Summary
        api_response = api_instance.summary(meta_id)
        print("The response of DefaultApi->summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meta_id** | **str**| ID of the profile meta | 

### Return type

[**FingerprintDataResponse**](FingerprintDataResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Baked browser profiles that are ready to start |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

