#Sum of two numbers 



#function defination
def CalcSum(a,b):         #a,b = passing the parameter
    sum = a+b 
    print(sum)
    return sum


    
 #Function call 
CalcSum(2, 3)           #2,3 = Passing the arguments
#CalcSum(5, 10)
#print("Function calling")


def Sum(a,b):
    return a+b

finalAns = Sum(7, 7)
print(finalAns)

def PrintHello():
    print("Hello")
    
PrintHello()    
PrintHello()  

output = PrintHello()      #o/p = none, cause this function doesnot returns any value
print(output)
 
 