num = int(input("Enter number: "))
count = 0
i = 1
while(i<=num):
    if(num%i==0):
        count+=1
    i = i+1    
    
if(count == 2):
    print("Prime number.")
else:
    print("Not a prime number")
