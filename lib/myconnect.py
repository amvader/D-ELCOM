import os
import machine
import pycom
import time
import socket
from network import WLAN
from network import LTE
import _thread

wlan=WLAN()
lte=LTE()
beatcolor=0x0000ff


def wificonnect():
    wlan.mode(WLAN.STA)
    try:
        wlan.ifconfig(config=net_properties['wlan_config'])
        print(config)
        wlan.connect('SWS', auth=(WLAN.WPA2, 'ok321321'), timeout=10000)
        print("WiFi: connecting to SWS...",end='')
        while not wlan.isconnected():
            machine.idle() # save power while waiting
        print("Connected to "+net_to_use+" with IP address: " + wlan.ifconfig()[0])
    except Exception as e:
        print("WiFi connect try failure! ...")
        #wlan.disconnect()

def lteconnect():
    try:
        lte.attach( apn="iot.truphone.com")
        print("LTE: attaching..",end='')
        while not lte.isattached():
            time.sleep(0.25)
            print('.',end='')
            print(lte.send_at_cmd('AT!="fsm"'))         # get the System FSM
            #print("band 13")
        print("attached!")
        lte.connect()
        print("LTE: connecting...",end='')
        while not lte.isconnected():
            machine.idle()
        print("Connected by LTE!")
    except Exception as e:
        print("LTE connect try failure! ...")

def disconnect(net):
    if net=="WiFi":
        wlan.disconnect()
        print("disconnect wifi")
        time.sleep(1)
    elif net=="LTE":
        lte.disconnect()
        print("disconnect lte")
        time.sleep(1)



def connType():
    if lte.isconnected() and wlan.isconnected():
        return "LTEWiFi"
    elif wlan.isconnected():
        return "WiFi"
    elif lte.isconnected():
        return "LTE"
    else:
        return ("None")


def myheart(bps,colorH):
    while True:
        try:
            if lte.isconnected() and wlan.isconnected():
                colorH=0x00ff00
            elif wlan.isconnected():
                colorH=0x0000ff
            elif lte.isconnected():
                colorH=0xffffff
            else:
                colorH=0xff0000
            pycom.rgbled(colorH)
            time.sleep(.1)
            pycom.rgbled(0x000000)
            time.sleep(bps)
        except:
            print("")


def startheart():
    _thread.start_new_thread(myheart, (2, beatcolor))
