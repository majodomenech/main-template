#!python3
import redflagbpm

def get_pass_key():
    bpm = redflagbpm.BPMService()
    if bpm.service.text("STAGE") == "DEV":
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
