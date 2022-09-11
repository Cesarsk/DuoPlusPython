import threading
import subprocess

from duolinguo import Duolinguo

if __name__ == '__main__':
    subprocess.call("clear")

    invitation_code = "BDHTZTB5CWWKT6DUXOFYXLVSRU"
    duo = Duolinguo(invitation_code=invitation_code)

    for i in range(200):
        t = threading.Thread(target=duo.create_account).start()
