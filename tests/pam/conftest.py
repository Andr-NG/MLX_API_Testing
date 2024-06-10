import pytest
import json
import os
import jwt
from utils import helper
from dotenv import load_dotenv
from test_data import credentials as creds
from datetime import datetime, timedelta
from services.PAM.endpoints.PAM import PAM
from services.PAM import pam_api_client as api

load_dotenv(override=True)


@pytest.fixture()
def load_saved_response():
    with open(r"utils\signup_response_201.json", "r") as content:
        data = json.load(content)
        return data


@pytest.fixture()
def check_token(get_owner_wid, get_refresh_token):

    token = os.getenv("TOKEN")
    user = PAM()

    # Checking if the token is good and accessing its iat value.
    if token:
        decoded = jwt.decode(
            token, algorithms=["HS512"], options={"verify_signature": False}
        )
        iat_stamp = decoded.get("iat")
        issued_at = datetime.fromtimestamp(iat_stamp)

        # Checking the token lifetime.
        if issued_at + timedelta(minutes=25) < datetime.now():
            print("Token expired\n")
            payload = api.RefreshToken(
                email=creds.EMAIL,
                workspace_id=get_owner_wid,
                refresh_token=get_refresh_token,
            )
            user.refresh_token(payload=payload)
            print("Token updated and saved")
        else:
            print("Token is still valid")

    # If not, call to get a new token and save it.
    else:
        user.sign_in(login=creds.EMAIL, user_pass=creds.PASSWORD)
        print("Token retrieved and saved")
    yield


@pytest.fixture()
def fetch_wid(check_token):
    pam = PAM()
    response = pam.get_workspace_id()
    wid = response.data.workspaces[0].workspace_id
    yield wid


@pytest.fixture()
def get_refresh_token():
    ref_token = os.getenv("REFRESH_TOKEN")
    yield ref_token


@pytest.fixture()
def get_owner_wid():
    wid = helper.get_wid(email=creds.EMAIL)
    yield wid


@pytest.fixture()
def get_owner_fid():
    fid = helper.get_fid(email=creds.EMAIL)
    yield fid
