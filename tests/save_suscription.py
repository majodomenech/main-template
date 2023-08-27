import sys
sys.path.append('../src')
from endpoints_santander import post_login

#example
# {
#     "fundId": 130,
#     "type": "amount",
#     "value": 1000,
#     "investmentAccount": 5987311,
#     "paymentMethod": {
#         "type": "ACCOUNT",
#         "UBK": "0720112320000001419672"
#     },
#     "externalReference": 484670111111111
# }


import requests
import json

token = post_login()
#simular suscripción (dar el alta)
def save_suscription(token):
  url = "https://sbx.santander.com.ar/apif-api_mutual_funds/v2/subscriptions"

  payload = json.dumps({
    "fundId": 130,
    "type": "amount",
    "value": 1000,
    "investmentAccount": 5987311,
    "paymentMethod": {
      "type": "ACCOUNT",
      "UBK": "0720112320000001419672"
    },
    "externalReference": 484670111111111
  })
  headers = {
    'Authorization': f"Bearer {token}",
    'x-ibm-client-id': 'e3fa0fa8-ec9d-406b-960a-150071b151a7',
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  print(response.text)


# resp = save_suscription(token)


def find_all_suscriptions(token):
  url = "https://sbx.santander.com.ar/apif-api_mutual_funds/v2/subscriptions/search"

  payload = ""
  headers = {
    'Authorization': f"Bearer {token}",
    'x-ibm-client-id': 'e3fa0fa8-ec9d-406b-960a-150071b151a7',
    'Content-Type': 'application/json'
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  print(response.text)

  #string to json
  #parse json
  transactions_list = []
  for i in json.loads(response.text)['result']:
    print(i['transactionId'])
    transactions_list.append(i['transactionId'])
  return transactions_list


transactions_list = find_all_suscriptions(token)
def get_suscription_info(transaction_id):

  url = f"https://sbx.santander.com.ar/apif-api_mutual_funds/v2/subscriptions/{transaction_id}"

  payload = ""
  headers = {
    'Authorization': f"Bearer {token}",
    'x-ibm-client-id': 'e3fa0fa8-ec9d-406b-960a-150071b151a7',
    'Content-Type': 'application/json',
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  # print(response.text)
  return response.text


json_resp = {}
for i in transactions_list:
  json_resp[i] = get_suscription_info(i)

print(json_resp)

def ingresar_suscription(token, transactionId):
  url = f"https://sbx.santander.com.ar/apif-api_mutual_funds/v2/subscriptions/{transactionId}?action=confirm"

  payload = {}
  headers = {
    'Content-Type': 'application/json',
    'x-ibm-client-id': 'e3fa0fa8-ec9d-406b-960a-150071b151a7',
    'Authorization': f"Bearer {token}",
    'x-san-customer-id': '00559374'
  }

  response = requests.request("PUT", url, headers=headers, data=payload)

  print(response.text)



