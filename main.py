# main.py -- put your code here!
# Import what is necessary to create a thread
import time
import math
from network import WLAN
import machine
import pycom
from pycoproc_2 import Pycoproc
from MPL3115A2 import MPL3115A2,ALTITUDE,PRESSURE
import urequest
import ubinascii
from network import LTE
from network import WLAN
import sys

#import urequest
#import ubinascii
#from network import LTE

#My Code
import myconnect

#START my code
print("Main...")

pycom.heartbeat(True)
#wlan=WLAN()
#if not wlan.isconnected():
#    myconnect.wifi(pybytes)

lte=LTE()
while not lte.isconnected():
    myconnect.lte(pybytes)



py = Pycoproc()

# Send data continuously to Pybytes
for i in range(0,20):

    mp = MPL3115A2(py,mode=ALTITUDE)
    mp1 = mp.altitude() * 3.281
    mp2 = int(mp1 * (10**2))/(10**2)
    mp3 = float(mp2)
    battery_voltage = py.read_battery_voltage()
    pybytes.send_signal(1, math.sin(i/10*math.pi))
    pybytes.send_signal(2, mp3 )
    pybytes.send_signal(3, battery_voltage )
    print('sent signals to pybytes')

    connType="undefined"
    mID=ubinascii.hexlify(machine.unique_id())
    dat={"deviceToken": "gpy-a1","altitude":mp3, "batteryV":battery_voltage, "type":connType }
    header={"content-type":"application/json"}
    link="https://amvader.net/iot/pycom/elcom-hook.php"
    r = urequest.post(link,json=dat,headers=header)
    print("Post Data Sent via HTTP " )
    print(r)
    r.close()

    time.sleep(10)

pycom.heartbeat(False)
while True:
    pycom.rgbled(0xFF6600) # orange
    time.sleep(60)

print ("done")
sys.exit()
