#!python3
import redflagbpm

bpm = redflagbpm.BPMService()
try:
    array_solicitud_pendiente = bpm.context.input['array_solicitud_pendiente']
    if array_solicitud_pendiente is None:
        bpm.reply('No hay solicitudes pendientes')
except:
    bpm.reply('No hay solicitudes pendientes')

if len(array_solicitud_pendiente) == 0:
    bpm.reply('No hay solicitudes pendientes')
