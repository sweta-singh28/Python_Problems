count = 0
while count<=3:
    p = input("Enter password: ")
    if p == "Python123":
        print("Access granted!")
        break
    else:
        print("Incorrect password!")
        count +=1 
        
    if count == 3:
        print("Too many attempts. Access denied!")    
        