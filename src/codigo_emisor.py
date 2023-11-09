#!/usr/bin/env python3
# coding: utf-8

#CUIT:Código EMISOR BYMA FONDOS
cod_emisores = {'30-57612427-5':470, 	#Banco de Valores S.A.
                '30-60473101-8':383, 	#BANCO COMAFI SOCIEDAD ANONIMA
                '30-70496099-5':2803,	#BANCO DE SERVICIOS Y TRANSACCIONES S.A.
                '30-50000173-5':11,	    #BANCO DE GALICIA
                '30-68502995-9':5305,	#BANCO INDUSTRIAL S.A.
                '30-65768392-9':4293,	#Custodia Sociedad Depositaria de F.C.I. S.A.
                '30-50001008-4':409,	#Banco Macro
                '30-58018941-1':656,	#Banco Itau Arg. SA SD FCI
                '33-50000517-9':112,	#BANCO SUPERVIELLE S.A.,
                '30-70722741-5':2619,	#BACS BANCO DE CREDITO Y SECURITIZACION S.A.
                '30-50001091-2':404}	#BANCO DE LA NACION ARGENTINA

def get_codigo_emisor_byma_cuit(cuit):
    return cod_emisores[cuit]