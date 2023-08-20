
import os
import time
import json

def open_web_browser():
    time.sleep(10)
    os.system("startx -- -nocursor")

def scan_network(application):
    while application.wifi_selector:
        # wifi.json dosyasını al
        try:
            with open("wifi.json", "r") as jsonfile:
                data = json.load(jsonfile)
                print(data)
        except Exception as e:
            print("wifi.json dosyası açılamadı",e)

        # wifi dosyasında kayıtları tara, öncelikli olana bağlan
        for data_key, wifi in data.items():
            print("wifi", wifi )
            if application.wifi_connected == False:
                print(wifi["ssid"])
                print(wifi["password"])
                print(wifi["priority"])
                # bağlanmayı dene
                if wifi["priority"] == "1":
                    print('sudo nmcli dev wifi connect ' + wifi["ssid"] + ' password "' + wifi["password"] + '"')
                    os.system('sudo nmcli dev wifi connect ' + wifi["ssid"] + ' password "' + wifi["password"] + '"')

        # Bağlandı mı kontrol et
        os.system('touch network_status.txt')
        os.system('nmcli dev status > network_status.txt')
        file = open("network_status.txt",'r')
        lines = file.readlines()
        for line in lines:
            print(line)
            if (" connected" in line) and (application.wifi_connected == False):
                    wifiSplit = line.split(" ")
                    application.wifi_name = wifiSplit[len(wifiSplit)-2]
                    print("Wifi connected.", application.wifi_name)
                    application.wifi_connected = True

        # Bağlandıysa sayfayı aç
        if application.wifi_connected:
            print("https://momentum.visi.help/ sayfasına git")
            application.wifi_selector = False
            application.websocket_module.send_message_to_all("VisihelpPage")
        # Bağlanmadıysa wifi dosyasını tara hepsini dene
        else:
            for data_key, wifi in data.items():
                print("wifi", wifi )
                if application.wifi_connected == False:
                    print(wifi["ssid"])
                    print(wifi["password"])
                    print(wifi["priority"])
                    # bağlanmayı dene
                    print('sudo nmcli dev wifi connect ' + wifi["ssid"] + ' password "' + wifi["password"] + '"')
                    os.system('sudo nmcli dev wifi connect ' + wifi["ssid"] + ' password "' + wifi["password"] + '"')

                    # Bağlandı mı kontrol et
                    os.system('touch network_status.txt')
                    os.system('nmcli dev status > network_status.txt')
                    file = open("network_status.txt",'r')
                    lines = file.readlines()
                    for line in lines:
                        print(line)
                        if (" connected" in line) and (application.wifi_connected == False):
                            wifiSplit = line.split(" ")
                            application.wifi_name = wifiSplit[len(wifiSplit)-2]
                            print("Wifi connected.", application.wifi_name)
                            application.wifi_connected = True
                            print("https://momentum.visi.help/ sayfasına git")
                            application.wifi_selector = False
                            application.websocket_module.send_message_to_all("VisihelpPage")


        time.sleep(3)
        # Önceden kaydedilmişlere bağlanamdıysa, wifi seçici sayfasını getir
        print("self.wifi_connected",application.wifi_connected)

        if application.wifi_connected == False:
            # Hangi wifiler mevcut?
            os.system('touch network.txt')
            os.system('nmcli dev wifi > network.txt')
            time.sleep(3)
            file = open("network.txt",'r')
            lines = file.readlines()
            application.wifi_list = {}
            for line in lines:
                if "IN-USE" in line:
                    pass
                else:
                    line = line.split(" ")
                    wifi = []
                    wifi_name = ""
                    for word in line:
                        if word != "":
                            wifi.append(word)
                    for word in wifi:
                        if ":" in word:
                            pass
                        else:
                            if "Infra" == word:
                                break
                            wifi_name = wifi_name + word + " "

                    for word in wifi:
                        if "*" in word:
                            wifi_bar = word

                    application.wifi_list[wifi_name] = wifi_bar

            print(application.wifi_list)
            print("Wifi selector sayfasına git")

            application.websocket_module.send_message_to_all("WifiPage",application.wifi_list)


















def get_wifi_listxxxxx():
    print("get_wifi_list")
    os.system('pwd')
    os.system('touch network.txt')
    os.system("nmcli dev wifi > network.txt")

def turn_on_networkxxxx():
    try:
        os.system('sudo systemctl restart NetworkManager')
        os.system('nmcli r wifi on')
        time.sleep(7)
    except Exception as e:
        print(e)


def scan_networkxxx(application):
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