i = 0
str = "Javapoint"
while i < len(str):
    if str[i] == 'v' or str[i] == 'i':
        i+=1
        continue
    print("The curreant letter is: ", str[i])
    i+=1
