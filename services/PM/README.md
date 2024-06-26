# pm-api
Multilogin X Profile Management API allows you to manage profiles.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Generator version: 7.5.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [http://www.mlx.yt](http://www.mlx.yt)

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import pm_api
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import pm_api
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import pm_api
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
    except ApiException as e:
        print("Exception when calling DefaultApi->baked: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.multilogin.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**baked**](docs/DefaultApi.md#baked) | **GET** /profile/baked | Baked
*DefaultApi* | [**create_extensions**](docs/DefaultApi.md#create_extensions) | **POST** /extensions/create | Store Browser Extensions for Workspace
*DefaultApi* | [**get_extensions**](docs/DefaultApi.md#get_extensions) | **GET** /extensions | Retrieve Browser Extensions for Workspace
*DefaultApi* | [**network_create**](docs/DefaultApi.md#network_create) | **POST** /network/create | Network Create
*DefaultApi* | [**network_remove**](docs/DefaultApi.md#network_remove) | **POST** /network/remove | Network Remove
*DefaultApi* | [**networks**](docs/DefaultApi.md#networks) | **GET** /network | Networks
*DefaultApi* | [**partial_profile_update**](docs/DefaultApi.md#partial_profile_update) | **POST** /profile/partial_update | Partial Profile Update
*DefaultApi* | [**profile_auto_update_core**](docs/DefaultApi.md#profile_auto_update_core) | **POST** /profile/auto_update_core | Profile Auto Update Core
*DefaultApi* | [**profile_clone**](docs/DefaultApi.md#profile_clone) | **POST** /profile/clone | Profile Clone
*DefaultApi* | [**profile_count_by_workspace**](docs/DefaultApi.md#profile_count_by_workspace) | **GET** /profile/workspace_count | Profile Count By Workspace
*DefaultApi* | [**profile_create**](docs/DefaultApi.md#profile_create) | **POST** /profile/create | Profile Create
*DefaultApi* | [**profile_fingerprints**](docs/DefaultApi.md#profile_fingerprints) | **POST** /profile/fingerprints | Profile Fingerprints
*DefaultApi* | [**profile_meta_ids_by_workspace_folder**](docs/DefaultApi.md#profile_meta_ids_by_workspace_folder) | **GET** /profile/workspace_meta_ids | Profile Meta IDs By Workspace Folder
*DefaultApi* | [**profile_metas**](docs/DefaultApi.md#profile_metas) | **POST** /profile/metas | Profile Metas
*DefaultApi* | [**profile_move**](docs/DefaultApi.md#profile_move) | **POST** /profile/move | Profile Move
*DefaultApi* | [**profile_quick**](docs/DefaultApi.md#profile_quick) | **POST** /profile/quick | Quick Profile
*DefaultApi* | [**profile_remove**](docs/DefaultApi.md#profile_remove) | **POST** /profile/remove | Profile Remove
*DefaultApi* | [**profile_restore**](docs/DefaultApi.md#profile_restore) | **POST** /profile/restore | Profile Restore
*DefaultApi* | [**profile_update**](docs/DefaultApi.md#profile_update) | **POST** /profile/update | Profile Update
*DefaultApi* | [**remove_extensions**](docs/DefaultApi.md#remove_extensions) | **DELETE** /extensions/remove | Remove Browser Extensions for Workspace
*DefaultApi* | [**screen_resolution**](docs/DefaultApi.md#screen_resolution) | **GET** /fpb/resolutions | Screen Resolution
*DefaultApi* | [**search_profiles**](docs/DefaultApi.md#search_profiles) | **POST** /profile/search | Search Profiles
*DefaultApi* | [**summary**](docs/DefaultApi.md#summary) | **GET** /profile/summary | Summary


## Documentation For Models

 - [AllowedScreenResolutions](docs/AllowedScreenResolutions.md)
 - [ArrayOfIDs](docs/ArrayOfIDs.md)
 - [ArrayOfIDsResponse](docs/ArrayOfIDsResponse.md)
 - [AutoUpdateCoreProfiles](docs/AutoUpdateCoreProfiles.md)
 - [BrowserExtension](docs/BrowserExtension.md)
 - [BrowserExtensionList](docs/BrowserExtensionList.md)
 - [BrowserType](docs/BrowserType.md)
 - [CloneProfile](docs/CloneProfile.md)
 - [CmdParam](docs/CmdParam.md)
 - [CmdParams](docs/CmdParams.md)
 - [CreateNetwork](docs/CreateNetwork.md)
 - [CreateProfile](docs/CreateProfile.md)
 - [CreateSingleObject](docs/CreateSingleObject.md)
 - [CreateSingleObjectResponse](docs/CreateSingleObjectResponse.md)
 - [ExtensionsCreate](docs/ExtensionsCreate.md)
 - [Fingerprint](docs/Fingerprint.md)
 - [FingerprintArray](docs/FingerprintArray.md)
 - [FingerprintArrayResponse](docs/FingerprintArrayResponse.md)
 - [FingerprintData](docs/FingerprintData.md)
 - [FingerprintDataResponse](docs/FingerprintDataResponse.md)
 - [Geolocation](docs/Geolocation.md)
 - [GetProfileParts](docs/GetProfileParts.md)
 - [Graphic](docs/Graphic.md)
 - [ListOfStringIDs](docs/ListOfStringIDs.md)
 - [Localization](docs/Localization.md)
 - [MLXResponse](docs/MLXResponse.md)
 - [MaskingCD](docs/MaskingCD.md)
 - [MaskingMN](docs/MaskingMN.md)
 - [MaskingNCM](docs/MaskingNCM.md)
 - [MaskingNCMD](docs/MaskingNCMD.md)
 - [MaskingND](docs/MaskingND.md)
 - [MaskingPAB](docs/MaskingPAB.md)
 - [MediaDevices](docs/MediaDevices.md)
 - [MoveProfile](docs/MoveProfile.md)
 - [Navigator](docs/Navigator.md)
 - [Network](docs/Network.md)
 - [NetworkArray](docs/NetworkArray.md)
 - [NetworkArrayResponse](docs/NetworkArrayResponse.md)
 - [PartialProfileMetaUpdateParams](docs/PartialProfileMetaUpdateParams.md)
 - [PartialUpdateProfile](docs/PartialUpdateProfile.md)
 - [ProfileMeta](docs/ProfileMeta.md)
 - [ProfileMetaArray](docs/ProfileMetaArray.md)
 - [ProfileMetaArrayResponse](docs/ProfileMetaArrayResponse.md)
 - [ProfileMetaCore](docs/ProfileMetaCore.md)
 - [ProfileMetaFlags](docs/ProfileMetaFlags.md)
 - [ProfileMetaFlagsOptional](docs/ProfileMetaFlagsOptional.md)
 - [ProfileMetaInternal](docs/ProfileMetaInternal.md)
 - [ProfileMetaPAM](docs/ProfileMetaPAM.md)
 - [ProfileMetaUpdate](docs/ProfileMetaUpdate.md)
 - [ProfileMetaUpdateParams](docs/ProfileMetaUpdateParams.md)
 - [ProfileSearchCriteria](docs/ProfileSearchCriteria.md)
 - [ProfileSearchQuery](docs/ProfileSearchQuery.md)
 - [ProfileSearchQueryItem](docs/ProfileSearchQueryItem.md)
 - [ProfileSearchQueryResponse](docs/ProfileSearchQueryResponse.md)
 - [ProfilesCount](docs/ProfilesCount.md)
 - [ProfilesCountResponse](docs/ProfilesCountResponse.md)
 - [Proxy](docs/Proxy.md)
 - [QuickProfile](docs/QuickProfile.md)
 - [QuickProfileMetaParams](docs/QuickProfileMetaParams.md)
 - [ReadyProfile](docs/ReadyProfile.md)
 - [ReadyProfileCore](docs/ReadyProfileCore.md)
 - [ReadyProfileResponse](docs/ReadyProfileResponse.md)
 - [RemoveNetwork](docs/RemoveNetwork.md)
 - [RemoveProfiles](docs/RemoveProfiles.md)
 - [ResponseStatus](docs/ResponseStatus.md)
 - [RestoreProfiles](docs/RestoreProfiles.md)
 - [Screen](docs/Screen.md)
 - [ScreenResolution](docs/ScreenResolution.md)
 - [ScreenResolutions](docs/ScreenResolutions.md)
 - [ScreenResolutionsResponse](docs/ScreenResolutionsResponse.md)
 - [Storage](docs/Storage.md)
 - [Timezone](docs/Timezone.md)
 - [UpdateProfile](docs/UpdateProfile.md)
 - [Webrtc](docs/Webrtc.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author

support@multilogin.com


