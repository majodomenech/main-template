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
    TOKEN = bpm.service.text('TOKEN_WS')
    USR_NAME = "wstesoreria"
    data = {
        "clientId": "SYC",
        "username": USR_NAME,
        "password": TOKEN
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.text  # Return the response body as a string


def suscripcion_fci(bpm, url_base):
    url = f'{url_base}fondos/suscripcionFCI'
    TOKEN = bpm.service.text('TOKEN_WS')
    headers = {
        'Authorization': 'Bearer '+TOKEN,  # Replace 'la_clavecita' with your actual token
        'Content-Type': 'application/json'
    }


    data = {
        "contexto": {
            "modalidad": "BILATERAL",
            "origen": "S&C",
            "acdi": "57"
        },
        "solicitud": {
            "fechaSolicitud": "03/01/2023 15:52:50",
            "cuentaComitente": "5006687",
            "fondo": "14961",
            "especieMoneda": "ARS",
            "cantidad": 100000,
            "integraComitente": False,
            "aceptaReglamento": True
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.text

def rescate_fci(bpm, url_base):
    url = f'{url_base}fondos/rescateFCI'
    TOKEN = bpm.service.text('TOKEN_WS')
    headers = {
        'Authorization': 'Bearer '+TOKEN,  # Replace 'la_clavecita' with your actual token
        'Content-Type': 'application/json'
    }


    data = {
        "contexto": {
            "modalidad": "BILATERAL",
            "origen": "S&C",
            "acdi": "57"
        },
        "solicitud": {
            "fechaSolicitud": "03/01/2023 15:52:50",
            "cuentaComitente": "5006687",
            "fondo": "14961",
            "especieMoneda": "ARS",
            "cantidad": 100000,
            "rescateDinero": True,
            "aceptaReglamento": True
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.text

def main():
    bpm = redflagbpm.BPMService()
    url_base = f'https://demo-4.aunesa.dev:10064/Irmo/api/'
    response_body = login(bpm, url_base)
    response_body_s = suscripcion_fci(bpm, url_base)


if __name__ == "__main__":
    main()
