#!python3
import redflagbpm
def custom_message(tipoResultado):
    if tipoResultado == "ok":
        message = "Solicitud procesada"

        bpm.context.input['message_2'] = message

if __name__ == '__main__':
    bpm = redflagbpm.BPMService()
    tipoResultado = bpm.context.input['tipoResultado']
    custom_message(tipoResultado)
