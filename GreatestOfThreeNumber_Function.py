def FindGreatest(num1, num2, num3):
    if num1>num2 and num1>num3:
        print("Greatest: ",num1)
    elif num2>num1 and num2>num3:
        print("Greatest: ",num2) 
    else:
        print("Greatest: ",num3)      
        
        
num1 = int(input("Enter the first number: "))    
num2 = int(input("Enter the second number: ")) 
num3 = int(input("Enter the 3rd number: "))  

     
FindGreatest(num1, num2, num3)         