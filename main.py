import asyncio
import statusled
import logger
from time import sleep
import wifi
import sensor

log = logger.logger()
led = statusled.led()
wifi = wifi.wifi()


#log.action("work")
led.checkLed()
#import setup
#wifi.isInternetOn()

#wifi.setWifi('<ssid>','<passphrase>')

#wifi.isInternetOn()






