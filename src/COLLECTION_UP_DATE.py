#!python3
from datetime import datetime
import time
import redflagbpm
bpm = redflagbpm.BPMService()

current_datetime = datetime.now()
# Convert the datetime object to a timestamp in seconds
timestamp_seconds = time.mktime(current_datetime.timetuple())
# Convert the timestamp to milliseconds
timestamp_milliseconds = timestamp_seconds * 1000
bpm.context.input['fecha_cotizacion'] = timestamp_milliseconds
