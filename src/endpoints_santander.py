import base64
import json
import os
import requests

#Docu BYMA cURL

# curl --location --request POST 'https://sbx.santander.com.ar/oauthv2/token' \
# --header 'Accept: application/json' \
# --header 'Content-Type: application/x-www-form-urlencoded' \
# --header 'Authorization: Basic QXQ4dFJRS1N3U3lsV0RuRGpITUZBdkNicFNyZXVrRTA6alpSVDVwNUtSMnlFa25CYmFjRnpCa3hHeER4TkJsMjk=' \
# --data-urlencode 'grant_type=client_credentials'
def post_login():
    #python cURL --> pycurl
    usrpass = base64.b64encode("At8tRQKSwSylWDnDjHMFAvCbpSreukE0:jZRT5p5KR2yEknBbacFzBkxGxDxNBl29".encode('ascii')).decode('ascii')
    print(usrpass)

    #payload is url encoded string
    payload = 'grant_type=client_credentials'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'Authorization': 'Basic ' + usrpass
    }


    url = "https://sbx.santander.com.ar/oauthv2/token"
    response = requests.request("POST", url, headers=headers, data=payload)

    #recibo un jwt: json web token
    token = response.json()['access_token']
    return token


