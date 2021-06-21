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

print("ConnType=",end='')
print(myconnect.connType())

randN=machine.rng()%10
rand2=randN%10

print("hello")
print(rand2)
time.sleep(20)
#myconnect.disconnect("WiFi")
print("good bye")
