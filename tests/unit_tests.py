#!python3
import os
import unittest
import sys
import requests
import json
sys.path.append('../backtesting')
sys.path.append('../src')


from backtest_data import get_suscripcion, get_rescate
from endpoints_hg import login, suscripcion_fci, rescate_fci

import logging
import http.client as http_client
http_client.HTTPConnection.debuglevel = 1
#initialize logging
logging.basicConfig()
#logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

url_base = f'https://demo.aunesa.dev:10017/Irmo/api/'
def login():
    url = f'{url_base}login'
    headers = {'Content-Type': 'application/json'}
    USR_NAME = "USER_FCI"
    PWD = "USER_FCI"

    data = {
        "clientId": "SYC",
        "username": USR_NAME,
        "password": PWD
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    resp = response.json()
    print(resp)
    token = resp['token']
    print(token)
    return token


class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_test_header(test_name):
    print(f"{bcolors.CYAN}{64 * '='}\nTest Case {test_name}\n{64 * '='}{bcolors.ENDC}\n\n")

def print_call_header():
    print(f"{bcolors.GREEN}-- Request / Response {64 * '-'}{bcolors.ENDC}\n")

def print_call_footer():
    print(f"{bcolors.GREEN}-- Fin Request / Response {64 * '-'}{bcolors.ENDC}\n\n")

def print_test_input(input):
    print(f"{bcolors.BLUE}-- INPUT {64 * '-'}\n{input}\n-- FIN INPUT {64 * '-'}{bcolors.ENDC}\n\n")

def print_test_output(output):
    print(f"{bcolors.YELLOW}-- OUTPUT {64 * '-'}\n{output}\n-- FIN OUTPUT {64 * '-'}{bcolors.ENDC}\n\n")

def print_response(response):
    print(f"{bcolors.YELLOW}-- OUTPUT {64 * '-'}\nSTATUS: {response.status_code}\n{response.text}\n-- FIN OUTPUT {64 * '-'}{bcolors.ENDC}\n\n")


class Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Preparación global, se ejecuta una vez antes de ejecutar cualquier caso de prueba
        print(f"Inicializando recursos globales")
        # suscription backtesting dat
        cls.suscripcion = get_suscripcion()
        cls.id_suscri = None
        cls.rescate = get_rescate()
        cls.id_rescate = None

    @classmethod
    def tearDownClass(cls):
        print(f"Eliminando recursos globales")

    def tearDown(self) -> None:
        input(f"Presione enter para continuar\n\n\n")

    # @unittest.skip
    def test_case_000(self):
        print_test_header("000: Login")
        print_call_header()
        Tests.token = login()
        print_call_footer()
        print_test_output(Tests.token)

    # @unittest.skip
    def test_case_001(self):
        print_test_header("001: Dar de alta suscripción")

        print_test_input(f"{Tests.suscripcion}")

        print_call_header()
        response = suscripcion_fci(Tests.token, url_base, Tests.suscripcion)
        print_call_footer()

        # if response.status_code in [200, 201]:
            # Tests.id_suscri = response.json()['id']
        print_response(response)

    # @unittest.skip
    def test_case_002(self):
        print_test_header("002: Dar de alta rescate por cp")

        print_test_input(f"{Tests.rescate}")

        print_call_header()
        response = rescate_fci(Tests.token, url_base, Tests.rescate)
        print_call_footer()

        # if response.status_code in [200, 201]:
        #     Tests.id_rescate = response.json()['id']
        print_response(response)

if __name__ == '__main__':
    # Change to source dir, to avoid resources conflicts (with templates, images, etc.)
    os.chdir('../src')
    unittest.main()
