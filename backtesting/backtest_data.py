#!python3

def get_suscripcion():
    data_sus = {
          "contexto": {
                "modalidad": "BILATERAL",
                "origen": "S&C",
                "acdi": "000"
          },
          "solicitud": {
                "fechaSolicitud": "03/01/2023 15:52:50",
                "cuentaComitente": "02597",
                "fondo": "14325",
                "especieMoneda": "ARS",
                "cantidad": 100000,
                "integraComitente": False,
                "aceptaReglamento": True
          }
    }
    return data_sus

def get_rescate():
    data_res = {
            "contexto": {
                "modalidad": "BILATERAL",
                "origen": "S&C",
                "acdi": "000"
            },
            "solicitud": {
                "fechaSolicitud": "03/01/2023 15:52:50",
                "cuentaComitente": "5002837",
                "fondo": "14006",
                "rescateDinero": True,
                "cantidadImporte": 1000
            }
        }
    return data_res
