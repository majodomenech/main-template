#!python3
import redflagbpm

bpm = redflagbpm.BPMService()
error = '[[[No hay solicitudes pendientes]]]'
try:
    array_solicitud_pendiente = bpm.context.input['array_solicitud_pendiente']
    if array_solicitud_pendiente is None:
        bpm.fail(error)
except:
    bpm.fail(error)

if len(array_solicitud_pendiente) == 0:
    bpm.fail(error)


tipoResultado = bpm.context.input['tipoResultado']
if tipoResultado == "finalizar":
    message = "Tarea cancelada"
elif tipoResultado == "guardar":
    message = "Solicitud procesada"

bpm.context.input['message'] = message
#validación para rescates
# bpm.context['array_solicitud_pendiente']['cantidad_importe']
