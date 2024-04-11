def CalcBMI(H,W):
    print(W/H)
    if W/H < 18.5:
        print("Underweight!")
    elif W/H>=18.5 and W/H<25:
        print("Normal Weight!")    
    elif W/H>25 and W/H<30:
        print("Over Weight") 
    else:
        print("Obese")       
        
   
   
   
H = int(input("Enter your height (in meters): "))
W = int(input("Enter your weight (in kgs): "))    

CalcBMI(H, W)