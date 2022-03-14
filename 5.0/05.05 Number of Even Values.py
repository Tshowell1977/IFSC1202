ct=0
max=0
while 1:
    n = float(input("Enter a Value (zero to quit):"))  
    if n == 0:
        print("Number of Even Values: ",ct)
        break
    else:
                
        if n%2 == 0:
            ct=ct+1
            