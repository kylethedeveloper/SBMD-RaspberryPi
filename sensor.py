import os
from time import sleep
import Adafruit_DHT
#import RPi.GPIO as GPIO
class sensor:
    
    temperature = 0.0
    humidity = 0.0
    cpuTemp = 0.0
    DHT_SENSOR = Adafruit_DHT.DHT22
    DHT_PIN = 4
    
    def __init__(self):
        pass

    def updateSensors(self):
        #read CPU temp
        stream = os.popen("vcgencmd measure_temp | egrep -o '[0-9]*\.[0-9]*'") #linux command for getting rpi cpu temperature
        self.cpuTemp= float(stream.read())

        #read temperature and humidity
        while True:
            humidity, temperature = Adafruit_DHT.read_retry(self.DHT_SENSOR, self.DHT_PIN)
            if humidity is not None and temperature is not None:
                self.humidity = round(humidity,2)
                self.temperature = round(temperature,2)
                #print(str(self.temperature)+'*C '+str(self.humidity)+'%') #for debug
                break
            else:
                print("Failed to retrieve data from humidity sensor")

    def cpuTemperature(self):
        self.updateSensors()
        return self.cpuTemp

    def temperatureAndHumidity(self):
        if self.humidity == 0 and self.temperature == 0:
            self.updateSensors()
            return self.temperature, self.humidity
        return self.temperature, self.humidity

"""
sensor = sensor()
print(sensor.cpuTemperature())
print(sensor.temperatureAndHumidity())

"""
