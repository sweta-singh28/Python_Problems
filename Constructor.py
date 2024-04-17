

class Car:
    wheel = "four"       #it only stores for omce in memeory    Class attr
    name = "sweta"              #class attr
    def __init__(self,name,color,price):
        self.name = name            #obj attr>class attr
        self.color = color
        self.price = price
        print("Adding a new car in database")
        
        
c1 = Car("BMW","red",27)      
print(c1.name, c1.color,c1.price)  
print(c1.wheel)

c2 = Car("Mercedes","black",49)
print(c2.name,c2.color,c2.price)
