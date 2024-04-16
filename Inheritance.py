

class Car:
    @staticmethod
    def start():
        print("Car started")
        
    @staticmethod
    def stop():
        print("Car stopped")    
        
   
class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name  
        
        
car1 = ToyotaCar("Fotuner")
car2 = ToyotaCar("Pirus") 

print(car1.name)  
print(car2.name)    

print(car1.start()) 
print(car1.stop()) 
     