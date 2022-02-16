ct=0
max=0
eqmax=0
while 1:
    n = float(input("Enter a Value (zero to quit):"))  
    if n ==0:
        print("Maximum: ",max)
        print("number of occurences: ",eqmax)
        break
    else:
        ct +=1
        
        if n > max:
            
                max=n
        
