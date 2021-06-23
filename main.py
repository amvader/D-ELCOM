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

G.pconfig(True)
#time.sleep(5)

myconnect.startheart()
time.sleep(3)
interval=1
myconnect.startConn(True,True,60)
print("main loop ************************************** ->")
while True:
    randN=machine.rng()%10
    print("Interval=",end='');print(interval)


    if G.pybytes.isconnected():
        G.pybytes.send_signal(2, interval)

    print("Pybytes Connected?= ",end='');print(G.pybytes.isconnected(),end='')
    print(" Network Connected?= ",end='');print(G.connType,' / ',myconnect.connType())

    time.sleep(30)
    interval+=1
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
