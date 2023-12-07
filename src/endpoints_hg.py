#!python3
import pycurl
import json
from io import BytesIO
import redflagbpm
import requests


def login(url_base):
    url = f'{url_base}login'
    headers = {'Content-Type': 'application/json'}
    USR_NAME = "USER_FCI"
    PWD = "USER_FCI"

    data = {
        "clientId": "SYC",
        "username": USR_NAME,
        "password": PWD
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    resp = response.json()
    print(resp)
    token = resp['token']
    print(token)
    return token


def suscripcion_fci(token, url_base, data):
    url = f'{url_base}fondos/suscripcionFCI'
    TOKEN = token
    headers = {
        'Authorization': 'Bearer '+TOKEN,
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))

    return response

def rescate_fci(token, url_base, data):
    url = f'{url_base}fondos/rescateFCI'
    TOKEN = token
    headers = {
        'Authorization': 'Bearer '+TOKEN,
        'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    return response

# def main():
#     bpm = redflagbpm.BPMService()
#     url_base = f'https://demo.aunesa.dev:10017/Irmo/api/'
#     response_body = login(bpm, url_base)
#     response = suscripcion_fci(bpm, url_base, data)
#
#
# if __name__ == "__main__":
#     main()
