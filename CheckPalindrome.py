#WAP to check palindrome
num = int(input("Enter the number: "))
rev = 0
x = num
while(num>0):
    rev = (rev*10) + num % 10
    num//=10
    
if(rev == x):
    print("palindrome")
else:
    print("Not a palindrome")
    
