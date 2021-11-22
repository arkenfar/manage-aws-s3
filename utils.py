import subprocess
import traceback
import requests


def ping(host):
    try:
        command = ['ping', '-c', '1', host]
        traceback.print_stack()
        if subprocess.call(command) == 0:
            result = True
        else:
            result = False

        return result
    except Exception as err_ping:
        traceback.print_stack()
        raise err_ping


def req(url):
    try:
        res = requests.get(url)
        if res.status_code == 200 or res.status_code == 403:
            return True
        return False
    except Exception as err_req:
        traceback.print_stack()
        raise err_req
