import base64
import json
import os
import requests


usrpass = base64.b64encode("fci_ag105:nueva123".encode('ascii')).decode('ascii')

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic ' + usrpass
}