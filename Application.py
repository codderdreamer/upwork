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

        # Network'ü aktif et ilk başta aktif olmuyor
        os.system('sudo systemctl restart NetworkManager')

        # İnternet bağlımı diye sorgula
        os.system('touch network_status.txt')
        os.system('nmcli dev status > network_status.txt')
        file = open("network_status.txt",'r')
        lines = file.readlines()
        for line in lines:
            if "eth0" in line:
                print("eth0:",line)
            elif "wlan0" in lines:
                print("wlan0",line)
                


















        # self.network_ssid = {}

        # # scan_network(self)
        # turn_on_network()
        # threading.Thread(target=scan_network, args=(self,), daemon=True).start()

        # threading.Thread(target=self.key_control, daemon=True).start()

        # os.system("startx -- -nocursor")

        # self.key_down_press = 0
        # self.counter = 0


    def key_counter(self):
        if self.key_down_press==0:
            self.counter += 1
            if self.counter == 1:
                return True
        else:
            self.counter = 0
        return False



    def key1(self):
        if self.key_counter():
            print('************************* ctrl+shift+1 ')
            self.websocket_module.send_message_to_all("ctrl+shift+1")

    def key2(self):
        if self.key_counter():
            print('************************* ctrl+shift+2')
            self.websocket_module.send_message_to_all("ctrl+shift+2")

    def key3(self):
        if self.key_counter():
            print('************************* ctrl+shift+3')
            self.websocket_module.send_message_to_all("ctrl+shift+3")

    def key4(self):
        if self.key_counter():
            print('************************* ctrl+shift+4')
            self.websocket_module.send_message_to_all("ctrl+shift+4")

    def key5(self):
        if self.key_counter():
            print('************************* ctrl+shift+5')
            self.websocket_module.send_message_to_all("ctrl+shift+5")

    def key6(self):
        if self.key_counter():
            print('************************* ctrl+shift+6')
            self.websocket_module.send_message_to_all("ctrl+shift+6")

    def key7(self):
        if self.key_counter():
            print('************************* ctrl+shift+7')
            self.websocket_module.send_message_to_all("ctrl+shift+7")

    def key_up(self):
        if self.key_counter():
            print('************************* up')
            self.websocket_module.send_message_to_all("up")

    def key_down(self):
        if self.key_counter():
            print('************************* down')
            self.websocket_module.send_message_to_all("down")

    def key_left(self):
        if self.key_counter():
            print('************************* left')
            self.websocket_module.send_message_to_all("left")

    def key_right(self):
        if self.key_counter():
            print('************************* right')
            self.websocket_module.send_message_to_all("right")

    def key_enter(self):
        if self.key_counter():
            print('************************* enter')
            self.websocket_module.send_message_to_all("enter")

    def key_control(self):
        keyboard.add_hotkey('ctrl+shift+1', self.key1)
        keyboard.add_hotkey('ctrl+shift+2', self.key2)
        keyboard.add_hotkey('ctrl+shift+3', self.key3)
        keyboard.add_hotkey('ctrl+shift+4', self.key4)
        keyboard.add_hotkey('ctrl+shift+5', self.key5)
        keyboard.add_hotkey('ctrl+shift+6', self.key6)
        keyboard.add_hotkey('ctrl+shift+7', self.key7)
        keyboard.add_hotkey('up',self.key_up)
        keyboard.add_hotkey('down',self.key_down)
        keyboard.add_hotkey('right',self.key_right)
        keyboard.add_hotkey('left',self.key_left)
        keyboard.add_hotkey('enter',self.key_enter)

        while True:  # Loop to capture keys continuously
            try:
                event = keyboard.read_event()
                if event.event_type == keyboard.KEY_DOWN:
                    self.key_down_press += 1
                if event.event_type == keyboard.KEY_UP:
                    self.key_down_press = 0
                    self.counter = 0

            except Exception as e:
                print(e)


Application()
while True:
    time.sleep(10)
    if BootError:
        print("BootError")
        time.sleep(10)
        break







#event = keyboard.read_event()  # Capture a keyboard event

# if event.name == 'q' and event.event_type == 'down':
#     print("Q key was pressed.")
#     break
# elif event.event_type == 'down':
#     print(f"{event.name} key was pressed********************")
#     self.websocket_module.send_message_to_all(event.name)