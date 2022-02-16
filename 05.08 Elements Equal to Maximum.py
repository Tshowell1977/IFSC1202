ct=1
max=0
while 1:
    n = float(input("Enter a Value (zero to quit):"))  
    if n ==0:
        print("Maximum: ",max)
        print("Number of occurences: ",ct)
        break
    else:
        if n==max:         
            ct +=1
        if n > max:
            max=n
       
