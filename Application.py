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

        os.system('pwd')
        os.system('touch network.txt')
        os.system("nmcli dev wifi > network.txt")

        file = open("home/pi/upwork/network.txt",'r')
        lines = file.readlines()
        i=0
        network = []
        for line in lines:
            a = line.split("\t")
            print(a)
        

       



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