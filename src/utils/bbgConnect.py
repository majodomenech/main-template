import json
import logging
from urllib.parse import urljoin

import requests

################################################################################
# - Import module needed to authorize into BEAP service
#
from bwslib.bws_auth import Credentials, BWSAdapter, download, handle_response

################################################################################
# - Import SSEClient component which handles notification protocol
from bwslib.sseclient import SSEClient

################################################################################
# - Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)-8s] [%(name)s:%(lineno)s]: %(message)s',
)
LOG = logging.getLogger(__name__)

def connect(credentials_file_path:str=None,credentials:str=None):
    ################################################################################
    # - Load credentials from credential file you have obtained from
    # *https://console.bloomberg.com*
    if credentials_file_path is None and credentials is None:
        raise Exception("You must provide credentials_file_path or credentials")
    if credentials_file_path is not None and credentials is not None:
        raise Exception("You must provide credentials_file_path or credentials")
    if credentials_file_path is not None:
        CREDENTIALS = Credentials.from_file(credentials_file_path)
    elif credentials is not None:
        CREDENTIALS = Credentials.from_dict(json.loads(credentials))
    else:
        raise Exception("You must provide credentials_file_path or credentials")
    ################################################################################
    # - Initialize HTTP session with BEAP auth adapter to set version header and
    # provide a signed JWT for each request.
    ADAPTER = BWSAdapter(CREDENTIALS)
    SESSION = requests.Session()
    SESSION.mount('https://', ADAPTER)

    ################################################################################
    # - Create an SSE session to receive notification when reply is delivered
    HOST = 'https://api.bloomberg.com'
    try:
        SSE_CLIENT = SSEClient(urljoin(HOST, '/eap/notifications/sse'), SESSION)
        # Catch an exception to get full error description with the help of the next
        # GET request
    except requests.exceptions.HTTPError as err:
        LOG.error(err)
    try:
        SSE_CLIENT = SSEClient(urljoin(HOST, '/eap/notifications/sse'), SESSION)
        # Catch an exception to get full error description with the help of the next
        # GET request
    except requests.exceptions.HTTPError as err:
        LOG.error(err)
        raise err

    return SESSION, SSE_CLIENT
