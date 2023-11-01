#!python3
import json
import re
import urllib
from datetime import date, timedelta
import redflagbpm
from decimal import Decimal
import psycopg2
import psycopg2.extras
from endpoints_santander import login_apigee, get_all_funds, get_fund_by_id, get_fund_by_id_details


def main():
    headers = login_apigee()
    response = get_all_funds(headers)
    all_funds = json.dumps(response.json(), indent=4, sort_keys=True, ensure_ascii=False)

    all_funds = json.loads(all_funds)
    for fund in all_funds['results']:
        response_by_id_details = get_fund_by_id_details(headers, fund['id'])
        response_by_id_details = json.dumps(response_by_id_details.json(), indent=4, sort_keys=True, ensure_ascii=False)
        print(response_by_id_details)
        response_by_id_details = json.loads(response_by_id_details)
        fund['codigo_cv'] = response_by_id_details['CVCode']
        break
    #pretty print all_funds
    pretty_all_funds = json.dumps(all_funds, indent=4, sort_keys=True, ensure_ascii=False)
    print(pretty_all_funds)

if __name__ == '__main__':
    main()
