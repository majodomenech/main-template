#!/bin/bash
#export PROXY_BYMA=''

#export plazo='T+0'
#export tipo='Rescates'
export tipo='Suscripciones'

#subscription selection_hg actual data
#export selection='[{"idOrigen": 215471, "codigo_fci": 23808, "fci": "[23808] Super Ahorro $- Clase G", "cuit": "-", "ASUNTO": "Solicitud de suscripción de [23808] Super Ahorro $- Clase G", "ACPIC": "-", "DENOMINACION": "-", "cuenta_id": 5006038, "cuenta": "[5006038] BATISTELLI , Laura Nilda  o RIOS, Ignacio Javier", "cuenta_fci": "BSGFCI", "unidad": "ARS", "moneda": "ARS", "cbu": "01508046 01000112693584", "DINERO": null, "mkt": null, "T+0": null, "T++": null, "ESTADO": "Liquidación pendiente", "FECHA": "2023-10-26T12:30:22.080Z", "FECHAFIN": "2023-10-27T12:13:05.539Z", "PROPIETARIO": 58134, "TIPO": "Agenda", "SOLICITUD": "DOC 2023031443", "CLASS": "com.aunesa.irmo.model.acdi.ISolicitudSuscripcionFCI", "CONTEXTO": "Fondos comunes de inversión", "cantidad": 1009734.0, "VALORCUOTAPARTE": "95.447409", "cantidad_cuotapartes": 10578.956, "CANTIDADSOLICITUD": null, "UNIDAD": 1, "FECHASOLICITUD": 1698289200000, "INTEGRACOMITENTE": false, "template": "uu"}]'

#subscription selection HG faked idFci,fakeCbu
#export selection='[{"idOrigen": 215471, "codigo_fci": 130, "fci": "[130] Super Ahorro Clase G", "cuit": "-", "ASUNTO": "Solicitud de suscripción de [23808] Super Ahorro $- Clase G", "ACPIC": "-", "DENOMINACION": "-", "cuenta_id": 5006038, "cuenta": "[5006038] BATISTELLI , Laura Nilda  o RIOS, Ignacio Javier", "cuenta_fci": "BSGFCI", "unidad": "ARS", "moneda": "ARS", "cbu": "0720112320000001419672", "DINERO": null, "mkt": null, "T+0": null, "T++": null, "ESTADO": "Liquidación pendiente", "FECHA": "2023-10-26T12:30:22.080Z", "FECHAFIN": "2023-10-27T12:13:05.539Z", "PROPIETARIO": 58134, "TIPO": "Agenda", "SOLICITUD": "DOC 2023031443", "CLASS": "com.aunesa.irmo.model.acdi.ISolicitudSuscripcionFCI", "CONTEXTO": "Fondos comunes de inversión", "cantidad": 1009734.0, "VALORCUOTAPARTE": "95.447409", "cantidad_cuotapartes": 10578.956, "CANTIDADSOLICITUD": null, "UNIDAD": 1, "FECHASOLICITUD": 1698289200000, "INTEGRACOMITENTE": false, "template": "uu"}]'


#redemption selection_hg actual data
export selection='[{"idOrigen": 215964, "codigo_fci": "14405", "fci": "[14405] Quinquela Desarrollo Argentino Infraest. - Clase A", "cuit": "30-70496099-5", "ASUNTO": "Solicitud de rescate de [14405] CAFCI768-1268 - Quinquela Desarrollo Argentino Infraest. - Clase A", "cuenta_id": 5005934, "cuenta": "[5005934] ROLDAN, Javier Ignacio", "cuenta_fci": "QMSGFCI", "unidad": "ARS", "DINERO": false, "tipo_rescate": "Cuotapartes", "plazo_liq": 2, "mkt": "BILATERAL", "T+0": "16:30", "T++": "16:30", "ESTADO": "Liquidación pendiente", "FECHA": 1698634800000, "FECHAFIN": null, "PROPIETARIO": 4577, "TIPO": "Agenda", "SOLICITUD": "DOC 2023031750", "CLASS": "com.aunesa.irmo.model.acdi.ISolicitudRescateFCI", "CONTEXTO": "Fondos comunes de inversión", "cantidad": "14055.19", "VALORCUOTAPARTE": null, "CANTIDADCUOTAPARTES": null, "cantidad_cuotapartes": 14055.19, "UNIDAD": null, "FECHASOLICITUD": 1698634800000, "INTEGRACOMITENTE": false, "ACPIC": 8088, "DENOMINACION": "BANCO DE SERVICIOS Y TRANSACCIONES S.A", "template": "ja"}]'

#redemption selection HG faked idFci,fakeCbu
#export selection=''