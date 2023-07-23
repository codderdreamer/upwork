from Modules.WebsocketModule import *
from Modules.FlaskModule import *
import time
import subprocess

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

        # wifi = subprocess.check_output(['netsh', 'WLAN', 'show', 'interfaces'])
        # data = wifi.decode('utf-8')
        # print(data)

        # using the check_output() for having the network term retrieval
        
        devices = subprocess.check_output(['netsh','wlan','show','network'])
        
        # decode it to strings
        devices = devices.decode('utf-8')
        devices= devices.replace("\r","")
        
        # displaying the information
        print(devices)
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

        print(self.wifi_devices)

        subprocess_result = subprocess.Popen('iwgetid',shell=True,stdout=subprocess.PIPE)
        subprocess_output = subprocess_result.communicate()[0],subprocess_result.returncode
        network_name = subprocess_output[0].decode('utf-8')
        if network_name == "":
            print("wifi bağlı değil")
        else:
            print(network_name)

       


Application()
while True:
    time.sleep(10)
    if BootError:
        print("BootError")
        time.sleep(10)
        break