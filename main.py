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
