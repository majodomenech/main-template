#!python3

import json
import time
import datetime
import random

def get_idOrigen():
    # Microseconds since epoch
    timestamp = int(time.time() * 1000000)
    #keep 4 middle digits of a string and back to integer
    short_stamp = int(str(timestamp)[6:-5])
    # Random 5-digit integer
    random_value = random.randint(0, 99999)
    #joining both within a strinf of at list 5 digits
    unique_id = f"{short_stamp:03}{random_value:02}"
    list_unique_id = list(unique_id)
    #randomly shuffle the list
    random.shuffle(list_unique_id)
    #join the list and keep the first 5 digits
    sample = list_unique_id[:5]
    #sample list to string
    sample = int(''.join(sample))
    return sample

def get_redemption_selection():
    data = [{'resumen_orden': json.dumps([{"cantidad": 60000, "cuenta": "5005957", "origenes": [{"cantidad": 60000, "idOrden": get_idOrigen(), "solicitud": "DOC 2023025505", "propietario": 6087}]},
                                        {"cantidad": 40000, "cuenta": "5001429", "origenes": [{"cantidad": 40000, "idOrden": get_idOrigen(), "solicitud": "DOC 2023025512", "propietario": 8970}]}]),
           'plazo_liq': 2, 'cuit': '30-60473101-8', 'cp_total': 100000, 'codigo_fci': '14410', 'template': 'template'}]
    return data

def get_suscription_selection():
    data = [{'cuit': '30-50000173-5', 'cantidad_cuotapartes': 81314.69, 'codigo_fci': '15280', 'idOrigen': get_idOrigen(), 'template': 'template'}]
    return data

def get_suscription():
    data = {
            "fundId": 130,
            "type": "amount",
            "value": 1000,
            "investmentAccount": 5987311,
            "paymentMethod": {
                "type": "ACCOUNT",
                "UBK": "0720112320000001419672"
            },
            "externalReference": 484670111111111
        }
    return data

