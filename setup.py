from qrReader import qrReader
from wifi import wifi
from statusled import led
from time import sleep

led = led()
qr = qrReader()
wifi = wifi()

led.red()
if(wifi.isInternetOn()):
	led.green()
ssid, password = qr.read()
led.yellow()
wifi.setWifi(ssid,password)

while(not wifi.isInternetOn()):
	sleep(1)
led.green()


"""
ssid=<SSID>
psk=<passphrase>
"""
