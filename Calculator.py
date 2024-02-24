a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("Select operation: ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

c = input("Enter the operation: ")

if c == '1':
    print("Result: ", a + b)
elif c == '2':
    print("Result: ", a - b)
elif c == '3':
    print("Result: ", a * b)
elif c == '4':
    if b == 0:
        print("Cannot divide by zero!")
    else:
        print("Result: ", a / b)
else:
    print("Invalid operation selected.")
