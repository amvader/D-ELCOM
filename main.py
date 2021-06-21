# main.py -- put your code here!

import pycom
import _thread
import time
#import globals
#my libs
import myconnect
import machine


#pycom.heartbeat(True)
print("hello")

myconnect.startheart()
time.sleep(10)
myconnect.lteconnect()

while True:
    print("ConnType=",end='')
    print(myconnect.connType())

    randN=machine.rng()%10

    print("hello! Interval=",end='')
    print(randN)
    time.sleep(randN)
    myconnect.disconnect("WiFi")
    myconnect.disconnect("LTE")
    time.sleep(2)
    if (randN==2 or randN==4 or randN==6 or randN==8):
        myconnect.wificonnect()
    else:
        myconnect.lteconnect()
    print("good bye")
