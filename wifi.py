import os
import urllib.request
import statusled
import logger
import asyncio

class wifi:
    
    #log = logger.logger()
    wifiConf = """ctrl_interface=/run/wpa_supplicant GROUP=netdev
update_config=1
country=TR

network={
	ssid="wifiname"
	psk="password"
}
"""
    
    def __init__(self):
        pass

    def isInternetOn(self):
        print('isInternetOn')
        try:
            urllib.request.urlopen('http://172.217.12.174', timeout=0.5)
            print('true')
            return True
        except urllib.request.URLError as err: 
            print('false')
            return False
            
    def setWifi(self,ssid,psk):
        print('works')
        self.wifiConf = self.wifiConf.replace('wifiname',ssid)
        self.wifiConf = self.wifiConf.replace('password',psk)
        currDir = os.getcwd()
        os.chdir('/etc/wpa_supplicant')
        wifiFile = open("wpa_supplicant.conf","w")
        wifiFile.write(self.wifiConf)
        wifiFile.close()
        stream = os.popen("sudo ifdown wlan0 ; sudo ifdown wlan0")
        output = stream.read()
        print(output)
        #log.action(output)
        #os.chdir(currDir)
        #sudo wpa_cli -i wlan0 reconfigure
        #sudo systemctl restart dhcpcd

        return True
        
