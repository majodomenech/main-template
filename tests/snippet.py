#!python3
import re

final_results = ['guara guara', 'Suscripcion Alta: Ya existe una solicitud pendiente con estos datos. Por favor actualice la solicitud previa.', 'Suscripcion Alta: Ya existe una solicitud pendiente con estos datos. Por favor actualice la solicitud previa.']

pattern = '(Ya existe una solicitud pendiente con estos datos. Por favor actualice la solicitud previa.)'

for res in final_results:
    #comparo con el error de solicitud repetida
    try:
        err_solicitud_duplicada = re.search(pattern, res).group(1)
    except AttributeError:
        err_solicitud_duplicada = None
    print(err_solicitud_duplicada)
