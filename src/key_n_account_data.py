#!python3
import redflagbpm

def endpoint_calling_data():
    bpm = redflagbpm.BPMService()
    if bpm.service.text("STAGE") == 'DEV':
        url_base = "https://sbx.santander.com.ar"
        client_id = 'e3fa0fa8-ec9d-406b-960a-150071b151a7'
    else:
        url_base = "https://api.santander.com.ar"
        client_id = '9v7Z1boPQ5CkGzsAhOXMtpcWL0EBRXmo'
    return url_base, client_id

def get_pass_key():
    bpm = redflagbpm.BPMService()
    if bpm.service.text("STAGE") == 'DEV':
        # Credenciales Sandbox:
        # Consumer Key:
        KEY = "At8tRQKSwSylWDnDjHMFAvCbpSreukE0"
        # Consumer Secret
        PRIVATE = "jZRT5p5KR2yEknBbacFzBkxGxDxNBl29"
    else:
        # Credenciales Productivas:
        # Consumer Key:
        KEY = "9v7Z1boPQ5CkGzsAhOXMtpcWL0EBRXmo"
        # Consumer Secret:
        PRIVATE = "X5XvmVmV9ZpZZfuFquDRtmkhun7zMHWR"
    return str(KEY+":"+PRIVATE)


def get_account_data():
    bpm = redflagbpm.BPMService()
    account_data = {}
    if bpm.service.text("STAGE") == 'DEV':
        # suscris test
        account_data['investmentAccount'] = 2707138
        account_data['UBK'] = "0720099188000037875486"
        # # rescates test
        # account_data['investmentAccount'] = 41621350
        # account_data['UBK'] = "0720247820000008610672"
    else:
        account_data['investmentAccount'] = 47519688
        account_data['UBK'] = "0720247820000008610672"
    return account_data
