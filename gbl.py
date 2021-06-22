import pycom
from _pybytes import Pybytes
from _pybytes_config import PybytesConfig

x=3
conf = PybytesConfig().read_config()
pybytes = Pybytes(conf)

def pconfig():
    gbl.pybytes = Pybytes(gbl.conf)
    print("OLD Conf -> ****")
    print(gbl.conf)
    gbl.pybytes.update_config("wifi", value={"ssid": "SWS", "password": "ok321321"}, permanent=True, silent=False, reconnect=False)
    gbl.conf = PybytesConfig().read_config()
    print("New Conf -> ****")
    print(gbl.conf)




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



print(gbl.conf)
gbl.pybytes = Pybytes(gbl.conf)

"""
