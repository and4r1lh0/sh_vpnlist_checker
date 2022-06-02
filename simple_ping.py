import platform
import subprocess

def myping(host):
    parameter = '-n' if platform.system().lower()=='windows' else '-c'

    command = ['ping', parameter, '1', host]
    response = subprocess.call(command,stdout=subprocess.DEVNULL,
    stderr=subprocess.STDOUT)

    if response == 0:
        return True
    else:
        return False