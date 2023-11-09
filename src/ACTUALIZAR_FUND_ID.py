#!python3
import json
from endpoints_santander import login_apigee, get_all_funds, get_fund_by_id_details
import redflagbpm
from redflagbpm import PgUtils

def call_stdr_fund_endpoints(headers):
    response = get_all_funds(headers)
    all_funds = json.dumps(response.json(), indent=4, sort_keys=True, ensure_ascii=False)
    all_funds = json.loads(all_funds)
    for fund in all_funds['results']:
        response_by_id_details = get_fund_by_id_details(headers, fund['id'])
        response_by_id_details = json.dumps(response_by_id_details.json(), indent=4, sort_keys=True, ensure_ascii=False)
        response_by_id_details = json.loads(response_by_id_details)
        fund['codigo_cv'] = response_by_id_details['CVCode']

    # pretty print all_funds
    pretty_all_funds = json.dumps(all_funds, indent=4, sort_keys=True, ensure_ascii=False)
    return pretty_all_funds

def update_fund_id(bpm, **kwargs):
    with PgUtils.get_connection(bpm, 'SyC_RW') as conn:
        conn.autocommit = False
        with conn.cursor() as cursor:
            sql_actualizar = """
                            update public."UNI_ATRIBUTO"
                            set "VALOR"= %s
                            where "UNIDAD"=(select "UNI_UNIDAD_ID" from "UNI_UNIDAD" where "SUBCODIGO"= %s)
                            and "ATRIBUTO" = %s;
                        """
            sql_insertar = """
                                INSERT INTO public."UNI_ATRIBUTO"("UNIDAD", "ATRIBUTO", "VALOR")
                                VALUES ((select "UNI_UNIDAD_ID" from "UNI_UNIDAD" where "SUBCODIGO"=%s), %s, %s);
                            """

            unidad = kwargs['cv_id']
            valor = kwargs['stdr_fund_id']
            atributo = 'FundId Santander'
            cursor.execute(sql_actualizar,(valor, unidad, atributo,))
            rowcount = cursor.rowcount
            if rowcount == 0:
                cursor.execute(sql_insertar,(unidad, atributo, valor,))
            else:
                pass
            conn.commit()
    return


def main():
    headers = login_apigee()
    bpm = redflagbpm.BPMService()
    funds_w_cv_code = call_stdr_fund_endpoints(headers)

    for i in json.loads(funds_w_cv_code)['results']:
        if i['codigo_cv'] is not None and i['codigo_cv'] != '':
            update_fund_id(bpm, **{'stdr_fund_id': str(i['id']), 'cv_id': str(i['codigo_cv'])})



if __name__ == '__main__':
    main()
