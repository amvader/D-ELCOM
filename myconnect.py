import os
import machine
import pycom

def wifi(pybytes):
    uart = machine.UART(0, 115200)
    os.dupterm(uart)

    known_nets = {
        'AMEL': {'pwd': 'b00b121374'},
        'AmelSWS': {'pwd': 'nancy3stl4'},
        'Amvader1': {'pwd': '4053085956'},
        'Amvader2': {'pwd': '4053085956'},
        'NETGEAR25': {'pwd': 'littleshoe029'},
        'SWS': {'pwd': 'ok321321'}}


    if machine.reset_cause() != machine.SOFT_RESET:
        from network import WLAN
        wlan = WLAN()
        wlan.mode(WLAN.STA)
        original_ssid = wlan.ssid()
        original_auth = wlan.auth()

        print("Scanning for known wifi nets")
        available_nets = wlan.scan()
        nets = frozenset([e.ssid for e in available_nets])

        known_nets_names = frozenset([key for key in known_nets])
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

        except Exception as e:
            print("Failed to connect to any known network, going into AP mode")
            wlan.init(mode=WLAN.AP, ssid=original_ssid, auth=original_auth, channel=6, antenna=WLAN.INT_ANT)

    pybytes.reconnect()
