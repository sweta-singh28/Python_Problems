count = 1 
while count <= 3:
 P = input("Enter the password: ")
 if P == "password123":
    print("Acess Granted!") 
    break
 else:
    print("Incorrect password. Try again.")
    count += 1
if count == 3:
    print("Acess denied. Too many attempts")
