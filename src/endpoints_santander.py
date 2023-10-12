import base64
import json
import os
import requests

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
    return requests.request("POST", url, headers=headers, data=payload, proxies=proxy)


response = login_apigee()
# recibo un jwt: json web token
token = response.json()['access_token']

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + token
}

def get(url: str):
    try:
        proxy = {'https': os.environ['PROXY_BYMA']}
    except KeyError:
        proxy = {}
    return requests.request("GET", url, headers=headers, proxies=proxy)

def post(url: str, payload: str):
    try:
        proxy = {'https': os.environ['PROXY_BYMA']}
    except KeyError:
        proxy = {}
    return requests.request("POST", url, headers=headers, data=payload, proxies=proxy)

def put(url: str):
    try:
        proxy = {'https': os.environ['PROXY_BYMA']}
    except KeyError:
        proxy = {}
    return requests.request("PUT", url, headers=headers, proxies=proxy)


def save_suscription(subscriptions: dict):
    payload = json.dumps(subscriptions)
    url = "https://sbx.santander.com.ar/apif-api_mutual_funds/v2/subscriptions"
    return post(url, payload)

def confirm_suscription(transactionId):
    url = f"https://sbx.santander.com.ar/apif-api_mutual_funds/v2/subscriptions/{transactionId}?action=confirm"
    return put(url)


def find_subscriptions():
    url = "https://sbx.santander.com.ar/apif-api_mutual_funds/v2/subscriptions/search"
    return get(url)

def get_subscription(transactionId):
    url = f"https://sbx.santander.com.ar/apif-api_mutual_funds/v2/subscriptions/{transactionId}"
    return get(url)

def save_redemption(redemptions: dict):
    payload = json.dumps(redemptions)
    url = "https://sbx.santander.com.ar/apif-api_mutual_funds/v2/redemptions"
    return post(url, payload)

def search_redemption():
    url = f"https://sbx.santander.com.ar/apif-api_mutual_funds/v2/redemption/search"
    return get(url)

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

resp = search_redemption()
print(resp.text)