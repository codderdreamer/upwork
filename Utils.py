
import os
import time

def get_wifi_list():
    print("get_wifi_list")
    os.system('pwd')
    os.system('touch network.txt')
    os.system("nmcli dev wifi > network.txt")

def turn_on_network():
    try:
        os.system('sudo systemctl restart NetworkManager')
        os.system('nmcli r wifi on')
        time.sleep(7)
    except Exception as e:
        print(e)


def scan_network(application):
    try:
        os.system('pwd')
        os.system('touch network.txt')
        os.system("nmcli dev wifi > network.txt")

        file = open("network.txt",'r')
        lines = file.readlines()
        i=0
        ssid = None
        for line in lines:
            line = line.split("        ")[1].split(" ")
            if len(line) > 2:
                ssid = line[2]
                if (not (ssid in application.network_ssid.values())) and (not ssid == ""):
                    application.network_ssid[i] = ssid
                    i+=1

        print("result: ", application.network_ssid)

        application.websocket_module.send_message_to_all("networks",application.network_ssid)
    except Exception as e:
        print(e)