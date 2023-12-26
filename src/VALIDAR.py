#!python3
import redflagbpm

def validar_solicitudes_no_vacias(bpm):
    error = '[[[No hay solicitudes pendientes]]]'
    try:
        array_solicitud_pendiente = bpm.context.input['array_solicitud_pendiente']
    except:
        array_solicitud_pendiente = None
    try:
        array_solicitud_confirmada = bpm.context['array_solicitud_confirmada']
    except:
        array_solicitud_confirmada = None

    # si no hay solicitudes pendientes ni confirmadas arroja error
    if (array_solicitud_pendiente is None or len(array_solicitud_pendiente) == 0) and (array_solicitud_confirmada is None or len(array_solicitud_confirmada) == 0):
        bpm.fail(error)
    #si no hay solicitudes pendientes pero si confrimadas y le dan continuar, el proceso se finaliza
    elif (array_solicitud_pendiente is None or len(array_solicitud_pendiente) == 0) and (array_solicitud_confirmada is not None or len(array_solicitud_confirmada) > 0):
        bpm.context['finalizar_carga'] = True
        bpm.reply("No se puede continuar")
    #si hay solicitudes pendientes y hay o no confimradas, es el camino feliz: else:pass

def custom_message(tipoResultado):
    if tipoResultado == "finalizar":
        message = "Tarea cancelada"
    else:
        message = "Solicitud procesada"

    bpm.context.input['message'] = message



if __name__ == '__main__':
    bpm = redflagbpm.BPMService()
    validar_solicitudes_no_vacias(bpm)
    tipoResultado = bpm.context.input['tipoResultado']
    custom_message(tipoResultado)
