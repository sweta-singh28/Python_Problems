total = 0

while True:
    num = int(input("Enter a number: "))
    if num == -1:
        break
    else:
        total += num
        
print("The total sum is ", total)        