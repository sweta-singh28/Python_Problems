# print 1 
#       2  3 
#       4  5  6 
#       7  8  9  10
#       11 12 13 14  15

num = 1
for i in range(0, 5, 1):
    for j in range(0, i+1, 1):
        print(num, end = ' ')
        num+=1
    print(" ")    