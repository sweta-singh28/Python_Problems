#print the sum of all even numbers from 1 to 100
sum = 0
for i in range (1, 100):
    if (i % 2 == 0):
        sum += i
        print("Sum of all even numbers: ", sum)