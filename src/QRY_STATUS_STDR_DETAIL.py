#!python3
import redflagbpm
import json

bpm = redflagbpm.BPMService()
# Uso la selección del usuario (ve el listado de suscris y rescates de BYMA)

str_reply = ''
try:
    tipo = bpm.context['tipo']
    certificate_id = bpm.context['certificate_id'] if bpm.context['certificate_id'] is not None else ''
    especie = bpm.context['especie']
    estado = bpm.context['estado']
    cantidad_cp = bpm.context['cantidad_cp']
    fecha_alta = bpm.context['fecha_alta']
    id_origen = bpm.context['id_origen']
    str_reply+= f"""Tipo: {tipo}
                    Certificate ID: {certificate_id}
                    Especie: {especie}
                    Estado: {estado}
                    Cantidad Cuotapartes: {cantidad_cp}
                    Fecha alta: {fecha_alta}
                    Id HG: {id_origen}\n\n"""


    try:
        descripcion = json.loads(bpm.context['descripcion'])
        for i in descripcion['errores']:
            for k, v in i.items():
                str_reply += k + ': '
                str_reply += str(v) + '\t'
            str_reply += '\n'
    except:
        descripcion = None

    def crearDesc(descripcion):
        if descripcion != None:
            ret = "<table class=\"tg\">"
            ret += "<tr><th class=\"bold gray\">ERRORES</th></tr>"
            for i in descripcion['errores']:
                ret += f"<tr><td class=\"tg-0lax center\">{i['descripcion']}</td></tr>"
            ret +="</table>"

            return ret

    html = """
    <div>
        <style type="text/css">
            .tg  {border-collapse:collapse;border-spacing:0;margin:0px auto; width:100%;}
            .tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
              overflow:hidden;padding:10px 5px;word-break:normal;}
            .tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;word-break:normal;}
            .tg .tg-0lax{text-align:left;vertical-align:top;}
            .center{text-align:center !important;}
            .bold{font-weight:700;}
            .gray{background-color: lightgray;}
            .fiftyw{width:52.5%;}
            .leftp{padding-left: 30px !important;}
            </style>""" + f"""
            <table class="tg">
            <tbody>
            <tr>
                <td class="tg-0lax bold gray fiftyw leftp">TIPO</td>
                <td class="tg-0lax center">{tipo}</td>
            </tr>
            <tr>
                <td class="tg-0lax bold gray leftp">Certificate ID</td>
                <td class="tg-0lax center"><span style="font-weight:400;font-style:normal">{certificate_id}</span></td>
            </tr>
            <tr>
                <td class="tg-0lax bold gray leftp">ESPECIE</td>
                <td class="tg-0lax center">{especie}</td>
            </tr>
            <tr>
                <td class="tg-0lax bold gray leftp">ESTADO</td>
                <td class="tg-0lax center">{estado}</td>
            </tr>
            <tr>
                <td class="tg-0lax bold gray leftp">CANTIDAD CUOTAPARTES</td>
                <td class="tg-0lax center">{cantidad_cp}</td>
            </tr>
            <tr>
                <td class="tg-0lax bold gray leftp">FECHA ALTA</td>
                <td class="tg-0lax center">{fecha_alta}</td>
            </tr>
            <tr>
                <td class="tg-0lax bold gray leftp">ID HG</td>
                <td class="tg-0lax center">{id_origen}</td>
            </tr>
            </tbody>
            </table>
</div>
    """

    # mensaje pop-up HTML
    bpm.reply({
    "type": "MESSAGE",
    "statusMessage": html,
    "statusMessageContentType": "text/html"
    })
except:
      # print(bpm.context)
      bpm.fail()


