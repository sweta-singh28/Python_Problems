a = int(input("Enter a number: "))
operator = input("Choose an oprator(+,-,*,/): ")
b = int(input("Enter the second number: "))
if(operator == '+'):
    print("Addititon: ", a + b)
elif(operator == '-'):
    print("Substraction: ", a - b) 
elif(operator == '*'):
    print("Multiplication: ", a * b)
else:
    print("Division: ", a / b)
    
        