def SumOfFactorials(n):
    fact = 1
    sum = 0
    for i in range(1,n+1,1):
        fact *= i
        sum += fact  
    print("Sum is: ", sum)



n = int(input("Enter the number: "))
SumOfFactorials(n)