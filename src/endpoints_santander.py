import base64
import json
import os
import requests

sandbimport requests

url = "https://sbx.santander.com.ar/oauthv2/token"

payload = {}
headers = {
  'Authorization': 'Basic OXY3WjFib1BRNUNrR3pzQWhPWE10cGNXTDBFQlJYbW86QXQ4dFJRS1N3U3lsV0RuRGpITUZBdkNicFNyZXVrRTA='
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

}