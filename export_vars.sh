#!/bin/bash
#export PROXY_BYMA=''

#export plazo='T+0'
#export tipo='Rescates'
export tipo='Suscripciones'

#selection_hg actual data
#export selection='[{"idOrigen": 215471, "codigo_fci": 23808, "fci": "[23808] Super Ahorro $- Clase G", "cuit": "-", "ASUNTO": "Solicitud de suscripción de [23808] Super Ahorro $- Clase G", "ACPIC": "-", "DENOMINACION": "-", "cuenta_id": 5006038, "cuenta": "[5006038] BATISTELLI , Laura Nilda  o RIOS, Ignacio Javier", "cuenta_fci": "BSGFCI", "unidad": "ARS", "moneda": "ARS", "cbu": "01508046 01000112693584", "DINERO": null, "mkt": null, "T+0": null, "T++": null, "ESTADO": "Liquidación pendiente", "FECHA": "2023-10-26T12:30:22.080Z", "FECHAFIN": "2023-10-27T12:13:05.539Z", "PROPIETARIO": 58134, "TIPO": "Agenda", "SOLICITUD": "DOC 2023031443", "CLASS": "com.aunesa.irmo.model.acdi.ISolicitudSuscripcionFCI", "CONTEXTO": "Fondos comunes de inversión", "cantidad": 1009734.0, "VALORCUOTAPARTE": "95.447409", "cantidad_cuotapartes": 10578.956, "CANTIDADSOLICITUD": null, "UNIDAD": 1, "FECHASOLICITUD": 1698289200000, "INTEGRACOMITENTE": false, "template": "uu"}]'

#selection HG faked idFci,fakeCbu
export selection='[{"idOrigen": 215471, "codigo_fci": 130, "fci": "[130] Super Ahorro Clase G", "cuit": "-", "ASUNTO": "Solicitud de suscripción de [23808] Super Ahorro $- Clase G", "ACPIC": "-", "DENOMINACION": "-", "cuenta_id": 5006038, "cuenta": "[5006038] BATISTELLI , Laura Nilda  o RIOS, Ignacio Javier", "cuenta_fci": "BSGFCI", "unidad": "ARS", "moneda": "ARS", "cbu": "0720112320000001419672", "DINERO": null, "mkt": null, "T+0": null, "T++": null, "ESTADO": "Liquidación pendiente", "FECHA": "2023-10-26T12:30:22.080Z", "FECHAFIN": "2023-10-27T12:13:05.539Z", "PROPIETARIO": 58134, "TIPO": "Agenda", "SOLICITUD": "DOC 2023031443", "CLASS": "com.aunesa.irmo.model.acdi.ISolicitudSuscripcionFCI", "CONTEXTO": "Fondos comunes de inversión", "cantidad": 1009734.0, "VALORCUOTAPARTE": "95.447409", "cantidad_cuotapartes": 10578.956, "CANTIDADSOLICITUD": null, "UNIDAD": 1, "FECHASOLICITUD": 1698289200000, "INTEGRACOMITENTE": false, "template": "uu"}]'