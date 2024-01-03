#!python3
from GET_FCI_INFO import get_moneda_fondo
import redflagbpm
import re

bpm = redflagbpm.BPMService()
array_solicitud_pendiente = bpm.context['array_solicitud_pendiente']
for solicitud in array_solicitud_pendiente:
    # leo el user input
    fondo_deno = solicitud['fondo']
    # extraigo el codigo de fci
    matches = re.search(r'(\d+)', fondo_deno)
    codigo_fci = matches.group(1)
    # busco la moneda original del fondo
    moneda_fondo = get_moneda_fondo(codigo_fci=codigo_fci)
    # guardo la moneda en el array original
    solicitud['moneda'] = moneda_fondo

bpm.context.input['array_solicitud_pendiente'] = array_solicitud_pendiente
