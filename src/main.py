from threading import Thread

import redflagbpm

from bbg.query import queryDataPoint, queryDataHistory, queryChashFlow, queryFactorSchedule
from bbg.updateDET import update_instruments, update_cashflows
from bbg.updateHIS import update_history
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.applications import get_swagger_ui_html

app = FastAPI()
bpm = redflagbpm.BPMService()


@app.get("/", include_in_schema=False)
async def root():
    response = RedirectResponse(url='/docs')
    return response


@app.get("/update_instruments")
async def update_instruments_endpoint(instruments: str, fields: str):
    isin_list = instruments.split(',')
    fields = fields.split(',') if fields is not None else None
    t = Thread(target=update_instruments, args=(bpm, isin_list, fields))
    t.start()
    return {"message": "OK"}


@app.get("/update_history")
async def update_history_endpoint(instruments: str, start_date: str, end_date: str, fields: str = None,
                                  periodicity: str = 'daily'):
    isin_list = instruments.split(',')
    fields = fields.split(',') if fields is not None else None
    periodicity = periodicity if periodicity is not None else 'daily'
    t = Thread(target=update_history, args=(bpm, isin_list, start_date, end_date, fields, periodicity))
    t.start()
    return {"message": "OK"}


@app.get("/query_data_point")
async def query_data_point_endpoint(isin: str, fields: str = None):
    fields = fields.split(',') if fields is not None else None
    dp = queryDataPoint(bpm, isin, fields)
    return dp


@app.get("/query_cash_flow")
async def query_cash_flow_endpoint(isin: str):
    dp = queryChashFlow(bpm, isin)
    return dp


@app.get("/query_factor_shedule")
async def query_factor_schedule_endpoint(isin: str):
    dp = queryFactorSchedule(bpm, isin)
    return dp


@app.get("/query_data_history")
async def query_data_history_endpoint(isin: str, start_date: str, end_date: str, fields: str = None):
    fields = fields.split(',') if fields is not None else None
    dp = queryDataHistory(bpm, isin, start_date, end_date, fields)
    return dp
