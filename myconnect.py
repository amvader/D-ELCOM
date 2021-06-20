import os
import machine
import pycom
from network import LTE
import time
import socket

def wifi(pybytes,wlan):
    #uart = machine.UART(0, 115200)
    #os.dupterm(uart)

    known_nets = {
        'AMEL': {'pwd': 'b00b121374'},
        'AmelSWS': {'pwd': 'xnancy3stl4'},
        'Amvader1': {'pwd': 'x4053085956'},
        'Amvader2': {'pwd': 'x4053085956'},
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
        print("Failed to scan available nets")

    try:
        nets = frozenset([e.ssid for e in available_nets])
    except Exception as e:
        print("Failed to scan frozen nets")
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
            #print("reconnect pybytes...")
            #pybytes.connect()

        except Exception as e:
            print("Failed to connect to any known network!")
            wlan.deinit()
                #wlan.init(mode=WLAN.AP, ssid=original_ssid, auth=original_auth, channel=6, antenna=WLAN.INT_ANT)
    except Exception as e:
        print("WiFi connect try failure! ...")
        wlan.deinit()




def lte(pybytes,lte):
    #lte = LTE()
    #lte.attach( band=13,apn="iot.truphone.com",cid=3,type=LTE.IPV4V6)
<<<<<<< HEAD
    lte.attach( band=3, apn="iot.truphone.com")
    #lte.attach( apn="iot.truphone.com",band=13,  cid=3, type=LTE.IP, legacyattach=True)
=======
    #lte.attach( band=3, apn="iot.truphone.com")
    lte.attach( apn="iot.truphone.com",band=13,  cid=3, type=LTE.IP, legacyattach=True)
>>>>>>> 8b84d2e25a6b5337ee37c6e9c67ec1047b509be0
    print("LTE: attaching..",end='')
    while not lte.isattached():
        time.sleep(0.25)
        print('.',end='')
        print(lte.send_at_cmd('AT!="fsm"'))         # get the System FSM
        #print("band 13")
    print("attached!")
    print("LTE: connecting...",end='')
    lte.connect(cid=3)
    #print("connecting [##",end='')
    while not lte.isconnected():
        time.sleep(0.25)
        #print('#',end='')
        #print(lte.send_at_cmd('AT!="showphy"'))
        print(lte.send_at_cmd('AT!="fsm"'))
    #print("] connected!")
    print("connected!")
    #WLAN.deinit()
    #print(socket.getaddrinfo('pycom.io', 80))
    #print("reconnect pybytes...")
    #pybytes.connect()
