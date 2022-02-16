ct=0
sum=0
while 1:
    n = float(input("Enter a Value (zero to quit):"))  
    if n ==0:
        #print("Sum: ",sum)
        if ct ==0:
            print("Average : ", "Not Defined")
        else:
            print("Average : ", sum/ct)
        break
    else:
        ct +=1
        sum +=n