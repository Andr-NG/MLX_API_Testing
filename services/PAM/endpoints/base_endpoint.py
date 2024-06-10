import os
import pam_api_client as pam
from dotenv import load_dotenv


class BaseEndpoint:

    """Basendpoint to be inhereted by other endpoints.
    """

    def _get_headers(self):
        load_dotenv(override=True)
        header = {}
        token = os.getenv('TOKEN')
        if token is None:
            print('No JWT token has been found')
            return None
        else:
            header.setdefault("Authorization",  f"Bearer {token}")
        return header

    @staticmethod
    def create_api_client(env="DEV"):

        # Define configurations
        host = "https://api-dev.mlx.yt"
        config = pam.Configuration(host=host)
        if env.upper() == "QA":
            host_qa = "https://api-qa.mlx.yt"
            config.host = host_qa
        elif env.upper() == "PROD":
            host_prod = "https://api.multilogin.com"
            config.host = host_prod

        with pam.ApiClient(configuration=config) as client:
            api = pam.DefaultApi(client)
            return api