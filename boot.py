# boot.py -- run on boot-up
import time
import machine
import pycom
print("boot.py start->")

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
