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

def find_subscriptions(auth_headers:dict):
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
    url = f"https://sbx.santander.com.ar/apif-api_mutual_funds/v2/redemption/search"
    return get(auth_headers, url)

def get_redemption(transactionId):
    url = f"https://sbx.santander.com.ar/apif-api_mutual_funds/v2/redemption/{transactionId}"
    return get(url)

def confirm_redemption(transactionId):
    url = f"https://sbx.santander.com.ar/apif-api_mutual_funds/v2/redemptions/{transactionId}?action=confirm"
    return put(url)

def all_funds():
    url = "https://sbx.santander.com.ar/apif-api_mutual_funds/v2/"
    return get(url)

def get_fund_by_id(fundId):
    url = f"https://sbx.santander.com.ar/apif-api_mutual_funds/v2/{fundId}"
    return get(url)

def get_fund_by_id_details(fundId):
    url = f"https://sbx.santander.com.ar/apif-api_mutual_funds/v2/{fundId}/details"
    return get(url)

def get_fund_by_id_rules(fundId):
    url = f"https://sbx.santander.com.ar/apif-api_mutual_funds/v2/{fundId}/rules"
    return get(url)
