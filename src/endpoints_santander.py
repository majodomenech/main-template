import base64
import json
import os
import requests
import sys
sys.path.append('../backtesting')
# from data import get_suscription


def login_apigee():
    #payload is url encoded string
    payload = 'grant_type=client_credentials'
    url = "https://sbx.santander.com.ar/oauthv2/token"
    usrpass = base64.b64encode(
        "At8tRQKSwSylWDnDjHMFAvCbpSreukE0:jZRT5p5KR2yEknBbacFzBkxGxDxNBl29".encode('ascii')).decode(
        'ascii')

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'Authorization': 'Basic ' + usrpass
    }
    try:
        proxy = {'https': os.environ['PROXY_BYMA']}
    except KeyError:
        proxy = {}
    response=requests.request("POST", url, headers=headers, data=payload, proxies=proxy)
    # recibo un jwt: json web token
    token = response.json()['access_token']
    auth_headers = {
        'Content-Type': 'application/json',
        'x-ibm-client-id': 'e3fa0fa8-ec9d-406b-960a-150071b151a7',
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + token
    }
    return auth_headers


def get(auth_headers:dict, url: str):
    try:
        proxy = {'https': os.environ['PROXY_BYMA']}
    except KeyError:
        proxy = {}
    return requests.request("GET", url, headers=auth_headers, proxies=proxy)

def post(auth_headers, url: str, payload: str):
    try:
        proxy = {'https': os.environ['PROXY_BYMA']}
    except KeyError:
        proxy = {}
    return requests.request("POST", url, headers=auth_headers, data=payload, proxies=proxy)

def put(auth_headers:dict, url: str):
    try:
        proxy = {'https': os.environ['PROXY_BYMA']}
    except KeyError:
        proxy = {}
    return requests.request("PUT", url, headers=auth_headers, proxies=proxy)


def save_suscription(auth_headers: dict, subscriptions: dict):
    payload = json.dumps(subscriptions)
    url = "https://sbx.santander.com.ar/apif-api_mutual_funds/v2/subscriptions"
    return post(auth_headers,url, payload)

def confirm_suscription(auth_headers:dict, transactionId):
    url = f"https://sbx.santander.com.ar/apif-api_mutual_funds/v2/subscriptions/{transactionId}?action=confirm"
    return put(auth_headers,url)

def search_subscription(auth_headers:dict):
    url = "https://sbx.santander.com.ar/apif-api_mutual_funds/v2/subscriptions/search"
    return get(auth_headers, url)

def get_subscription(auth_headers:dict, transactionId):
    url = f"https://sbx.santander.com.ar/apif-api_mutual_funds/v2/subscriptions/{transactionId}"
    return get(auth_headers, url)

def save_redemption(auth_headers:dict, redemptions: dict):
    payload = json.dumps(redemptions)
    url = "https://sbx.santander.com.ar/apif-api_mutual_funds/v2/redemptions"
    return post(auth_headers, url, payload)

def search_redemption(auth_headers:dict):
    # payload = json.dumps({})
    url = f"https://sbx.santander.com.ar/apif-api_mutual_funds/v2/redemptions/search"
    return get(auth_headers, url)

def get_redemption(auth_headers:dict, transactionId):
    url = f"https://sbx.santander.com.ar/apif-api_mutual_funds/v2/redemptions/{transactionId}"
    return get(auth_headers, url)

def confirm_redemption(auth_headers:dict, transactionId):
    url = f"https://sbx.santander.com.ar/apif-api_mutual_funds/v2/redemptions/{transactionId}?action=confirm"
    return put(auth_headers, url)

def all_funds(auth_headers:dict):
    url = "https://sbx.santander.com.ar/apif-api_mutual_funds/v2/"
    return get(auth_headers, url)

def get_fund_by_id(auth_headers:dict, fundId):
    url = f"https://sbx.santander.com.ar/apif-api_mutual_funds/v2/{fundId}"
    return get(auth_headers, url)

def get_fund_by_id_details(auth_headers:dict, fundId):
    url = f"https://sbx.santander.com.ar/apif-api_mutual_funds/v2/{fundId}/details"
    return get(auth_headers, url)

def get_fund_by_id_rules(auth_headers:dict, fundId):
    url = f"https://sbx.santander.com.ar/apif-api_mutual_funds/v2/{fundId}/rules"
    return get(auth_headers, url)

data = {'fundId': 130, 'type': 'share', 'value': 1301.4482, 'paymentMethod': {'type': 'account', 'UBK': '0720099188000037875486'}, 'investmentAccount': 2707138, 'netShare': None, 'shareValue': None, 'netAmount': None, 'dateConcert': None, 'dateLiquid': None, 'transactionId': 59764, 'status': 'FAILED', 'certificateId': None, 'processDate': '2023-10-11', 'externalReference': '2000024'}


# headers = login_apigee()
# # resp = search_subscription(headers)
# resp  =search_redemption(headers)
# print(resp.text)
