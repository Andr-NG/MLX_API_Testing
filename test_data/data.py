from json import load
import os
from utils import helper
from test_data import credentials as creds
from dotenv import load_dotenv
# load_dotenv(override=True)

SIGN_UP = [
    (
        "andreynguyentest@multilogin.com",
        "63a893295ab32eade50ed72544ecaec0",
        409,
        "User email already registered",
    ),
    # Existing email
    (
        "andreynguyentest1@multilogin.com",
        "63a893295ab32eade50ed72544eca",
        400,
        "Password not valid",
    ),
    # Invalid md5 hash
    (
        "andreynguyentest@multilogi",
        "63a893295ab32eade50ed72544ecaec0",
        400,
        "invalid email format",
    ),
    # Invalid email
]

SIGN_IN = [
    (
        "",
        "password123",
        "BAD_REQUEST_BODY",
        400,
        "invalid email format",
        None
    ),
    # Empty email
    (
        "user@example.com",
        "63a893295ab32eade50ed72544ecaec0",
        "BAD_REQUEST_VALUES",
        400,
        "Incorrect credentials",
        None
    ),
    # Non-existent email
    (
        "andrey.nguyenowner26@multilogin.com",
        "63a893295ab32eade50ed72544ecaec2",
        "BAD_REQUEST_VALUES",
        400,
        "Incorrect credentials",
        None
    ),
    # Wrong password
    (
        "",
        "",
        "BAD_REQUEST_BODY",
        400,
        "invalid email format",
        None
    ),
    # Empty strings
    (
        "andrey.nguyenowner26@multilogin.com",
        "",
        "BAD_REQUEST_VALUES",
        400,
        "Incorrect credentials",
        None
    ),
    # Empty pass
]

GET_ID = [
    (
        '401',
        'UNAUTHORIZED_REQUEST',
        'Wrong JWT token'
    )
]

REFRESH_TOKEN = [
    (
        '',
        os.getenv('REFRESH_TOKEN'),
        helper.get_wid(creds.EMAIL),
        'BAD_REQUEST_BODY',
        400,
        'invalid email format',
    ),  # empty email
    (
        'dasdsa@test.com',
        os.getenv('REFRESH_TOKEN'),
        helper.get_wid(creds.EMAIL),
        'BAD_REQUEST_VALUES',
        400,
        'Incorrect credentials',
    ),  # wrong email
    (
        creds.EMAIL,
        '',
        helper.get_wid(creds.EMAIL),
        'BAD_REQUEST_BODY',
        400,
        'invalid refresh token',
    ),  # empty refersh_token
    (
        creds.EMAIL,
        '122313',
        helper.get_wid(creds.EMAIL),
        'BAD_REQUEST_BODY',
        400,
        'invalid refresh token',
    ),  # wrong refresh_token
    (
        creds.EMAIL,
        os.getenv('REFRESH_TOKEN'),
        '',
        'BAD_REQUEST_VALUES',
        400,
        'Wrong workspace user',
    ),  # empty workspace user
    (
        creds.EMAIL,
        os.getenv('REFRESH_TOKEN'),
        'ab2e57b2-d9bd-4de5-a3fa-ea89e82d113e',
        'BAD_REQUEST_VALUES',
        400,
        'Wrong workspace user',
    )  # wrong workspace user
]
