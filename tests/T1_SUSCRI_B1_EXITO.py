#!python3
# -*- coding: utf-8 -*-

#!python3

import unittest
import os
import sys
import redflagbpm

sys.path.append('../src', '../backtesting')
from data import get_suscription_selection
from endpoints_santander import save_suscription

class Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Preparación global, se ejecuta una vez antes de ejecutar cualquier caso de prueba
        print(f"Inicializando recursos globales")
        #backtesting suscription data
        cls.suscripcion = get_suscription_selection()
        cls.bpm = redflagbpm.BPMService()
    @classmethod
    def tearDownClass(cls):
        print(f"Eliminando recursos globales")
        pass

    # Uncomment to skip
    # @unittest.skip
    def test_case_001(self):
        print(f"{64 * '='}\nTest Case 001: Dar de alta e ingresar suscripción\n{64 * '='}\n{self.subscripcions}\n\n\nLog de request y response:\n{32 * '-'}")
        resp = save_suscription(subscriptions)
        Tests.id_list = id_list
        print(f"{64 * '='}\n\n\n")
        pass

    @unittest.skip
    def tearDown(self) -> None:
        input(f"Presione enter para continuar\n\n\n")


if __name__ == '__main__':
    # Change to source dir, to avoid resources conflicts (with templates, images, etc.)
    os.chdir('../src')
    # Run tests
    unittest.main()
