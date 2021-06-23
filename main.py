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
myconnect.startConn()
print("main loop ************************************** ->")
while True:
    randN=machine.rng()%10
    print("Interval=",end='');print(interval)


    if G.pybytes.isconnected():
        G.pybytes.send_signal(1, interval)

    print("Pybytes Connected?= ",end='');print(G.pybytes.isconnected(),end='')
    print(" Network Connected?= ",end='');print(G.connType,' / ',myconnect.connType())

    time.sleep(5)
    interval+=1
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
