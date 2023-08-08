import asyncio
import time
from threading import Thread

import redflagbpm

from bbg.query import queryDataPoint, queryDataHistory, queryChashFlow, queryFactorSchedule, queryField
from bbg.updateDET import update_instruments_and_cashflows, update_cashflows, update_date
from bbg.updateFields import update_fields, update_field, update_missing
from bbg.updateHIS import update_history
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.applications import get_swagger_ui_html

import uvicorn

tags_metadata = [
    {
        "name": "update",
        "description": "Operaciones de actualización de tablas (recupera de bloomberg y guarda en base de datos)",
    },
    {
        "name": "query",
        "description": "Operaciones de consulta de tablas (recupera de base de datos)"
    },
]

app = FastAPI(title="Bloomberg API",
              description="API para acceder a información de Bloomberg",
              version="0.1.0",
              openapi_tags=tags_metadata)
bpm = redflagbpm.BPMService()

@app.get("/", include_in_schema=False)
async def root():
    response = RedirectResponse(url='/docs')
    return response


@app.get("/update_instruments", tags=["update"])
async def update_instruments_endpoint(instruments: str, fields: str = None):
    """Actualiza información de los instrumentos y sus cashflows (en caso de ser deudas y contar con el campo ISSUE_DT)
       La infomración se guarda en la tabla bbg.det.
    """
    isin_list = instruments.split(',')
    fields = fields.split(',') if fields is not None else None
    t = Thread(target=update_instruments_and_cashflows, args=(bpm, isin_list, fields))
    t.start()
    return {"message": "OK"}


@app.get("/update_cashflows", tags=["update"])
async def update_cashflows_endpoint():
    """Actualiza información todos los cashflows incompletos (en caso de ser deudas y contar con el campo ISSUE_DT)"""
    t = Thread(target=update_cashflows, args=(bpm,))
    t.start()
    return {"message": "OK"}


@app.get("/update_history", tags=["update"])
async def update_history_endpoint(instruments: str, start_date: str, end_date: str, fields: str = None,
                                  periodicity: str = 'daily'):
    """Actualiza información histórica de los instrumentos. Admite indicar periodicidad (daily, weekly, monthly, quarterly, yearly).
    Por defecto es daily. Se utiliza el servicio de Historical Data.
    La lista predeterminada de campos es:
        'PX_LAST',
        'PX_BID',
        'PX_ASK',
        'PX_DISC_MID',
        'PX_DIRTY_MID',
        'YLD_YTM_BID',
        'YLD_YTM_ASK'.
    """
    isin_list = instruments.split(',')
    fields = fields.split(',') if fields is not None else None
    periodicity = periodicity if periodicity is not None else 'daily'
    t = Thread(target=update_history, args=(bpm, isin_list, start_date, end_date, fields, periodicity))
    t.start()
    return {"message": "OK"}


@app.get("/update_date", tags=["update"])
async def update_date_endpoint(instruments: str, target_date: str, fields: str = None):
    """ Actualiza información de los instrumentos en una fecha específica. Admite indicar los campos a actualizar.
        La información se guarda en la tabla bbg.his a pesar de que el endpoint utilizado se corresponde con
        Current Data (usando SETTLE_DT=target_date) para preservar las fechas.
    """
    isin_list = instruments.split(',')
    fields = fields.split(',') if fields is not None else None
    t = Thread(target=update_date, args=(bpm, isin_list, fields, target_date))
    t.start()
    return {"message": "OK"}


@app.get("/update_fields", tags=["update"])
async def update_fields_endpoint(mnemonics: str):
    """ Actualiza la información de campos (tabla bbg.field) de los instrumentos que no cuentan con la misma.
        Admite indicar los mnemonicos de los campos a actualizar.
    """
    mnemonics = mnemonics.split(',')
    t = Thread(target=update_missing, args=(bpm, mnemonics))
    t.start()
    return {"message": "OK"}


@app.get("/update_all_fields", tags=["update"])
async def update_all_fields_endpoint(queryParameters: str = None):
    """
    Actualiza los campos de todos los instrumentos basados en los parámetros de la query.
    Los parámetros se definenen como un query string, por ejemplo:
        q=PX_LAST&DL:Bulk=true
    """
    t = Thread(target=update_fields, args=(bpm, queryParameters))
    t.start()
    return {"message": "OK"}


@app.get("/update_field", tags=["update"])
async def update_field_endpoint(identifier: str):
    """ Actualiza la información de un campo específico (basado en el identificador de bloomberg, 
        no en mnemómico, ej:pxLast)
    """
    t = Thread(target=update_field, args=(bpm, identifier))
    t.start()
    return {"message": "OK"}


@app.get("/query_data_point", tags=["query"])
async def query_data_point_endpoint(isin: str, fields: str = None):
    """ Consulta información de un instrumento en particular. Admite indicar los campos a consultar.
        La consulta se realiza sobre la tabla bbg.det.
    """
    fields = fields.split(',') if fields is not None else None
    dp = queryDataPoint(bpm, isin, fields)
    return dp


@app.get("/query_cash_flow", tags=["query"])
async def query_cash_flow_endpoint(isin: str):
    """ Consulta el cashflow de un instrumento en particular.
        La consulta se realiza sobre la tabla bbg.det.
    """
    dp = queryChashFlow(bpm, isin)
    return dp


@app.get("/query_factor_shedule", tags=["query"])
async def query_factor_schedule_endpoint(isin: str):
    """ Consulta el factor schedule de un instrumento en particular.
        La consulta se realiza sobre la tabla bbg.det.
    """
    dp = queryFactorSchedule(bpm, isin)
    return dp


@app.get("/query_data_history", tags=["query"])
async def query_data_history_endpoint(isin: str, start_date: str, end_date: str, fields: str = None):
    """ Consulta información histórica de un instrumento en particular. Admite indicar los campos a consultar
        y el rango de fechas. Si no se indican los campos, se consultan todos los campos.
    """
    fields = fields.split(',') if fields is not None else None
    dp = queryDataHistory(bpm, isin, start_date, end_date, fields)
    return dp


@app.get("/query_field", tags=["query"])
async def query_field_endpoint(field: str):
    """ Consulta información de un campo en particular. Admite indicar el mnemónico del campo a consultar.
    """
    dp = queryField(bpm, field)
    return dp


bpm.register_app(app, prefix="bbg:")
