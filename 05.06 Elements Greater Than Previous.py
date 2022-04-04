ct=0
max=0
num=0
while 1:
    n = float(input("Enter a Value (zero to quit):"))  
    if n ==0:
        print("Number of values Greater then Previous: ",num)
        break
    else:
        ct +=1
        if n > max:
            max=n
            num +=num 
            