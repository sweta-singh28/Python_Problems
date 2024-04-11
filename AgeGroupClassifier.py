def AgeClassify(age):
    if age <= 0 or age <= 12:
        print("Child")
    elif age <= 19:
        print("Teenage")
    elif age <= 59:
        print("Adult")
    else:
        print("Senior")

age = int(input("Enter your age: "))
AgeClassify(age)
