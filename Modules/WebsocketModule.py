import websocket_server
import json
import threading
from Utils import *

class WebsocketModule():
    def __init__(self,application):
        self.application = application
        self.websocket = websocket_server.WebsocketServer('0.0.0.0', 9000 )

    def run(self):
        self.websocket.set_fn_new_client(self.NewClientws)
        self.websocket.set_fn_client_left(self.ClientLeftws)
        self.websocket.set_fn_message_received(self.MessageReceivedws)
        threading.Thread(target=self.websocket.run_forever,daemon=True).start()
        print("Websocket Started.")

    def NewClientws(self,client, server):
        print("New client connected and was given id %d" % client['id'], client["address"])
        scan_network(self.application)
        # if len(self.application.network_ssid)>0:
        #     self.send_message_to_all("networks",self.application.network_ssid)


    def send_message_to_all(self, command = None, data = None):
        DataToSend = {"Command": command, "Data": data}
        self.websocket.send_message_to_all(json.dumps(DataToSend))

    def ClientLeftws(self,client, server):
        print("Client(%d) disconnected" % client['id'])

    def MessageReceivedws(self, client, server, message):
        IncomingData = json.loads(message)
        print(IncomingData)