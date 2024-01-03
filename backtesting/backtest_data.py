#!python3

def get_uni_suscripcion():
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

def get_uni_rescate():
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

def get_backtesting_subscription_data(bpm):
    bpm.context.array_solicitud_pendiente = [{"fondo": "[14325] CAFCI461-887 - Cohen Abierto Pymes - Clase A.", "moneda": "ARS","monto" : 1, "integra_comitente" : False},
                                             {"fondo": "[14298] CAFCI1018 - FCI MAF PESOS PLUS CL.A", "moneda": "ARS","monto" : 2, "integra_comitente" : False},
                                             {"fondo": "[14305] CAFCI550-1113 - FCI MAF ACCIONES ARGENTINAS B.", "moneda": "ARS","monto" : 3, "integra_comitente" : False}
                                             ]
    bpm.context.cuenta = "141390"
    bpm.context.initiator = "lbessone"
    bpm.context.processInstanceId = '1'
    bpm.context['fecha.getTime()'] = 1702263600000

def get_backtesting_redemption_data(bpm):
    bpm.context.array_solicitud_pendiente = [{"fondo": "[14325] CAFCI461-887 - Cohen Abierto Pymes - Clase A.",
                                              "cantidad_importe": 1, "rescate_dinero": False, "monto": None}
                                             ]
    bpm.context.cuenta = "145196"
    bpm.context.initiator = "lbessone"
    bpm.context.processInstanceId = '1'
    bpm.context['fecha.getTime()'] = 1702263600000

