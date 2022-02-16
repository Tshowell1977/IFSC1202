ct=0
sum=0
min=0
max=0
while 1:  
      n = float(input("Enter a Value (zero to quit):"))   
      if n ==0:
        print("Count: ",ct)
        print("Sum: ",sum)
        if ct==0:
            print("Average: ","Not defined")
        else:
            print("Average: ",sum/ct)
        print("Minimum: ",min)
        print("Maximum: ",max)
        break
      else:
        ct +=1
        sum +=n        
        if ct ==1:
            max = n
            min = n        
        if n > max:
            max = n
        if n < min:
            min = n