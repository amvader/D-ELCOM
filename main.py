# main.py -- put your code here!
from network import WLAN
from network import LTE
import pycom

#my libs
import myconnect


pycom.heartbeat(True)
print("hello")

lte=LTE()

myconnect.lte(pycom,lte)
