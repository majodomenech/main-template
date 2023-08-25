import base64
import json
import os
import requests

sandbimport requests

usrpass = base64.b64encode("At8tRQKSwSylWDnDjHMFAvCbpSreukE0:jZRT5p5KR2yEknBbacFzBkxGxDxNBl29".encode('ascii')).decode('ascii')
print(usrpass)
payload = {'grant_type':usrpass}

payload = {}
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic ' + usrpass
}


url = "https://sbx.santander.com.ar/oauthv2/token"
response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)