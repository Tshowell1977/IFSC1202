ct=0
Sum=0
min=0
max=0
while 1:  
      n = float(input("Enter a Value (zero to quit):"))   
      if n ==0:
        print("Count: ",ct)
        print("Sum: ",Sum)
        if ct==0:
            print("Average: ","Not defined")
        else:
            print("Average: ",Sum/ct)
        print("Minimum: ",min)
        print("Maximum: ",max)
        break
      else:
        ct +=1
        Sum +=n        
        if ct ==1:
            max = n
            min = n        
        if n > max:
            max = n
        if n < min:
            min = n