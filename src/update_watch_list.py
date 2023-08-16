#!/usr/bin/env python3

import redflagbpm

bpm = redflagbpm.BPMService()

import requests

url = "http://localhost:10001/update_watch_list"

response = requests.get(url)

if response.status_code == 200:
    bpm.reply("OK!")
else:
    bpm.reply("Error al hacer la solicitud. Código de estado:"+ str(response.status_code))
