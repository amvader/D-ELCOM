print("boot",end='')
import time
import pycom
import machine
from _pybytes import Pybytes
from _pybytes_config import PybytesConfig

# boot.py -- run on boot-up
print("ing",end='')
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

print("...")
"""
print("Setup pybytes...",end='')
pycom.nvs_set('pybytes_debug', 99)

conf = PybytesConfig().read_config()
pybytes = Pybytes(conf)
#pybytes.start()
print('done')
print("Pybytes connected=",end='')
print(pybytes.isconnected())
"""
