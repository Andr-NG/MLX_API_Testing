# pam_api_client.DefaultApi

All URIs are relative to *https://api.multilogin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**folder_add_user**](DefaultApi.md#folder_add_user) | **POST** /folder/user_add | Folder Add User
[**folder_remove_user**](DefaultApi.md#folder_remove_user) | **POST** /folder/user_remove | Folder Remove User
[**folder_users**](DefaultApi.md#folder_users) | **GET** /folder/users | Folder Users
[**get_workspace_restrictions**](DefaultApi.md#get_workspace_restrictions) | **GET** /workspace/restrictions | Get Workspace Restrictions
[**s_so_signin**](DefaultApi.md#s_so_signin) | **POST** /sso/signin | SSO Signin
[**set_user_settings**](DefaultApi.md#set_user_settings) | **POST** /user/settings | Set User Settings
[**user_change_password**](DefaultApi.md#user_change_password) | **POST** /user/change_password | User Change Password
[**user_forgot_password**](DefaultApi.md#user_forgot_password) | **POST** /user/forgot_password | User Forgot Password
[**user_get_billing_url**](DefaultApi.md#user_get_billing_url) | **GET** /user/get_billing_url | Get Billing Url
[**user_identity**](DefaultApi.md#user_identity) | **GET** /user/identity | User identity
[**user_launcher_signin**](DefaultApi.md#user_launcher_signin) | **POST** /user/launcher_signin | (Private API) Launcher signin
[**user_refresh_token**](DefaultApi.md#user_refresh_token) | **POST** /user/refresh_token | User Refresh Token
[**user_resend_verification**](DefaultApi.md#user_resend_verification) | **GET** /user/resend_verification | Resend Verification
[**user_reset_password**](DefaultApi.md#user_reset_password) | **POST** /user/reset_password | User Reset Password
[**user_revoke_tokens**](DefaultApi.md#user_revoke_tokens) | **POST** /user/revoke_tokens | Revoke user tokens
[**user_settings**](DefaultApi.md#user_settings) | **GET** /user/settings | User Settings
[**user_signin**](DefaultApi.md#user_signin) | **POST** /user/signin | User Signin
[**user_signup**](DefaultApi.md#user_signup) | **POST** /user/signup | User Signup
[**user_tokens_list**](DefaultApi.md#user_tokens_list) | **GET** /user/tokens_list | Return all active tokens with expiration date that belongs to account
[**user_verify_email**](DefaultApi.md#user_verify_email) | **GET** /user/verify_email | User Verify Email
[**user_workspaces**](DefaultApi.md#user_workspaces) | **GET** /user/workspaces | User Workspaces
[**workspace_add_user**](DefaultApi.md#workspace_add_user) | **POST** /workspace/user_add | Workspace AddUser
[**workspace_automation_token**](DefaultApi.md#workspace_automation_token) | **GET** /workspace/automation_token | Workspace Automation Token
[**workspace_change_user_role**](DefaultApi.md#workspace_change_user_role) | **POST** /workspace/user_change_role | Workspace Change UserRole
[**workspace_create**](DefaultApi.md#workspace_create) | **POST** /workspace/create | Workspace Create
[**workspace_create_folder**](DefaultApi.md#workspace_create_folder) | **POST** /workspace/folder_create | Workspace Create Folder
[**workspace_folders**](DefaultApi.md#workspace_folders) | **GET** /workspace/folders | Workspace Folders
[**workspace_folders_for_user**](DefaultApi.md#workspace_folders_for_user) | **GET** /workspace/folders_for_user | Workspace Folders For User
[**workspace_get_key**](DefaultApi.md#workspace_get_key) | **GET** /pam/workspace/key | WorkspaceGetKey
[**workspace_invitations**](DefaultApi.md#workspace_invitations) | **GET** /workspace/invitations | Workspace Invitations
[**workspace_join**](DefaultApi.md#workspace_join) | **GET** /workspace/join | Workspace Join
[**workspace_leave**](DefaultApi.md#workspace_leave) | **POST** /workspace/leave | Workspace Leave
[**workspace_remove**](DefaultApi.md#workspace_remove) | **POST** /workspace/remove | Workspace Remove
[**workspace_remove_folders**](DefaultApi.md#workspace_remove_folders) | **POST** /workspace/folders_remove | Workspace Remove Folders
[**workspace_remove_user**](DefaultApi.md#workspace_remove_user) | **POST** /workspace/user_remove | Workspace RemoveUser
[**workspace_send_invite**](DefaultApi.md#workspace_send_invite) | **POST** /workspace/send_invite | Workspace SendInvite
[**workspace_stats**](DefaultApi.md#workspace_stats) | **GET** /workspace/statistics | Workspace Stats
[**workspace_update_folder**](DefaultApi.md#workspace_update_folder) | **POST** /workspace/folder_update | Workspace Update Folder
[**workspace_user_balance**](DefaultApi.md#workspace_user_balance) | **GET** /workspace/user_balance | Workspace User Balance
[**workspace_users**](DefaultApi.md#workspace_users) | **GET** /workspace/users | Workspace Users


# **folder_add_user**
> MLXResponse folder_add_user(add_user_to_folder)

Folder Add User

Add a new user into folder

### Example


```python
import pam_api_client
from pam_api_client.models.add_user_to_folder import AddUserToFolder
from pam_api_client.models.mlx_response import MLXResponse
from pam_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pam_api_client.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pam_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pam_api_client.DefaultApi(api_client)
    add_user_to_folder = pam_api_client.AddUserToFolder() # AddUserToFolder | Information about new user of folder

    try:
        # Folder Add User
        api_response = api_instance.folder_add_user(add_user_to_folder)
        print("The response of DefaultApi->folder_add_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->folder_add_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_user_to_folder** | [**AddUserToFolder**](AddUserToFolder.md)| Information about new user of folder | 

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

# **folder_remove_user**
> MLXResponse folder_remove_user(remove_user_from_folder)

Folder Remove User

Remove an user from folder

### Example


```python
import pam_api_client
from pam_api_client.models.mlx_response import MLXResponse
from pam_api_client.models.remove_user_from_folder import RemoveUserFromFolder
from pam_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pam_api_client.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pam_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pam_api_client.DefaultApi(api_client)
    remove_user_from_folder = pam_api_client.RemoveUserFromFolder() # RemoveUserFromFolder | Information about the removed user of folder

    try:
        # Folder Remove User
        api_response = api_instance.folder_remove_user(remove_user_from_folder)
        print("The response of DefaultApi->folder_remove_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->folder_remove_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remove_user_from_folder** | [**RemoveUserFromFolder**](RemoveUserFromFolder.md)| Information about the removed user of folder | 

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

# **folder_users**
> FolderUserArrayResponse folder_users(folder_id, limit, offset)

Folder Users

Get list of users for folder

### Example


```python
import pam_api_client
from pam_api_client.models.folder_user_array_response import FolderUserArrayResponse
from pam_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pam_api_client.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pam_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pam_api_client.DefaultApi(api_client)
    folder_id = 'folder_id_example' # str | Folder ID.
    limit = 56 # int | Amount of users.
    offset = 56 # int | Offset says to skip that many rows.

    try:
        # Folder Users
        api_response = api_instance.folder_users(folder_id, limit, offset)
        print("The response of DefaultApi->folder_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->folder_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**| Folder ID. | 
 **limit** | **int**| Amount of users. | 
 **offset** | **int**| Offset says to skip that many rows. | 

### Return type

[**FolderUserArrayResponse**](FolderUserArrayResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | List of available users by folder ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace_restrictions**
> GetRestriction get_workspace_restrictions()

Get Workspace Restrictions

Get workspace restriction which is currently in use

### Example


```python
import pam_api_client
from pam_api_client.models.get_restriction import GetRestriction
from pam_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pam_api_client.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pam_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pam_api_client.DefaultApi(api_client)

    try:
        # Get Workspace Restrictions
        api_response = api_instance.get_workspace_restrictions()
        print("The response of DefaultApi->get_workspace_restrictions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_workspace_restrictions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetRestriction**](GetRestriction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Message with restrictions data. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **s_so_signin**
> SSOResponse s_so_signin(user_creds)

SSO Signin

(Private) SSO signin

### Example


```python
import pam_api_client
from pam_api_client.models.sso_response import SSOResponse
from pam_api_client.models.user_creds import UserCreds
from pam_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pam_api_client.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pam_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pam_api_client.DefaultApi(api_client)
    user_creds = pam_api_client.UserCreds() # UserCreds | Email and password of user

    try:
        # SSO Signin
        api_response = api_instance.s_so_signin(user_creds)
        print("The response of DefaultApi->s_so_signin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->s_so_signin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_creds** | [**UserCreds**](UserCreds.md)| Email and password of user | 

### Return type

[**SSOResponse**](SSOResponse.md)

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

# **set_user_settings**
> MLXResponse set_user_settings(settings)

Set User Settings

Set user settings

### Example


```python
import pam_api_client
from pam_api_client.models.mlx_response import MLXResponse
from pam_api_client.models.settings import Settings
from pam_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pam_api_client.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pam_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pam_api_client.DefaultApi(api_client)
    settings = pam_api_client.Settings() # Settings | Update user settings

    try:
        # Set User Settings
        api_response = api_instance.set_user_settings(settings)
        print("The response of DefaultApi->set_user_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->set_user_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings** | [**Settings**](Settings.md)| Update user settings | 

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

# **user_change_password**
> MLXResponse user_change_password(change_password)

User Change Password

Change password of user

### Example


```python
import pam_api_client
from pam_api_client.models.change_password import ChangePassword
from pam_api_client.models.mlx_response import MLXResponse
from pam_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pam_api_client.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pam_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pam_api_client.DefaultApi(api_client)
    change_password = pam_api_client.ChangePassword() # ChangePassword | Current and new password for the user

    try:
        # User Change Password
        api_response = api_instance.user_change_password(change_password)
        print("The response of DefaultApi->user_change_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->user_change_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_password** | [**ChangePassword**](ChangePassword.md)| Current and new password for the user | 

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

# **user_forgot_password**
> MLXResponse user_forgot_password(forgot_password)

User Forgot Password

Forgot password of user

### Example


```python
import pam_api_client
from pam_api_client.models.forgot_password import ForgotPassword
from pam_api_client.models.mlx_response import MLXResponse
from pam_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pam_api_client.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pam_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pam_api_client.DefaultApi(api_client)
    forgot_password = pam_api_client.ForgotPassword() # ForgotPassword | E-mail of user who forgot the password

    try:
        # User Forgot Password
        api_response = api_instance.user_forgot_password(forgot_password)
        print("The response of DefaultApi->user_forgot_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->user_forgot_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forgot_password** | [**ForgotPassword**](ForgotPassword.md)| E-mail of user who forgot the password | 

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

# **user_get_billing_url**
> BillingURLResponse user_get_billing_url()

Get Billing Url

Get billing url

### Example


```python
import pam_api_client
from pam_api_client.models.billing_url_response import BillingURLResponse
from pam_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pam_api_client.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pam_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pam_api_client.DefaultApi(api_client)

    try:
        # Get Billing Url
        api_response = api_instance.user_get_billing_url()
        print("The response of DefaultApi->user_get_billing_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->user_get_billing_url: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BillingURLResponse**](BillingURLResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Response message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_identity**
> UserIdentityResponse user_identity()

User identity

Return user identity for user

### Example


```python
import pam_api_client
from pam_api_client.models.user_identity_response import UserIdentityResponse
from pam_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pam_api_client.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pam_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pam_api_client.DefaultApi(api_client)

    try:
        # User identity
        api_response = api_instance.user_identity()
        print("The response of DefaultApi->user_identity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->user_identity: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserIdentityResponse**](UserIdentityResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Response message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_launcher_signin**
> SigninResponse user_launcher_signin(launcher_signin_request)

(Private API) Launcher signin

Launcher signin

### Example


```python
import pam_api_client
from pam_api_client.models.launcher_signin_request import LauncherSigninRequest
from pam_api_client.models.signin_response import SigninResponse
from pam_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pam_api_client.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pam_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pam_api_client.DefaultApi(api_client)
    launcher_signin_request = pam_api_client.LauncherSigninRequest() # LauncherSigninRequest | Metadata about user machine

    try:
        # (Private API) Launcher signin
        api_response = api_instance.user_launcher_signin(launcher_signin_request)
        print("The response of DefaultApi->user_launcher_signin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->user_launcher_signin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **launcher_signin_request** | [**LauncherSigninRequest**](LauncherSigninRequest.md)| Metadata about user machine | 

### Return type

[**SigninResponse**](SigninResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Response with new JWT details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_refresh_token**
> SigninResponse user_refresh_token(refresh_token)

User Refresh Token

Update JWT token

### Example


```python
import pam_api_client
from pam_api_client.models.refresh_token import RefreshToken
from pam_api_client.models.signin_response import SigninResponse
from pam_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pam_api_client.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pam_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pam_api_client.DefaultApi(api_client)
    refresh_token = pam_api_client.RefreshToken() # RefreshToken | Email and refresh token of user

    try:
        # User Refresh Token
        api_response = api_instance.user_refresh_token(refresh_token)
        print("The response of DefaultApi->user_refresh_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->user_refresh_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_token** | [**RefreshToken**](RefreshToken.md)| Email and refresh token of user | 

### Return type

[**SigninResponse**](SigninResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Response with new JWT details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_resend_verification**
> MLXResponse user_resend_verification()

Resend Verification

Resend Verification

### Example


```python
import pam_api_client
from pam_api_client.models.mlx_response import MLXResponse
from pam_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pam_api_client.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pam_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pam_api_client.DefaultApi(api_client)

    try:
        # Resend Verification
        api_response = api_instance.user_resend_verification()
        print("The response of DefaultApi->user_resend_verification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->user_resend_verification: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**MLXResponse**](MLXResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Response message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_reset_password**
> MLXResponse user_reset_password(reset_password)

User Reset Password

Reset password of user

### Example


```python
import pam_api_client
from pam_api_client.models.mlx_response import MLXResponse
from pam_api_client.models.reset_password import ResetPassword
from pam_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pam_api_client.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pam_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pam_api_client.DefaultApi(api_client)
    reset_password = pam_api_client.ResetPassword() # ResetPassword | E-mail with password and reset_token of the user

    try:
        # User Reset Password
        api_response = api_instance.user_reset_password(reset_password)
        print("The response of DefaultApi->user_reset_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->user_reset_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reset_password** | [**ResetPassword**](ResetPassword.md)| E-mail with password and reset_token of the user | 

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

# **user_revoke_tokens**
> MLXResponse user_revoke_tokens(revoke_token_request)

Revoke user tokens

Revoking user tokens

### Example


```python
import pam_api_client
from pam_api_client.models.mlx_response import MLXResponse
from pam_api_client.models.revoke_token_request import RevokeTokenRequest
from pam_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pam_api_client.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pam_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pam_api_client.DefaultApi(api_client)
    revoke_token_request = pam_api_client.RevokeTokenRequest() # RevokeTokenRequest | 

    try:
        # Revoke user tokens
        api_response = api_instance.user_revoke_tokens(revoke_token_request)
        print("The response of DefaultApi->user_revoke_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->user_revoke_tokens: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **revoke_token_request** | [**RevokeTokenRequest**](RevokeTokenRequest.md)|  | 

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

# **user_settings**
> UserSettingsResponse user_settings()

User Settings

Get user settings

### Example


```python
import pam_api_client
from pam_api_client.models.user_settings_response import UserSettingsResponse
from pam_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pam_api_client.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pam_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pam_api_client.DefaultApi(api_client)

    try:
        # User Settings
        api_response = api_instance.user_settings()
        print("The response of DefaultApi->user_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->user_settings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserSettingsResponse**](UserSettingsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | User settings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_signin**
> SigninResponse user_signin(user_creds)

User Signin

Login into mlx

### Example


```python
import pam_api_client
from pam_api_client.models.signin_response import SigninResponse
from pam_api_client.models.user_creds import UserCreds
from pam_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pam_api_client.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pam_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pam_api_client.DefaultApi(api_client)
    user_creds = pam_api_client.UserCreds() # UserCreds | Email and password (md5 hashed) of user

    try:
        # User Signin
        api_response = api_instance.user_signin(user_creds)
        print("The response of DefaultApi->user_signin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->user_signin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_creds** | [**UserCreds**](UserCreds.md)| Email and password (md5 hashed) of user | 

### Return type

[**SigninResponse**](SigninResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Successful login with JWT details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_signup**
> MLXResponse user_signup(complex_signup)

User Signup

Add a new user

### Example


```python
import pam_api_client
from pam_api_client.models.complex_signup import ComplexSignup
from pam_api_client.models.mlx_response import MLXResponse
from pam_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pam_api_client.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pam_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pam_api_client.DefaultApi(api_client)
    complex_signup = pam_api_client.ComplexSignup() # ComplexSignup | Email and password (minimum 7 symbols with different cases, numbers and special symbols) for new user

    try:
        # User Signup
        api_response = api_instance.user_signup(complex_signup)
        print("The response of DefaultApi->user_signup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->user_signup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **complex_signup** | [**ComplexSignup**](ComplexSignup.md)| Email and password (minimum 7 symbols with different cases, numbers and special symbols) for new user | 

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

# **user_tokens_list**
> TokenListResponse user_tokens_list()

Return all active tokens with expiration date that belongs to account

Return all active tokens with expiration date that belongs to account

### Example


```python
import pam_api_client
from pam_api_client.models.token_list_response import TokenListResponse
from pam_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pam_api_client.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pam_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pam_api_client.DefaultApi(api_client)

    try:
        # Return all active tokens with expiration date that belongs to account
        api_response = api_instance.user_tokens_list()
        print("The response of DefaultApi->user_tokens_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->user_tokens_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**TokenListResponse**](TokenListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_verify_email**
> MLXResponse user_verify_email(token)

User Verify Email

Email Address Verification API

### Example


```python
import pam_api_client
from pam_api_client.models.mlx_response import MLXResponse
from pam_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pam_api_client.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pam_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pam_api_client.DefaultApi(api_client)
    token = 'token_example' # str | Verification token

    try:
        # User Verify Email
        api_response = api_instance.user_verify_email(token)
        print("The response of DefaultApi->user_verify_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->user_verify_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Verification token | 

### Return type

[**MLXResponse**](MLXResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Response message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_workspaces**
> UserWorkspaceArrayResponse user_workspaces()

User Workspaces

Get list of workspaces for the user

### Example


```python
import pam_api_client
from pam_api_client.models.user_workspace_array_response import UserWorkspaceArrayResponse
from pam_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pam_api_client.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pam_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pam_api_client.DefaultApi(api_client)

    try:
        # User Workspaces
        api_response = api_instance.user_workspaces()
        print("The response of DefaultApi->user_workspaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->user_workspaces: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserWorkspaceArrayResponse**](UserWorkspaceArrayResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | List with information about workspaces |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workspace_add_user**
> MLXResponse workspace_add_user(add_user_to_workspace)

Workspace AddUser

Add a new user into workspace

### Example


```python
import pam_api_client
from pam_api_client.models.add_user_to_workspace import AddUserToWorkspace
from pam_api_client.models.mlx_response import MLXResponse
from pam_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pam_api_client.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pam_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pam_api_client.DefaultApi(api_client)
    add_user_to_workspace = pam_api_client.AddUserToWorkspace() # AddUserToWorkspace | Information about new user of workspace

    try:
        # Workspace AddUser
        api_response = api_instance.workspace_add_user(add_user_to_workspace)
        print("The response of DefaultApi->workspace_add_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->workspace_add_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_user_to_workspace** | [**AddUserToWorkspace**](AddUserToWorkspace.md)| Information about new user of workspace | 

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

# **workspace_automation_token**
> AutomationTokenResponse workspace_automation_token(expiration_period=expiration_period)

Workspace Automation Token

Get automation token

### Example


```python
import pam_api_client
from pam_api_client.models.automation_token_response import AutomationTokenResponse
from pam_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pam_api_client.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pam_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pam_api_client.DefaultApi(api_client)
    expiration_period = 'expiration_period_example' # str | Expiration period (1h, 3h, 5h, 16h, 24h, 48h, 1w, 2w, 3w, 1mo, no_exp) (optional)

    try:
        # Workspace Automation Token
        api_response = api_instance.workspace_automation_token(expiration_period=expiration_period)
        print("The response of DefaultApi->workspace_automation_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->workspace_automation_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expiration_period** | **str**| Expiration period (1h, 3h, 5h, 16h, 24h, 48h, 1w, 2w, 3w, 1mo, no_exp) | [optional] 

### Return type

[**AutomationTokenResponse**](AutomationTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Developer token. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workspace_change_user_role**
> MLXResponse workspace_change_user_role(add_user_to_workspace)

Workspace Change UserRole

Change role of user in workspace

### Example


```python
import pam_api_client
from pam_api_client.models.add_user_to_workspace import AddUserToWorkspace
from pam_api_client.models.mlx_response import MLXResponse
from pam_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pam_api_client.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pam_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pam_api_client.DefaultApi(api_client)
    add_user_to_workspace = pam_api_client.AddUserToWorkspace() # AddUserToWorkspace | Information about new role of exists user

    try:
        # Workspace Change UserRole
        api_response = api_instance.workspace_change_user_role(add_user_to_workspace)
        print("The response of DefaultApi->workspace_change_user_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->workspace_change_user_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_user_to_workspace** | [**AddUserToWorkspace**](AddUserToWorkspace.md)| Information about new role of exists user | 

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

# **workspace_create**
> CreateSingleObjectResponse workspace_create()

Workspace Create

Create new workspace

### Example


```python
import pam_api_client
from pam_api_client.models.create_single_object_response import CreateSingleObjectResponse
from pam_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pam_api_client.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pam_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pam_api_client.DefaultApi(api_client)

    try:
        # Workspace Create
        api_response = api_instance.workspace_create()
        print("The response of DefaultApi->workspace_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->workspace_create: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CreateSingleObjectResponse**](CreateSingleObjectResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Information about created workspace |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workspace_create_folder**
> CreateSingleObjectResponse workspace_create_folder(create_folder)

Workspace Create Folder

Add a new folder

### Example


```python
import pam_api_client
from pam_api_client.models.create_folder import CreateFolder
from pam_api_client.models.create_single_object_response import CreateSingleObjectResponse
from pam_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pam_api_client.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pam_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pam_api_client.DefaultApi(api_client)
    create_folder = pam_api_client.CreateFolder() # CreateFolder | Parameters of new folder

    try:
        # Workspace Create Folder
        api_response = api_instance.workspace_create_folder(create_folder)
        print("The response of DefaultApi->workspace_create_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->workspace_create_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_folder** | [**CreateFolder**](CreateFolder.md)| Parameters of new folder | 

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
**0** | Response message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workspace_folders**
> UserFolderArrayResponse workspace_folders()

Workspace Folders

Get list of available folders by workspace ID

### Example


```python
import pam_api_client
from pam_api_client.models.user_folder_array_response import UserFolderArrayResponse
from pam_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pam_api_client.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pam_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pam_api_client.DefaultApi(api_client)

    try:
        # Workspace Folders
        api_response = api_instance.workspace_folders()
        print("The response of DefaultApi->workspace_folders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->workspace_folders: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserFolderArrayResponse**](UserFolderArrayResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | List of available folders by workspace ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workspace_folders_for_user**
> UserFolderArrayResponse workspace_folders_for_user(email)

Workspace Folders For User

Get list of available folders by workspace ID and user email

### Example


```python
import pam_api_client
from pam_api_client.models.user_folder_array_response import UserFolderArrayResponse
from pam_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pam_api_client.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pam_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pam_api_client.DefaultApi(api_client)
    email = 'email_example' # str | E-mail of user

    try:
        # Workspace Folders For User
        api_response = api_instance.workspace_folders_for_user(email)
        print("The response of DefaultApi->workspace_folders_for_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->workspace_folders_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| E-mail of user | 

### Return type

[**UserFolderArrayResponse**](UserFolderArrayResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | List of available folders by workspace ID and user email |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workspace_get_key**
> WorkspaceKeyResponse workspace_get_key(workspace_get_key)

WorkspaceGetKey

Get base64 encodded workspace data encryption currently active key

### Example


```python
import pam_api_client
from pam_api_client.models.workspace_get_key import WorkspaceGetKey
from pam_api_client.models.workspace_key_response import WorkspaceKeyResponse
from pam_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pam_api_client.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pam_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pam_api_client.DefaultApi(api_client)
    workspace_get_key = pam_api_client.WorkspaceGetKey() # WorkspaceGetKey | Key pair query details

    try:
        # WorkspaceGetKey
        api_response = api_instance.workspace_get_key(workspace_get_key)
        print("The response of DefaultApi->workspace_get_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->workspace_get_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_get_key** | [**WorkspaceGetKey**](WorkspaceGetKey.md)| Key pair query details | 

### Return type

[**WorkspaceKeyResponse**](WorkspaceKeyResponse.md)

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

# **workspace_invitations**
> WorkspaceInvitationsArrayResponse workspace_invitations(limit, offset)

Workspace Invitations

Workspace invitations

### Example


```python
import pam_api_client
from pam_api_client.models.workspace_invitations_array_response import WorkspaceInvitationsArrayResponse
from pam_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pam_api_client.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pam_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pam_api_client.DefaultApi(api_client)
    limit = 56 # int | Amount of invitations for the workspace
    offset = 56 # int | Offset says to skip that many rows.

    try:
        # Workspace Invitations
        api_response = api_instance.workspace_invitations(limit, offset)
        print("The response of DefaultApi->workspace_invitations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->workspace_invitations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Amount of invitations for the workspace | 
 **offset** | **int**| Offset says to skip that many rows. | 

### Return type

[**WorkspaceInvitationsArrayResponse**](WorkspaceInvitationsArrayResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Response message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workspace_join**
> MLXResponse workspace_join(email, workspace_id, role, token)

Workspace Join

Workspace invitation verification

### Example


```python
import pam_api_client
from pam_api_client.models.mlx_response import MLXResponse
from pam_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pam_api_client.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pam_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pam_api_client.DefaultApi(api_client)
    email = 'email_example' # str | E-mail of user
    workspace_id = 'workspace_id_example' # str | ID of workspace
    role = 'role_example' # str | Role of user in workspace
    token = 'token_example' # str | Verification token

    try:
        # Workspace Join
        api_response = api_instance.workspace_join(email, workspace_id, role, token)
        print("The response of DefaultApi->workspace_join:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->workspace_join: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| E-mail of user | 
 **workspace_id** | **str**| ID of workspace | 
 **role** | **str**| Role of user in workspace | 
 **token** | **str**| Verification token | 

### Return type

[**MLXResponse**](MLXResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Response message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workspace_leave**
> MLXResponse workspace_leave(leave_workspace)

Workspace Leave

Leave workspace

### Example


```python
import pam_api_client
from pam_api_client.models.leave_workspace import LeaveWorkspace
from pam_api_client.models.mlx_response import MLXResponse
from pam_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pam_api_client.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pam_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pam_api_client.DefaultApi(api_client)
    leave_workspace = pam_api_client.LeaveWorkspace() # LeaveWorkspace | Id of workspace for leaving

    try:
        # Workspace Leave
        api_response = api_instance.workspace_leave(leave_workspace)
        print("The response of DefaultApi->workspace_leave:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->workspace_leave: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **leave_workspace** | [**LeaveWorkspace**](LeaveWorkspace.md)| Id of workspace for leaving | 

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

# **workspace_remove**
> MLXResponse workspace_remove(remove_workspace)

Workspace Remove

Remove workspace

### Example


```python
import pam_api_client
from pam_api_client.models.mlx_response import MLXResponse
from pam_api_client.models.remove_workspace import RemoveWorkspace
from pam_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pam_api_client.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pam_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pam_api_client.DefaultApi(api_client)
    remove_workspace = pam_api_client.RemoveWorkspace() # RemoveWorkspace | Id of workspace for removing

    try:
        # Workspace Remove
        api_response = api_instance.workspace_remove(remove_workspace)
        print("The response of DefaultApi->workspace_remove:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->workspace_remove: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remove_workspace** | [**RemoveWorkspace**](RemoveWorkspace.md)| Id of workspace for removing | 

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

# **workspace_remove_folders**
> MLXResponse workspace_remove_folders(remove_folder)

Workspace Remove Folders

Remove workspace folders

### Example


```python
import pam_api_client
from pam_api_client.models.mlx_response import MLXResponse
from pam_api_client.models.remove_folder import RemoveFolder
from pam_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pam_api_client.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pam_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pam_api_client.DefaultApi(api_client)
    remove_folder = pam_api_client.RemoveFolder() # RemoveFolder | List with ids of folders for removing from selected workspace

    try:
        # Workspace Remove Folders
        api_response = api_instance.workspace_remove_folders(remove_folder)
        print("The response of DefaultApi->workspace_remove_folders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->workspace_remove_folders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remove_folder** | [**RemoveFolder**](RemoveFolder.md)| List with ids of folders for removing from selected workspace | 

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

# **workspace_remove_user**
> MLXResponse workspace_remove_user(remove_user_from_workspace)

Workspace RemoveUser

Remove an user from workspace

### Example


```python
import pam_api_client
from pam_api_client.models.mlx_response import MLXResponse
from pam_api_client.models.remove_user_from_workspace import RemoveUserFromWorkspace
from pam_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pam_api_client.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pam_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pam_api_client.DefaultApi(api_client)
    remove_user_from_workspace = pam_api_client.RemoveUserFromWorkspace() # RemoveUserFromWorkspace | Information about the removed user of workspace

    try:
        # Workspace RemoveUser
        api_response = api_instance.workspace_remove_user(remove_user_from_workspace)
        print("The response of DefaultApi->workspace_remove_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->workspace_remove_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remove_user_from_workspace** | [**RemoveUserFromWorkspace**](RemoveUserFromWorkspace.md)| Information about the removed user of workspace | 

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

# **workspace_send_invite**
> MLXResponse workspace_send_invite(workspace_send_invite)

Workspace SendInvite

Send invitation to join workspace

### Example


```python
import pam_api_client
from pam_api_client.models.mlx_response import MLXResponse
from pam_api_client.models.workspace_send_invite import WorkspaceSendInvite
from pam_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pam_api_client.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pam_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pam_api_client.DefaultApi(api_client)
    workspace_send_invite = pam_api_client.WorkspaceSendInvite() # WorkspaceSendInvite | Email of user and ID of workspace for joining

    try:
        # Workspace SendInvite
        api_response = api_instance.workspace_send_invite(workspace_send_invite)
        print("The response of DefaultApi->workspace_send_invite:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->workspace_send_invite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_send_invite** | [**WorkspaceSendInvite**](WorkspaceSendInvite.md)| Email of user and ID of workspace for joining | 

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

# **workspace_stats**
> WorkspaceStatsResponse workspace_stats()

Workspace Stats

Get basic statistics for workspace

### Example


```python
import pam_api_client
from pam_api_client.models.workspace_stats_response import WorkspaceStatsResponse
from pam_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pam_api_client.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pam_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pam_api_client.DefaultApi(api_client)

    try:
        # Workspace Stats
        api_response = api_instance.workspace_stats()
        print("The response of DefaultApi->workspace_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->workspace_stats: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WorkspaceStatsResponse**](WorkspaceStatsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Information about workspace like user counter and profile counters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workspace_update_folder**
> MLXResponse workspace_update_folder(update_folder)

Workspace Update Folder

Change the folder

### Example


```python
import pam_api_client
from pam_api_client.models.mlx_response import MLXResponse
from pam_api_client.models.update_folder import UpdateFolder
from pam_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pam_api_client.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pam_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pam_api_client.DefaultApi(api_client)
    update_folder = pam_api_client.UpdateFolder() # UpdateFolder | Parameters for changing name of folder

    try:
        # Workspace Update Folder
        api_response = api_instance.workspace_update_folder(update_folder)
        print("The response of DefaultApi->workspace_update_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->workspace_update_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_folder** | [**UpdateFolder**](UpdateFolder.md)| Parameters for changing name of folder | 

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

# **workspace_user_balance**
> WorkspaceUserBalanceResponse workspace_user_balance()

Workspace User Balance

Get user balance for selected workspace

### Example


```python
import pam_api_client
from pam_api_client.models.workspace_user_balance_response import WorkspaceUserBalanceResponse
from pam_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pam_api_client.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pam_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pam_api_client.DefaultApi(api_client)

    try:
        # Workspace User Balance
        api_response = api_instance.workspace_user_balance()
        print("The response of DefaultApi->workspace_user_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->workspace_user_balance: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WorkspaceUserBalanceResponse**](WorkspaceUserBalanceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Workspace user balance |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workspace_users**
> WorkspaceUserArrayResponse workspace_users(limit, offset)

Workspace Users

Get list of users for workspace

### Example


```python
import pam_api_client
from pam_api_client.models.workspace_user_array_response import WorkspaceUserArrayResponse
from pam_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.multilogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pam_api_client.Configuration(
    host = "https://api.multilogin.com"
)


# Enter a context with an instance of the API client
with pam_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pam_api_client.DefaultApi(api_client)
    limit = 56 # int | Amount of users in the workspace
    offset = 56 # int | Offset says to skip that many rows.

    try:
        # Workspace Users
        api_response = api_instance.workspace_users(limit, offset)
        print("The response of DefaultApi->workspace_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->workspace_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Amount of users in the workspace | 
 **offset** | **int**| Offset says to skip that many rows. | 

### Return type

[**WorkspaceUserArrayResponse**](WorkspaceUserArrayResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | List with information about users in workspace |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

