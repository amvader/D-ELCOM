import pycom
from _pybytes import Pybytes
from _pybytes_config import PybytesConfig
import myconnect

x='!'
global conf
global pybytes
global connType

#device_id="9c8cab6e-f412-4a6d-beb5-3b03d54975c9" #fipy-a1
device_id="92e7be30-699e-4ac6-be7e-94b5adce1fa7" #gpy-a1


connType="None" #default to none until set

def pconfig(update):
    global conf
    global pybytes
    conf = PybytesConfig().read_config()
    pybytes = Pybytes(conf)
    if update:
        #print("OLD Conf -> ****");#print(conf)
        pybytes.update_config("wifi", value={"ssid": "SWS", "password": "ok321321"}, permanent=False, silent=False, reconnect=False)
        pybytes.update_config("device_id", value=device_id, permanent=True, silent=False, reconnect=True)
        nets="lte,wifi"
        pybytes.update_config("network_preferences", value="lte", permanent=False, silent=False, reconnect=False)
        conf = PybytesConfig().read_config()
        print("New Conf -> ****");print(conf)




"""
**************************************************************
**** THIS IS CODE SNIPPETS TO REMEMBER LATER
**************************************************************
"""
"""
import sqnsupgrade
print("*************************************")
print("Modem Firmware:",end='')
print(sqnsupgrade.info())
print("*************************************")
time.sleep(10)



print(G.conf)
G.pybytes = Pybytes(G.conf)

"""
