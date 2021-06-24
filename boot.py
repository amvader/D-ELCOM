# boot.py -- run on boot-up
import time
import machine
import pycom
import G

print("boot.py start->")
print("<- ********************************************* ->")

# boot.py -- run on boot-up
for j in range(0,2):
    pycom.rgbled(0xFF0000);time.sleep(.15)
    pycom.rgbled(0x0000FF);time.sleep(.15)
