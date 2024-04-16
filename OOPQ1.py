

class Student:
    def __init__(self, name, marks):
        self.name  = name
        self.marks = marks
        
 
    @staticmethod
    def Hello():
        print("Hello Sweta")    
           
           
           
    def getAvg(self):
        sum = 0
        for i in self.marks:
            sum+=i
        print("hi",self.name,"your average score is: ", sum/3)    
        
        
        
        
        
S1 = Student("sweta singh", [89,94,96])    
S1.getAvg()

S1.name = "Gungun Singh"
S1.getAvg()
  
        
        
        
