from deting.Report import create_report
from datetime import date

desde = date.fromisoformat("2022-01-01")
hasta = date.fromisoformat("2022-12-31")

create_report(desde, hasta)
