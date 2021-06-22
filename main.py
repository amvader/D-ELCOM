# main.py -- put your code here!

import pycom
import _thread
import time
import machine
#import globals
#my libs
import myconnect
import G

#pycom.heartbeat(True)
print("main.py start->",G.x)
print("<- ********************************************* ->")

G.pconfig()
time.sleep(5)

myconnect.startheart()
myconnect.lteconnect()
G.pconfig()
time.sleep(5)

print("main loop ************************************** ->")
while True:
    randN=machine.rng()%10
    print("hello! Interval=",end='')
    print(randN)

    if (randN==2 or randN==4 or randN==6 or randN==8):
        myconnect.lteconnect()
    else:
        myconnect.wificonnect()

    if myconnect.connType()=="None":
        time.sleep(5)
    else:
        print("Pybytes Connected?= ",end='')
        print(G.pybytes.isconnected())

    print("ConnType=",end='')
    print(myconnect.connType())


    #if not pybytes.isconnected():
    #    pybytes.connect()

    time.sleep(randN+60)

    myconnect.disconnect("WiFi")
    myconnect.disconnect("LTE")
    time.sleep(2)
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
