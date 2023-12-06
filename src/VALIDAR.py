#!python3
import redflagbpm

bpm = redflagbpm.BPMService()
try:
    x = bpm.context['array_solicitud_pendiente']
except:
    bpm.reply('No hay solicitudes pendientes')
