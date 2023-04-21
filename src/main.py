#!python3

from deting.Report import create_report
from datetime import date, datetime

import redflagbpm

bpm = redflagbpm.BPMService()

try:
    desde = datetime.fromtimestamp(bpm.context.desde/1000.0)
    hasta = datetime.fromtimestamp(bpm.context.hasta/1000.0)
except:
    desde = date.fromisoformat("2023-01-01")
    hasta = date.fromisoformat("2023-02-28")

create_report(desde, hasta)

##Preparo la salida del endpoint
_responseHeaders = bpm.context.json._responseHeaders
_responseHeaders["status"] = "200"  # Indico status 200 (OK)
_responseHeaders[
    "Content-Type"] = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"  # Indico el tipo de archivo
_responseHeaders["Content-Encoding"] = "UTF-8"  # Indico el encoding
_responseHeaders["Content-Disposition"] = "attachment; filename=deting.xlsx"  # Indico el encoding
# Indico que la respuesta será un recurso que guardé. Si omito esto la salida es
# lo que imprima por consola
_responseHeaders["resource"] = "/tmp/deting.xlsx"
