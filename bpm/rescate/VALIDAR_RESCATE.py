#!python3
import redflagbpm

def validar_solicitudes_no_vacias(bpm):
    error = '[[[No hay solicitudes pendientes]]]'
    try:
        array_solicitudes_pendientes = bpm.context.input['array_solicitudes_pendientes']
    except:
        array_solicitudes_pendientes = None
    try:
        array_solicitudes_confirmadas = bpm.context['array_solicitudes_confirmadas']
    except:
        array_solicitudes_confirmadas = None

    # si no hay solicitudes pendientes ni confirmadas arroja error
    if (array_solicitudes_pendientes is None or len(array_solicitudes_pendientes) == 0) and (array_solicitudes_confirmadas is None or len(array_solicitudes_confirmadas) == 0):
        bpm.fail(error)
    elif (array_solicitudes_pendientes is not None):
        for solicitud in array_solicitudes_pendientes:
            if ('monto' not in solicitud or
                    solicitud['monto'] is None or
                    'cantidad_importe' not in solicitud or
                    solicitud['cantidad_importe'] is None):
                bpm.fail('[[[Antes de continuar debe presionar "Calcular"]]]')

    #si no hay solicitudes pendientes pero si confrimadas y le dan continuar, el proceso se finaliza
    elif (array_solicitudes_pendientes is None or len(array_solicitudes_pendientes) == 0) and (array_solicitudes_confirmadas is not None or len(array_solicitudes_confirmadas) > 0):
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
