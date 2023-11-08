#!/bin/bash
export plazo_liq='T++'

#subscription backtesting test data
export selection='[{"idOrigen": 215560, "codigo_fci": 130, "fci": "[23808] Super Ahorro $- Clase G", "fund_id": 116, "cuit": "-", "ASUNTO": "Solicitud de suscripcion de [103] Super Ahorro $- Clase G", "ACPIC": "-", "DENOMINACION": "-", "cuenta_id": 2707138, "cuenta": "[5987311] Cuenta que saque de la docu del endpoint", "cuenta_fci": "BSGFCI", "unidad": "ARS", "moneda": "ARS", "cbu": "0720099188000037875486", "DINERO": null, "mkt": null, "T+0": null, "T++": null, "ESTADO": "Liquidacion pendiente", "FECHA": "2023-10-31T12:30:22.080Z", "FECHAFIN": "2023-10-27T12:13:05.539Z", "PROPIETARIO": 58134, "TIPO": "Agenda", "SOLICITUD": "DOC 2023031443", "CLASS": "com.aunesa.irmo.model.acdi.ISolicitudSuscripcionFCI", "CONTEXTO": "Fondos comunes de inversion", "cantidad": 1001, "VALORCUOTAPARTE": "95.447409", "cantidad_cuotapartes": 1001, "CANTIDADSOLICITUD": null, "UNIDAD": 1, "FECHASOLICITUD": 1698289200000, "INTEGRACOMITENTE": false, "template": "uu"}]'

#redemption backtesting test data 1
#export selection='[{"idOrigen": 216260, "codigo_fci": 116, "fci": "[116] SANTANDER INVENTO", "fund_id": 116, "cuit": "30-70496099-5", "ASUNTO": "Solicitud de rescate de [116] SANTANDER INVENTO", "cuenta_id": 41621350, "cuenta": "[2707138] CUENTA CONFIRMED ENDPOINT", "cuenta_fci": "QMSGFCI", "unidad": "ARS", "moneda": "ARS", "cbu": "0720099188000037875486", "DINERO": false, "tipo_rescate": "Cuotapartes", "plazo_liq": 0, "mkt": "BILATERAL", "T+0": "16:30", "T++": "16:30", "ESTADO": "Liquidacion pendiente", "FECHA": 1698721200000, "FECHAFIN": null, "PROPIETARIO": 2934, "TIPO": "Agenda", "SOLICITUD": "DOC 2023031873", "CLASS": "com.aunesa.irmo.model.acdi.ISolicitudRescateFCI", "CONTEXTO": "Fondos comunes de inversion", "cantidad": "171785.679499", "VALORCUOTAPARTE": null, "CANTIDADCUOTAPARTES": null, "cantidad_cuotapartes": 171785.679499, "UNIDAD": null, "FECHASOLICITUD": 1698721200000, "INTEGRACOMITENTE": false, "ACPIC": 8088, "DENOMINACION": "BANCO DE SERVICIOS Y TRANSACCIONES S.A", "template": ""}]'




