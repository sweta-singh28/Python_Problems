#Check Armstrong (three numbers)
num = int(input("Enter number: "))
x = num
sum = 0
while(num>0):
    sum += (num%10)*(num%10)*(num%10)
    num //= 10
    
if(x==sum):
    print("Armstrong number")
else:
    print("Not an armstrong")
    

    
