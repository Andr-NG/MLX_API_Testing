import requests
import pytest
from dotenv import load_dotenv
from test_data import data
from utils.base_test import BaseTest
from unittest.mock import patch
from datetime import datetime
from utils import helper
from test_data import credentials as creds
from services.PAM import pam_api_client as api


class TestSetUpSignIn(BaseTest):
    def test_setup_signin(self):
        signin_response = self.PAM.sign_in(login=creds.EMAIL, user_pass=creds.PASSWORD)
        wid_response = self.PAM.get_workspace_id()
        wid = wid_response.data.workspaces[0].workspace_id
        fid_response = self.PAM.get_folder_id()
        fid = fid_response.data.folders[0].folder_id
        role = wid_response.data.workspaces[0].role

        assert signin_response.status.http_code == 200, signin_response
        assert wid_response.status.http_code == 200, wid_response
        assert fid_response.status.http_code == 200, fid_response

        helper.add_user(email=creds.EMAIL, workspace_id=wid, folder_id=fid, role=role)


class TestUserSignIn(BaseTest):

    @pytest.mark.parametrize(
        "email, password, error_code, http_code, msg, custom_data",
        data.SIGN_IN,  # noqa: 501E
    )
    def test_user_signin_failed(
        self, email, password, error_code, http_code, msg, custom_data
    ):
        """Testing a negative case for /user/signin."""

        response = self.PAM.sign_in(login=email, user_pass=password)
        assert response.status.error_code == error_code
        assert response.status.http_code == http_code
        assert response.status.message == msg
        assert response.data == custom_data

    def test_user_signin(self):
        """Testing a positive case for /user/signin."""

        response = self.PAM.sign_in(login=creds.EMAIL, user_pass=creds.PASSWORD)
        assert response.status.http_code == 200
        assert response.status.message == "Successful signin"
        assert response.data.token
        assert response.data.refresh_token

    def test_user_signin_limit_error(self):
        """Testing the user sign-in limit error.
        The limit is 10 req/min for non-MLX emails.
        """

        for _ in range(12):
            response = self.PAM.sign_in(
                login=creds.NON_MLX_EMAIL, user_pass=creds.NON_MLX_PASSWORD
            )

        assert response.status.http_code == 429
        assert response.status.error_code == "TOO_MANY_REQUESTS"
        assert (
            response.status.error_code
            == "Too many requests! Wait or upgrade for higher limits."
        )


class TestUserSignUp(BaseTest):

    def test_signup_with_mock(self, load_saved_response):
        """Testing a postive case for /user/signup with mocking as there is no
        functionality to remove accounts. To avoid spamming accounts, the request is mocked.  # noqa: E501
        """

        email = "andreynguyentest@multilogin.com"
        password = "63a893295ab32eade50ed72544ecaec0"

        with patch("requests.post") as mock_post:
            mock_post.return_value.status.http_code = 201
            mock_post.return_value.json.return_value = load_saved_response
            response = requests.post(
                "https://api-dev.mlx.yt/user/signup",
                json={"email": email, "password": password},
            )

            assert response.json() == load_saved_response

    @pytest.mark.parametrize("login, password, http_code, msg", data.SIGN_UP)
    def test_failed_signup(self, login, password, http_code, msg):
        """Testing negative cases for /user/signup."""

        response = self.PAM.sign_up(login=login, user_pass=password)
        assert response["status"]["http_code"] == http_code
        assert response["status"]["message"] == msg


class TestGetWorkspace(BaseTest):
    def test_get_workspace_id(self, check_token):
        """Testing positive cases for retrieving thw workspace ID"""

        response = self.PAM.get_workspace_id()
        # Checking the status block
        assert response.status.http_code == 200
        assert response.status.error_code == ""
        assert response.status.message == ""

        # Checking the data block
        workspace = response.data.workspaces[0]
        assert isinstance(response.data.total_count, int)
        assert isinstance(response.data.workspaces, list)
        assert workspace.name
        assert workspace.workspace_id
        assert workspace.role
        assert len(response.data.workspaces[0].workspace_id) == 36

    @pytest.mark.parametrize("http_code, error_code, msg", data.GET_ID)
    def test_get_workspace_id_failed(self, http_code, error_code, msg):
        """Testing negative cases for retrieving the workspace ID.
        Send headers='invalid_token' to make an unauthorised request"""

        response = self.PAM.get_workspace_id(headers="invalid_token")
        response.status.http_code == http_code
        response.status.error_code == error_code
        response.status.message = msg


class TestGetFolder(BaseTest):
    def test_get_folder_id(self, check_token):
        response = self.PAM.get_folder_id()

        # Checking the status block
        assert response.status.http_code == 200
        assert response.status.error_code == ""
        assert response.status.message == ""

        # Checking the data block
        folder = response.data.folders[0]
        assert isinstance(folder.comment, str)
        assert isinstance(folder.folder_id, str)
        assert isinstance(folder.profiles_count, int)
        assert isinstance(response.data.folders, list)
        assert isinstance(folder.comment, str)
        assert isinstance(folder.name, str)
        assert isinstance(folder.created_at, datetime)
        assert isinstance(folder.profiles_count, int)
        assert len(response.data.folders[0].folder_id) == 36

    @pytest.mark.parametrize("http_code, error_code, msg", data.GET_ID)
    def test_get_folder_id_unauthorised(self, http_code, error_code, msg):
        """Testing negative cases for retrieving the folder ID.
        Send headers='invalid_token' to make an unathorised request."""

        response = self.PAM.get_folder_id(headers="invalid_token")
        response.status.http_code == http_code
        response.status.error_code == error_code
        response.status.message = msg


class TestRefreshToken(BaseTest):
    """Testing refresh token"""

    def test_refresh_token(self, get_owner_wid, get_refresh_token):
        payload = api.RefreshToken(
            email=creds.EMAIL,
            refresh_token=get_refresh_token,
            workspace_id=get_owner_wid,
        )
        response = self.PAM.refresh_token(payload=payload)
        assert response.status.http_code == 200
        assert response.status.error_code == ""
        assert response.status.message == "Token successfully updated"
        assert response.data.refresh_token
        assert response.data.token

    @pytest.mark.parametrize(
        "email, refresh_token, workspace_id, http_code, error_code, msg",
        data.REFRESH_TOKEN,
        ids=[
            "empty email",
            "wrong email",
            "empty refresh_token",
            "wrong refresh_token",
            "empty workspace user",
            "wrong workspace user",
        ],
    )
    def test_refresh_token_failed(
        self, email, refresh_token, workspace_id, http_code, error_code, msg
    ):
        """Testing negative cases"""

        payload = api.RefreshToken(
            email=email,
            refresh_token=refresh_token,
            workspace_id=workspace_id,
        )
        response = self.PAM.refresh_token(payload=payload)
        response.status.http_code = http_code
        response.status.error_code = error_code
        response.status.message = msg

    def test_refresh_token_exta_parameter(self):
        pass
