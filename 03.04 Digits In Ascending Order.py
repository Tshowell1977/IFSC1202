N=input("Enter a Number:")  
hd=(int(N)//100)
td=(int(N)//10%10)
od=(int(N)%10)
if hd > td and td > od:
    print (Yes)
if hd > td and td < od:
    print (No)
if hd < td and td > od:
    print (No)