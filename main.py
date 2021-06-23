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
time.sleep(5)

print("main loop ************************************** ->")
while True:
    randN=machine.rng()%10
    print("Interval=",end='');print(randN)

    if myconnect.connType=="None":
        myconnect.lteconnect()

    if not G.pybytes.isconnected():
        G.pybytes.connect()

    print("Pybytes Connected?= ",end='');print(G.pybytes.isconnected())
    print("ConnType=",end='');print(G.connType)

    time.sleep(randN+15)
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
