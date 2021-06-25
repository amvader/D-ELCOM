# main.py -- put your code here!

import pycom
import _thread
import time
import machine
from pycoproc_2 import Pycoproc
from MPL3115A2 import MPL3115A2,ALTITUDE,PRESSURE

#import globals
#my libs
import myconnect
import G



#pycom.heartbeat(True)
print("main.py start->",G.x)
print("<- ********************************************* ->")

"""
"""
G.initSD()
# check the content
if G.sd:
    print(os.listdir('/sd'))
    # try some standard file operations
    #f = open('/sd/test.txt', 'w')
    #f.write('Testing SD card write operations')
    #f.close()
    f = open('/sd/test.txt', 'r')
    print("File:")
    print(f.read())
    f.close()


G.pconfig(False)
#time.sleep(5)

myconnect.startheart()
time.sleep(3)
interval=1
myconnect.startConn(True,True,60)


def getElevDat():
        py = Pycoproc()
#        print(i)
#        print(" -> ",end='')
        mp = MPL3115A2(py,mode=ALTITUDE)
        mp1 = mp.altitude() * 3.281 #convert to ft
        mp2 = int(mp1 * (10**2))/(10**2) #scalle to clip decimals...
        mp3 = float(mp2)
        battery_voltage = py.read_battery_voltage()
        return mp3,battery_voltage

def send2Amel():
        print("send2Amel")
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
'''
        print(" send http...", end='')
        mID=ubinascii.hexlify(machine.unique_id())
        dat={"deviceToken": mID,"altitude":mp3, "batteryV":battery_voltage, "connType":connType, "event":i }
        header={"content-type":"application/json"}
        link="https://amvader.net/iot/pycom/elcom-hook.php"
        r = urequest.post(link,json=dat,headers=header)
        print("Post Data Sent via HTTP " , end='')
        print(r)
        r.close()
        pycom.rgbled(0x000011)
        time.sleep(5)
'''


print("main loop ************************************** ->")
while True:
    randN=machine.rng()%10
    print("Interval=",end='');print(interval)

    if not G.connType=="None" :
        dat=getElevDat()
        print("Dat:",dat)

    if G.pybytes.isconnected():
        G.pybytes.send_signal(2, interval)

    try:
        if G.sd:
            f = open('/sd/test.txt', 'r')
            print("File:")
            print(f.read())
            f.close()
    except:
        print("No SD")

    print("Pybytes Connected?= ",end='');print(G.pybytes.isconnected(),end='')
    print(" Network Connected?= ",end='');print(G.connType,' / ',myconnect.connType())

    time.sleep(15)
    interval+=1
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
