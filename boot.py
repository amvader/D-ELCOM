# boot.py -- run on boot-up
import time
import machine
import pycom
print("boot.py start->")
from _pybytes import Pybytes
from _pybytes_config import PybytesConfig
global conf
conf = PybytesConfig().read_config()
print(conf)
global pybytes
pybytes = Pybytes(conf)

"""
import sqnsupgrade
print("*************************************")
print("Modem Firmware:",end='')
print(sqnsupgrade.info())
print("*************************************")
time.sleep(10)
"""

# boot.py -- run on boot-up
for j in range(0,2):
    pycom.rgbled(0x00000f)
    time.sleep(.05)
    pycom.rgbled(0x000000)
    time.sleep(.05)
    pycom.rgbled(0x000f00)
    time.sleep(.05)
    pycom.rgbled(0x000000)
    time.sleep(.05)
    pycom.rgbled(0x0f0000)
    time.sleep(.05)
    pycom.rgbled(0x000000)
    time.sleep(.05)
    pycom.rgbled(0x00000f)
    time.sleep(.05)
    pycom.rgbled(0x000000)
    time.sleep(.05)
    pycom.rgbled(0x000f00)
    time.sleep(.05)
    pycom.rgbled(0x000000)
    time.sleep(.05)
    pycom.rgbled(0x0f0000)
    time.sleep(.05)
    pycom.rgbled(0x000000)
