from Modules.WebsocketModule import *
from Modules.FlaskModule import *
import time
import subprocess
import keyboard

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

        # using the check_output() for having the network term retrieval
        try:
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
        try:

            while True:  # Loop to capture keys continuously
                event = keyboard.read_event()  # Capture a keyboard event

                if event.name == 'q' and event.event_type == 'down':
                    print("Q key was pressed.")
                    break
                elif event.event_type == 'down':
                    print(f"{event.name} key was pressed")
        except Exception as e:
            print(e)

       


Application()
while True:
    time.sleep(10)
    if BootError:
        print("BootError")
        time.sleep(10)
        break