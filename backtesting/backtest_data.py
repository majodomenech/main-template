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
                "cuentaComitente": "141390",
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
                "fechaSolicitud": "07/12/2023 15:52:50",
                "cuentaComitente": "145196",
                "fondo": "14300",
                "rescateDinero": False,
                "cantidadImporte": 1
            }
        }
    return data_res

def get_backtesting_data(bpm):
    bpm.context.array_solicitudes_pendientes = [{"fondo": "[14221] CAFCI747-1638 - Galileo Income - Clase A", "cantidad" : 1, "integraComitente" : "false"}]
    bpm.context.cuenta = "[5003436] LALA"
    bpm.context.initiator = "lbessone"
    bpm.context.processInstanceId = '1'
    bpm.context.fecha = '123250111100000'
