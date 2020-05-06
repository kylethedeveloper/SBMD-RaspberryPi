#red 8 green 10 blue 12 anot 5v
#GPIO.output(red,GPIO.HIGH)
from time import sleep
import RPi.GPIO as GPIO
class led:
    redPin = 8
    greenPin = 10
    bluePin = 12
    ledCurrentColor = "None"
    
    def __init__(self):
        
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        self.turnOff()
        
    def currentColor(self):
        return self.ledCurrentColor
    
    def turnOff(self):
        self.ledCurrentColor = "None"
        GPIO.setup(self.redPin,GPIO.OUT,initial=GPIO.HIGH)
        GPIO.setup(self.greenPin,GPIO.OUT,initial=GPIO.HIGH)
        GPIO.setup(self.bluePin,GPIO.OUT,initial=GPIO.HIGH)
        
    def red(self):
        self.turnOff()
        GPIO.output(self.redPin,GPIO.LOW)
        self.ledCurrentColor = "red"
    
    def blue(self):
        self.turnOff()
        GPIO.output(self.bluePin,GPIO.LOW)
        self.ledCurrentColor = "blue"
    
    def green(self):
        self.turnOff()
        GPIO.output(self.greenPin,GPIO.LOW)
        self.ledCurrentColor = "green"
        
    def magenta(self):
        self.turnOff()
        GPIO.output(self.bluePin,GPIO.LOW)
        GPIO.output(self.redPin,GPIO.LOW)
        self.ledCurrentColor = "magenta"
    
    def cyan(self):
        self.turnOff()
        GPIO.output(self.greenPin,GPIO.LOW)
        GPIO.output(self.bluePin,GPIO.LOW)
        self.ledCurrentColor = "cyan"
    
    def yellow(self):
        self.turnOff()
        GPIO.output(self.greenPin,GPIO.LOW)
        GPIO.output(self.redPin,GPIO.LOW)
        self.ledCurrentColor = "yellow"
        
    def white(self):
        self.turnOff()
        GPIO.setup(self.redPin,GPIO.OUT,initial=GPIO.LOW)
        GPIO.setup(self.greenPin,GPIO.OUT,initial=GPIO.LOW)
        GPIO.setup(self.bluePin,GPIO.OUT,initial=GPIO.LOW)
        self.ledCurrentColor = "white"
        
    def checkLed(self):
        self.red()
        sleep(0.2)
        self.green()
        sleep(0.2)
        self.blue()
        sleep(0.2)
        self.cyan()
        sleep(0.2)
        self.magenta()
        sleep(0.2)
        self.yellow
        sleep(0.2)
        self.white()
        sleep(0.2)
        self.turnOff()
    