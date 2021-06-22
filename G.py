import pycom
from _pybytes import Pybytes
from _pybytes_config import PybytesConfig

x='!'
global conf
global pybytes

def pconfig():
    global conf
    global pybytes
    conf = PybytesConfig().read_config()
    pybytes = Pybytes(conf)
    print("OLD Conf -> ****")
    print(conf)
    pybytes.update_config("wifi", value={"ssid": "SWS2", "password": "ok321321"}, permanent=False, silent=False, reconnect=False)
    nets="lte,wifi"
    pybytes.update_config("network_preferences", value="lte", permanent=False, silent=False, reconnect=False)
    #conf = PybytesConfig().read_config()
    print("New Conf -> ****")
    print(conf)




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
