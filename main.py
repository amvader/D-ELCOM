# main.py -- put your code here!
print("start main...")
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

#import urequest
#import ubinascii
#from network import LTE

#My Code
import myconnect

#START my code
print("start")

pycom.heartbeat(True)
myconnect.wifi(pybytes)

# Send data continuously to Pybytes
while True:
    for j in range(0,2):
        for i in range(0,20):
            pybytes.send_signal(1, math.sin(i/10*math.pi))
            print('sent signal {}'.format(i) + ' & signal' + str(j) )
            time.sleep(2)

print ("done")
print(pybytes.isconnected())
