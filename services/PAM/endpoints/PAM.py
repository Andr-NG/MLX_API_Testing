import services.PAM.pam_api_client as pam
import json
from services.PAM.endpoints.base_endpoint import BaseEndpoint


class PAM(BaseEndpoint):

    def sign_in(self, login, user_pass):

        try:
            # Instantiating and setting up.
            mlx = self.create_api_client()
            creds = pam.UserCreds(email=login, password=user_pass)

            # Calling and validating the response against the model. Raises an error if wrong. # noqa: E501
            data = mlx.user_signin(user_creds=creds)
            response = pam.SigninResponse.model_validate(
                pam.SigninResponse.from_json(data)
            )
            assert response.status.http_code == 200, response
            data_to_env = {'TOKEN': response.data.token,
                           'REFRESH_TOKEN': response.data.refresh_token}

            # Saving the token and refresh token into the .env file.
            with open(r'D:\MLX\Projects\MLX_API\.env', 'w') as f:
                for key, value in data_to_env.items():
                    f.write(f"{key}={value}\n")

            return response

        except pam.ApiException as e:
            response = pam.ApiExceptionError(**json.loads(e.body))
            return response

    def sign_up(self, login, user_pass):

        # Instantiation the client.
        mlx = self.create_api_client()
        user_creds = pam.UserCreds(email=login, password=user_pass)
        body = pam.ComplexSignup(creds=user_creds)

        # Calling and validating the response against the model. Raises an error if wrong. # noqa: E501
        try:
            data = mlx.user_signup(complex_signup=body)
            response = pam.MLXResponse.model_validate(pam.MLXResponse.from_json(data))  # noqa: E501

            assert response.status.http_code == 201, response
            return response

        except pam.ApiException as e:
            response = pam.ApiExceptionError(**json.loads(e.body))
            return response

    def get_workspace_id(self, header=None):

        # Instantiate the client.
        mlx = self.create_api_client()
        if header is None:
            header = self._get_headers()
        elif header == 'invalid_token':
            header = {
                'Authorization': 'invalid_token'
            }

        # Calling and validating the response against the model. Raises an error if wrong. # noqa: E501
        try:
            data = mlx.user_workspaces(_headers=header)
            response = pam.UserWorkspaceArrayResponse.model_validate(
                pam.UserWorkspaceArrayResponse.from_json(data)
            )
            assert response.status.http_code == 200, response
            return response

        except pam.ApiException as e:
            response = pam.ApiExceptionError(**json.loads(e.body))
            return response

    def get_folder_id(self, headers=None):

        # Instantiate the client.
        mlx = self.create_api_client()
        if headers is None:
            headers = self._get_headers()
        elif headers == 'invalid_token':
            headers = {
                'Authorization': 'invalid_token'
            }

        # Calling and validating the response against the model. Raises an error if wrong. # noqa: E501
        try:
            data = mlx.workspace_folders(_headers=headers)
            response = pam.UserFolderArrayResponse.model_validate(
                pam.UserFolderArrayResponse.from_json(data)
            )
            assert response.status.http_code == 200, response
            self.folder_id = response.data.folders[0].folder_id

            return response

        except pam.ApiException as e:
            response = pam.ApiExceptionError(**json.loads(e.body))
            return response

    def refresh_token(self, payload, headers=None):
        # Instantiate the client.
        mlx = self.create_api_client()
        if headers is None:
            headers = self.headers
        elif headers == 'invalid_token':
            headers = {
                'Authorization': 'invalid_token'
            }

        try:
            data = mlx.user_refresh_token(
                refresh_token=payload, _headers=headers
                )
            response = pam.SigninResponse.model_validate(
                pam.SigninResponse.from_json(data)
            )
            assert response.status.http_code == 200, response

            return response

        except pam.ApiException as e:
            response = pam.ApiExceptionError(**json.loads(e.body))
            return response
