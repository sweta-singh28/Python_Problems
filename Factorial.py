#Calculate the factorial of a given number
def Factorial(num):
     fact = 1
     i = 1
     
     while i<=num:
        fact *= i
        i += 1
     print("The factorial is: ", fact)
        
        
num = int(input("Enter the number: "))        
        
Factorial(num)        
        