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
#time.sleep(5)

myconnect.startheart()
time.sleep(3)
interval=1
print("main loop ************************************** ->")
while True:
    randN=machine.rng()%10
    print("Interval=",end='');print(interval)

    if myconnect.connType()=="None":
        myconnect.lteconnect()

    if not G.pybytes.isconnected():
        G.pybytes.connect()

    if G.pybytes.isconnected():
        G.pybytes.send_signal(1, interval)

    print("Pybytes Connected?= ",end='');print(G.pybytes.isconnected())
    print("ConnType=",end='');print(G.connType)

    time.sleep(randN+15)
    interval+=1
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
