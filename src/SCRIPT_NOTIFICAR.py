#!python3
import redflagbpm

bpm = redflagbpm.BPMService()
rs=bpm.resourceService


operador = bpm.context['userId']
autorizados = ['cnievas', 'pmartinez', 'jluna']

if (operador in autorizados):
    mensaje = "Ya está disponible el menú de la semana"
    bpm.service.notifyGroup(group='MENU', title="Menú cargado", description = mensaje, sound=True)
    bpm.reply(
        {"statusMessage": "Notificación enviada",
         "type": "TERMINAL_UPDATE"
         })
else:
    bpm.reply("Su usuario no tiene autorización para realizar esta acción")
