from services.PAM.endpoints.PAM import PAM
from services.PAM import pam_api_client as api
from test_data import credentials as creden
from dotenv import load_dotenv
from test_data import data
from utils import helper
import json
import os

workspace_id = helper.get_wid(creden.EMAIL)
refresh_token = os.getenv('REFRESH_TOKEN')