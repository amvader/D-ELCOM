import time
import math
import pycom
from pycoproc_2 import Pycoproc
import machine
from MPL3115A2 import MPL3115A2,ALTITUDE,PRESSURE
import urequest
import ubinascii
from network import LTE
from network import WLAN
#from network import LTE

pycom.heartbeat(True)

py = Pycoproc()
#if py.read_product_id() != Pycoproc.USB_PID_PYSENSE:
#    raise Exception('Not a Pysense')

# Send data continuously to Pybytes
while True:
    for i in range(0,20):

        #if wlan.isconnected():
        #    connType="wifi"
        #if lte.isconnected():
        #    connType="lte"

        mp = MPL3115A2(py,mode=ALTITUDE)
        mp1 = mp.altitude() * 3.281
        mp2 = int(mp1 * (10**2))/(10**2)
        mp3 = float(mp2)
        battery_voltage = py.read_battery_voltage()

        #pybytes.send_signal(1, math.sin(i/10*math.pi))
        #pybytes.send_signal(2, mp3 )
        #pybytes.send_signal(3, battery_voltage )
        #print('sent signal {}'.format(i))

        mID=ubinascii.hexlify(machine.unique_id())

        connType="undefined"

        dat={"deviceToken": "gpy-a1","altitude":mp3, "batteryV":battery_voltage, "type":connType }
        header={"content-type":"application/json"}
        link="https://amvader.net/iot/pycom/elcom-hook.php"
        print("Sending HTTP Post Data")
        r = urequest.post(link,json=dat,headers=header)
        print("Post Data Sent")
        print(r)
        r.close()

        time.sleep(15)

def wyconnect():
    wlan = WLAN(mode=WLAN.STA)

    wlan.connect(ssid='NETGEAR25', auth=(WLAN.WPA2, 'littleshoe029'))
    while not wlan.isconnected():
        machine.idle()
    print("WiFi connected succesfully")

    print(wlan.ifconfig())

def uplink(var):
    print("uplink=" + var + "!")
