from Modules.WebsocketModule import *
from Modules.FlaskModule import *
import time
import subprocess
import keyboard
import os
from Utils import *

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

        # scan_network(self)
        turn_on_network()
        threading.Thread(target=scan_network, args=(self,), daemon=True).start()

        threading.Thread(target=self.key_control, daemon=True).start()

        # os.system("startx -- -nocursor")




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

    def key_control(self):
        time_start = time.time()
        time_finish = time.time()
        keyboard.add_hotkey('ctrl+shift+1', print('ctrl+shift+1**'))
        keyboard.add_hotkey('ctrl+shift+2', print('ctrl+shift+2**'))
        keyboard.add_hotkey('ctrl+shift+3', print('ctrl+shift+3**'))
        keyboard.add_hotkey('ctrl+shift+4', print('ctrl+shift+4**'))
        keyboard.add_hotkey('ctrl+shift+5', print('ctrl+shift+5**'))

        while True:  # Loop to capture keys continuously
            try:
                time_start = time.time()
                #event = keyboard.read_event()  # Capture a keyboard event
                event = keyboard.read_key(suppress=False)
                print("event:",event)
                # print("event capitalize:",event.capitalize())
                # print("event casefold:",event.casefold())
                # #print("event center:",event.center())
                # #print("event count:",event.count())
                # print("event encode:",event.encode())
                #  #print("event endswith:",event.endswith())
                # print("event expandtabs:",event.expandtabs())
                #  #print("event find:",event.find())
                #  #print("event format:",event.format())
                #  #print("event format_map:",event.format_map())
                #  #print("event index:",event.index())
                # print("event isalnum:",event.isalnum())
                # print("scan_code:",event.scan_code)
                # # print(f"{event.name} key was pressed")
                # # print(time_start-time_finish)
                # time_finish = time.time()

                # if event.name == 'q' and event.event_type == 'down':
                #     print("Q key was pressed.")
                #     break
                # elif event.event_type == 'down':
                #     print(f"{event.name} key was pressed********************")
                #     self.websocket_module.send_message_to_all(event.name)

                   

            
            
            except Exception as e:
                print(e)


Application()
while True:
    time.sleep(10)
    if BootError:
        print("BootError")
        time.sleep(10)
        break