from datetime import datetime

class logger:
    
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    logFile = open("logs.txt",'a')
    def __init__(self):
        self.logFile.write("["+self.dt_string+"] - *** Boot Time  ***\n")
        self.logFile.close()
    
    def openAndWrite(self, text):
        self.now = datetime.now()
        self.dt_string = self.now.strftime("%d/%m/%Y %H:%M:%S")
        self.logFile = open('logs.txt','a')
        self.logFile.write("["+self.dt_string + "] - "+text+"\n")
        self.logFile.close()
        
    
    def action(self, text):
        self.openAndWrite("Action: "+text)
        
    def error(self, text):
        self.openAndWrite("Error: "+text)