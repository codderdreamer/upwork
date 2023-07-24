from Modules.WebsocketModule import *
from Modules.FlaskModule import *
import time
import subprocess
import keyboard
import os


from scapy.all import *
from threading import Thread
import pandas
import time
import os

# initialize the networks dataframe that will contain all access points nearby
networks = pandas.DataFrame(columns=["BSSID", "SSID", "dBm_Signal", "Channel", "Crypto"])
# set the index BSSID (MAC address of the AP)
networks.set_index("BSSID", inplace=True)

def callback(packet):
    if packet.haslayer(Dot11Beacon):
        # extract the MAC address of the network
        bssid = packet[Dot11].addr2
        # get the name of it
        ssid = packet[Dot11Elt].info.decode()
        try:
            dbm_signal = packet.dBm_AntSignal
        except:
            dbm_signal = "N/A"
        # extract network stats
        stats = packet[Dot11Beacon].network_stats()
        # get the channel of the AP
        channel = stats.get("channel")
        # get the crypto
        crypto = stats.get("crypto")
        networks.loc[bssid] = (ssid, dbm_signal, channel, crypto)


def print_all():
    while True:
        os.system("clear")
        print(networks)
        time.sleep(0.5)


def change_channel():
    ch = 1
    while True:
        os.system(f"iwconfig {interface} channel {ch}")
        # switch channel from 1 to 14 each 0.5s
        ch = ch % 14 + 1
        time.sleep(0.5)

BootError=False

class Application():
    def __init__(self):
        self.wifi_devices = []

        # Websocketi Başlat
        self.websocket_module = WebsocketModule(self)
        self.websocket_module.run()

        # Flaskı Başlat
        self.flask_module = FlaskModule(__name__)
        self.flask_module.run(BootError)

        # # scanning the available Wi-Fi networks  
        # os.system('cmd /c "netsh wlan show networks"')  
        # # providing the Wi-Fi name as input  
        # router_name = input('Input Name/SSID of the Wi-Fi network we would like to connect: ')  
        # # connecting to the provided Wi-Fi network  
        # os.system(f'''cmd /c "netsh wlan connect name = {router_name}"''')  
        # print("If the system is not connected yet, try reconnecting to an earlier connected SSID!")  

        # using the check_output() for having the network term retrieval
        try:
            # devices = subprocess.check_output(['netsh','wlan','show','network'])
            devices = subprocess.check_output(['netsh','wlan','show','network'])
            
            # decode it to strings
            devices = devices.decode('utf-8')
            devices= devices.replace("\r","")
            
            # displaying the information
            print("devices",devices)
            time.sleep(1)

            devices = devices.split('SSID')
            counter = 0
            for device in devices:
                if devices[0] == device:
                    pass
                else:
                    i = str(counter) + " : "
                    device_name = device.split(i)[1].split('\n')[0]
                    self.wifi_devices.append(device_name)
                counter+=1

            print("self.wifi_devices",self.wifi_devices)

            subprocess_result = subprocess.Popen('iwgetid',shell=True,stdout=subprocess.PIPE)
            subprocess_output = subprocess_result.communicate()[0],subprocess_result.returncode
            network_name = subprocess_output[0].decode('utf-8')
            print(network_name)
            if network_name == "":
                print("wifi bağlı değil")
            else:
                print(network_name)
        except Exception as e:
            print(e)



        # keyboard girişlerini alıyor kumanda gelince bakılacak.
        # try:

        #     while True:  # Loop to capture keys continuously
        #         event = keyboard.read_event()  # Capture a keyboard event

        #         if event.name == 'q' and event.event_type == 'down':
        #             print("Q key was pressed.")
        #             break
        #         elif event.event_type == 'down':
        #             print(f"{event.name} key was pressed")
        # except Exception as e:
        #     print(e)

        # interface name, check using iwconfig
        interface = "wlan0mon"
        # start the thread that prints all the networks
        printer = Thread(target=print_all)
        printer.daemon = True
        printer.start()
        # start the channel changer
        channel_changer = Thread(target=change_channel)
        channel_changer.daemon = True
        channel_changer.start()
        # start sniffing
        sniff(prn=callback, iface=interface)

       


Application()
while True:
    time.sleep(10)
    if BootError:
        print("BootError")
        time.sleep(10)
        break