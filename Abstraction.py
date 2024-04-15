class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
        
        
    def Start(self):
        self.acc = True
        self.brk = True
        self.clutch = True 
        print("CAR STARTED....")
        
        
            
Car1 = Car()
Car1.Start()          