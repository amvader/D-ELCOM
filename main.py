print("Start",end='')
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
print("ing Main...")

#START my code

pycom.heartbeat(True)
wlan=WLAN()
if not wlan.isconnected():
    myconnect.wifi(pybytes)

lte=LTE()
while not lte.isconnected():
    myconnect.lte(pybytes)


print("pycproc")
py = Pycoproc()
print("end pyco")

# Send data continuously to Pybytes
for i in range(0,20):

    pycom.heartbeat(False)
    connType="na"
    if lte.isconnected() and wlan.isconnected():
        print("conn=both ",end='')
        wlan.disconnect()
        connType="LTEwifi"
        pycom.rgbled(0xFF0000)
    elif lte.isconnected():
        print("conn=lte ",end='')
        connType="lte"
        pycom.rgbled(0x00FF00)
    elif wlan.isconnected():
        connType="wifi"
        print("conn=wifi ",end='')
        pycom.rgbled(0x0000FF)
    else:
        connType="none"
        pycom.heartbeat(True)
        print("conn=none ",end='')


    print(i)
    print(" -> ",end='')
    mp = MPL3115A2(py,mode=ALTITUDE)
    mp1 = mp.altitude() * 3.281 #convert to ft
    mp2 = int(mp1 * (10**2))/(10**2) #scalle to clip decimals...
    mp3 = float(mp2)
    battery_voltage = py.read_battery_voltage()
    if pybytes.isconnected():
        pybytes.send_signal(1, i)
        pybytes.send_signal(2, mp3 )
        pybytes.send_signal(3, battery_voltage )
        print('sent signals to pybytes...')


    print(" send ...", end='')
    mID=ubinascii.hexlify(machine.unique_id())
    dat={"deviceToken": "gpy-a1","altitude":mp3, "batteryV":battery_voltage, "connType":connType, "event":i }
    header={"content-type":"application/json"}
    link="https://amvader.net/iot/pycom/elcom-hook.php"
    r = urequest.post(link,json=dat,headers=header)
    print("Post Data Sent via HTTP " , end='')
    print(r)
    r.close()
    pycom.rgbled(0x000000)
    time.sleep(10)

pycom.heartbeat(False)
while True:
    pycom.rgbled(0xFF6600) # orange
    time.sleep(60)

print ("done")
sys.exit()
