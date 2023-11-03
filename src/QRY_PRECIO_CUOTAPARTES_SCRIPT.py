#!python3
import json
import redflagbpm
from endpoints_santander import login_apigee, get_all_funds, get_fund_by_id

def get_fundId():

    sql = """
        select uni."CODIGO", 
                uni."NOMBRE", 
               atr."VALOR" as fund_id
        from "UNI_UNIDAD" uni
            inner join "UNI_ATRIBUTO" atr 
                on atr."UNIDAD"=uni."UNI_UNIDAD_ID"
                   and atr."ATRIBUTO" = 'FundId Santander'
    """

def main():
    headers = login_apigee()
    response = get_all_funds(headers)
    all_funds = json.dumps(response.json(), indent=4, sort_keys=True, ensure_ascii=False)

    all_funds = json.loads(all_funds)
    for fund in all_funds['results']:
        response_by_id = get_fund_by_id(headers, fund['id'])
        response_by_id = json.dumps(response_by_id.json(), indent=4, sort_keys=True, ensure_ascii=False)
        print(response_by_id)
        response_by_id = json.loads(response_by_id)
        fund['precio_cp'] = response_by_id['currentShareValue']
        fund['status_precio'] = response_by_id['status']
        fund['fecha_valuacion'] = response_by_id['valueDate']
        break
    #pretty print all_funds
    pretty_all_funds = json.dumps(all_funds, indent=4, sort_keys=True, ensure_ascii=False)
    # print(pretty_all_funds)
    # get_precio_cp_x_fondo(headers)
    # json_qry = json.loads(json_qry)
    # print(json_qry)
    with open('/tmp/qry_precio_cp.json', 'w') as f:
        json.dump(all_funds, f)

    bpm = redflagbpm.BPMService()
    _responseHeaders = bpm.context.json._responseHeaders
    _responseHeaders["status"] = "200"
    _responseHeaders["Content-Type"] = "application/json"
    _responseHeaders["Content-Encoding"] = "UTF-8"
    _responseHeaders["resource"] = "/tmp/qry_marga.json"

if __name__ == '__main__':
    main()
