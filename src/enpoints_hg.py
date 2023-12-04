#!python3
import pycurl
import json
from io import BytesIO
import redflagbpm
import requests

def call_json_endpoint(curl, auth_headers):
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, curl)
    c.setopt(pycurl.HTTPHEADER, auth_headers)
    c.setopt(c.WRITEDATA, buffer)

    c.perform()
    # response = c.getinfo(pycurl.RESPONSE_CODE)
    c.close()

    body = buffer.getvalue()
    resp = json.loads(body.decode('UTF-8'))
    return resp


def login(bpm, url_base):
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
    return response.text

def rescate_fci(bpm, url_base, data):
    url = f'{url_base}fondos/rescateFCI'
    TOKEN = bpm.service.text('TOKEN_WS')
    headers = {
        'Authorization': 'Bearer '+TOKEN,
        'Content-Type': 'application/json'
    }


    # data = {
    #     "contexto": {
    #         "modalidad": "BILATERAL",
    #         "origen": "S&C",
    #         "acdi": "57"
    #     },
    #     "solicitud": {
    #         "fechaSolicitud": "03/01/2023 15:52:50",
    #         "cuentaComitente": "5006687",
    #         "fondo": "14961",
    #         "especieMoneda": "ARS",
    #         "cantidad": 100000,
    #         "rescateDinero": True,
    #         "aceptaReglamento": True
    #     }
    # }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.text

# def main():
#     bpm = redflagbpm.BPMService()
#     url_base = f'https://demo.aunesa.dev:10017/Irmo/api/'
#     response_body = login(bpm, url_base)
#     response = suscripcion_fci(bpm, url_base, data)
#
#
# if __name__ == "__main__":
#     main()
