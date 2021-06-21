import os
import machine
import pycom
from network import LTE
import time
import socket
from network import WLAN
from network import LTE
import _thread
from _pybytes import Pybytes
from _pybytes_config import PybytesConfig

wlan=WLAN()
lte=LTE()
beatcolor=0x0000ff
global conf
conf = PybytesConfig().read_config()
global pybytes
pybytes = Pybytes(conf)


def wificonnect():
    #uart = machine.UART(0, 115200)
    #os.dupterm(uart)

    known_nets = {
        'AMEL': {'pwd': 'b00b121374'},
        'AmelSWS': {'pwd': 'nancy3stl4'},
        'Amvader1': {'pwd': '4053085956'},
        'Amvader2': {'pwd': '4053085956'},
        'NETGEAR25': {'pwd': 'littleshoe029'},
        'SWS': {'pwd': 'ok321321'}}

    #if machine.reset_cause() != machine.SOFT_RESET:
    from network import WLAN
    #wlan = WLAN()
    wlan.mode(WLAN.STA)
    original_ssid = wlan.ssid()
    original_auth = wlan.auth()

    print("Scanning for known wifi nets")

    try:
        available_nets = wlan.scan()
    except Exception as e:
        print("Failed to scan available nets-")

    try:
        nets = frozenset([e.ssid for e in available_nets])
    except Exception as e:
        print("Failed to scan frozen nets-")
        nets = known_nets


    known_nets_names = frozenset([key for key in known_nets])
    try:
        net_to_use = list(nets & known_nets_names)
        try:
            net_to_use = net_to_use[0]
            net_properties = known_nets[net_to_use]
            pwd = net_properties['pwd']
            sec = [e.sec for e in available_nets if e.ssid == net_to_use][0]
            if 'wlan_config' in net_properties:
                wlan.ifconfig(config=net_properties['wlan_config'])
            wlan.connect(net_to_use, (sec, pwd), timeout=10000)
            while not wlan.isconnected():
                machine.idle() # save power while waiting
            print("Connected to "+net_to_use+" with IP address: " + wlan.ifconfig()[0])
            print("reconnect pybytes by WIFI...")
            pybytes.connect()

        except Exception as e:
            print("Failed to connect to any known network!")
            #wlan.deinit()
                #wlan.init(mode=WLAN.AP, ssid=original_ssid, auth=original_auth, channel=6, antenna=WLAN.INT_ANT)
    except Exception as e:
        print("WiFi connect try failure! ...")
        #wlan.disconnect()

def disconnect(net):
    if net=="WiFi":
        wlan.disconnect()
        print("disconnect wifi")
        time.sleep(1)
    elif net=="LTE":
        lte.disconnect()
        print("disconnect lte")
        time.sleep(1)




def lteconnect():
    #lte = LTE()
    #lte.attach( band=13,apn="iot.truphone.com",cid=3,type=LTE.IPV4V6)
    #lte.attach( band=3, apn="iot.truphone.com")
    lte.attach( apn="iot.truphone.com")
    print("LTE: attaching..",end='')
    while not lte.isattached():
        time.sleep(0.25)
        print('.',end='')
        print(lte.send_at_cmd('AT!="fsm"'))         # get the System FSM
        #print("band 13")
    print("attached!")
    print("LTE: connecting...",end='')
    #lte.init()
    lte.connect()
    #print("connecting [##",end='')
    while not lte.isconnected():
        time.sleep(0.25)
        #print('#',end='')
        #print(lte.send_at_cmd('AT!="showphy"'))
        #print(lte.send_at_cmd('AT!="fsm"'))
    #print("] connected!")
    print("connected!")
    print("reconnect pybytes by LTE...")
    pybytes.connect_lte()
    #WLAN.deinit()
    #print(socket.getaddrinfo('pycom.io', 80))

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
