ct=0
max=0
while 1:
    n = float(input("Enter a Value (zero to quit):"))  
    if n ==0:
        print("Maximum: ",max)
        break
    else:
        ct +=1
        
        if n > max:
            max = n