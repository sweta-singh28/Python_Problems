# Function to print first N prime numbers
def print_primes_till_N(N):
    # Declare the variables
    flag = 0

    # Print display message
    print("Prime numbers between 1 and", N, "are:")

    # Traverse each number from 1 to N
    # with the help of for loop
    for i in range(2, N + 1):
        # flag variable to tell
        # if i is prime or not
        flag = 1
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                flag = 0
                break
        # flag = 1 means i is prime
        # and flag = 0 means i is not prime
        if flag == 1:
            print(i, end=" ")

# Driver code
N = 100
print_primes_till_N(N)
