num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative number.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    factorial = 1
    i = 1
    while(i <= num):
        factorial *= i
        i += 1
        print("The factorial of the given number is:   ", factorial)