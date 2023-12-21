#!python3
import redflagbpm
import re

bpm = redflagbpm.BPMService()
error = '[[[No hay solicitudes pendientes]]]'
try:
    array_solicitud_pendiente = bpm.context.input['array_solicitud_pendiente']

    # BusinessKey = bpm.execution.getBusinessKey()
    # tipo_solicitud = re.match(r'([a-zA-Z]+)', BusinessKey).group(1)
    # # validación para rescates: si usan o no calcular tiene que validar la cadena de clicks adecuada
    # validar_solicitar_string = ""
    # if tipo_solicitud == 'INSTFCIRE':
    #     for solicitud in array_solicitud_pendiente:
    #         fondo_deno = solicitud['fondo']
    #         cantidad_importe = solicitud['cantidad_importe']
    #         monto = solicitud['monto']
    #         validar_solicitar_string += f"{fondo_deno}_{cantidad_importe}_{monto}"
    #     try:
    #         calcular_solicitar_string = bpm.context['calcular_solicitar_string']
    #         if validar_solicitar_string != calcular_solicitar_string:
    #             bpm.fail(f"Revisa la carga {bpm.context['initiator']}")
    #             raise Exception(u'[[[Revisa la carga mi ciela 👁👄👁 💅!]]]')
    #     except:
    #         pass
    #
    if array_solicitud_pendiente is None:
        bpm.fail(error)
except:
    bpm.fail(error)

if len(array_solicitud_pendiente) == 0:
    bpm.fail(error)


tipoResultado = bpm.context.input['tipoResultado']
if tipoResultado == "finalizar":
    message = "Tarea cancelada"
else:
    message = "Solicitud procesada"

bpm.context.input['message'] = message




