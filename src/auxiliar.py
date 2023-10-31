#!python3
import pycurl
from io import BytesIO
import psycopg2
import psycopg2.extras
import datetime

def procesar_respuesta(resp, error_list, context, tarea):
    if resp.status_code == 400 and context is not None:
        err = [tarea+' ' + resp.json()['code'] + resp.json()['message']]
        [error_list.append(tarea+' ' +  resp.json()['message'] + str(context))]
        return False, str(err)
    elif resp.status_code == 400 and context is None:
        err = [tarea+' ' + resp.json()['code'] + resp.json()['message']]
        [error_list.append(tarea+' '  + resp.json()['code'] + resp.json()['message'])]
        return False, str(err)
    elif resp.status_code == 200 or resp.status_code == 201:
        return True, None
    elif resp.status_code == 409:
        err = tarea+' ' + 'Conflicto: ' + resp.text
        error_list.append(err)
        return False, str(err)
    else:
        print("Error en el request")
        print(resp)
        err = tarea+' ' +str(resp.status_code)+ ' ' + resp.text
        error_list.append(err)
        return False, str(err)
def get_fecha_liquidacion(plazo_habil):
    today = datetime.date.today()

    url = "https://ws.sycinversiones.com/plazoHabil?fecha="+str(today)+"&dias="+str(plazo_habil)

    # Create a BytesIO object to store the response
    buffer = BytesIO()

    # Create the pycurl request
    curl = pycurl.Curl()
    curl.setopt(pycurl.URL, url)
    curl.setopt(pycurl.HTTPHEADER, ['accept: text/plain'])
    curl.setopt(pycurl.WRITEDATA, buffer)

    # Perform the request
    curl.perform()

    # Get the response code and close the request
    response_code = curl.getinfo(pycurl.RESPONSE_CODE)
    curl.close()

    # Check if the request was successful (status code 200)
    if response_code == 200:
        # Get the response content from the buffer and print it
        response_content = buffer.getvalue().decode('utf-8')
        # print(response_content)
    else:
        print(f"Request días hábiles failed with status code: {response_code}")

    return response_content

#get last business day in Argentina excluding weekends and holidays
def get_b_day(fecha_alta_hasta, days):
    # URL and parameters
    url = f"https://ws.sycinversiones.com/plazoHabil?fecha={fecha_alta_hasta}&dias=-{days}"

    # Create a BytesIO object to store the response
    response_buffer = BytesIO()

    # Create a pycurl.Curl object
    curl = pycurl.Curl()

    # Set the URL
    curl.setopt(curl.URL, url)

    # Set the HTTP headers
    curl.setopt(curl.HTTPHEADER, ['accept: text/plain'])

    # Set the response buffer
    curl.setopt(curl.WRITEDATA, response_buffer)

    # Perform the GET request
    curl.perform()

    # Get the HTTP response code
    http_response_code = curl.getinfo(pycurl.HTTP_CODE)

    # Close the curl session
    curl.close()

    # Get the response content
    response_content = response_buffer.getvalue().decode('utf-8')

    # Print the response
    # print("HTTP Response Code:", http_response_code)
    # print("Response Content:", response_content)
    return response_content

def get_resc_id(conn, id_origen):
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    sql = """
        select id_rescate from FCISTDR.rescate_status
        where id_origen = %s
    """
    cur.execute(sql, (id_origen,), )
    qry = cur.fetchall()
    cur.close()
    return qry

def get_suscr_id(conn, id_origen):
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    sql = """
        select id_suscri from FCISTDR.suscripcion_status
        where id_origen = %s
    """
    cur.execute(sql, (id_origen,), )
    qry = cur.fetchall()
    cur.close()
    return qry