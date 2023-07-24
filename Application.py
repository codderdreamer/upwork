from Modules.WebsocketModule import *
from Modules.FlaskModule import *
import time
import subprocess
import keyboard
import os

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

        self.network_ssid = {}






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
                if (not (ssid in self.network_ssid.values())) and (not ssid == ""):
                    self.network_ssid[i] = ssid
                    i+=1

        print("result: ", self.network_ssid)

        self.websocket_module.send_message_to_all("networks",self.network_ssid)



            
        

       



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


Application()
while True:
    time.sleep(10)
    if BootError:
        print("BootError")
        time.sleep(10)
        break