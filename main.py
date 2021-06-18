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

pycom.nvs_set('pybytes_debug', 99)

pycom.heartbeat(True)
wlan=WLAN()
lte=LTE()

time.sleep(7)

print("pycproc")
py = Pycoproc()
print("end pyco")
k=1
while True:
    k=k+5
    #recheck connection, maybe this is done on interupt?
    if not lte.isconnected() and not wlan.isconnected():
        myconnect.lte(pybytes,lte)
        time.sleep(1)
    if not wlan.isconnected() and not lte.isconnected():
        time.sleep(5)
        if not lte.isconnected():
            myconnect.wifi(pybytes,wlan)

    # Send data continuously to Pybytes
    for i in range(1,6):

        pycom.heartbeat(False)
        connType="na"
        if lte.isconnected() and wlan.isconnected():
            print("conn=both ",end='')
            #wlan.disconnect()
            connType="LTEwifi"
            pycom.rgbled(0xff33fb)
        elif lte.isconnected():
            print("conn=lte ",end='')
            connType="LTE"
            pycom.rgbled(0x002200)
        elif wlan.isconnected():
            connType="wifi"
            print("conn=wifi ",end='')
            pycom.rgbled(0xff0000)
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
        '''
        if pybytes.isconnected():
            pybytes.send_signal(1, i)
            pybytes.send_signal(2, mp3 )
            pybytes.send_signal(3, battery_voltage )
            print('+pybytes+...')
        else:
            print(" XpybytesX. ",end='')
            #pybytes.reconnect()
        '''

        print(" send http...", end='')
        mID=ubinascii.hexlify(machine.unique_id())
        dat={"deviceToken": mID,"altitude":mp3, "batteryV":battery_voltage, "connType":connType, "event":k+i }
        header={"content-type":"application/json"}
        link="https://amvader.net/iot/pycom/elcom-hook.php"
        r = urequest.post(link,json=dat,headers=header)
        print("Post Data Sent via HTTP " , end='')
        print(r)
        try:
            r.close()
            pycom.rgbled(0x000011)
            time.sleep(10)
        except:
            if r=="XXX":
                while true:
                    pycom.rgbled(0xff00ff)
                    time.sleep(.3)
                    pycom.rgbled(0x000000)
                    time.sleep(.25)

    pycom.heartbeat(False)
    pycom.rgbled(0xFF66B2) # orange
    time.sleep(20)

    pycom.rgbled(0x990000)
    print ("done")
    time.sleep(20)
