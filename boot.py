# boot.py -- run on boot-up
import time
import machine
import pycom
import gbl

print("boot.py start->")
print("<- ********************************************* ->")


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
