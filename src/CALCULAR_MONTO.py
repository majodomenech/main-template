#!python3
import redflagbpm
from GET_COTIZACIONES import cotiz_dict


if __name__ == '__main__':
    bpm = redflagbpm.BPMService()

    id_fondo = bpm.context['id_fondo']
    bpm.context.input['monto'] = cotiz_dict['precio'] * bpm.context['cantidad_importe']

    cantidad_importe = bpm.context['cantidad_importe']
