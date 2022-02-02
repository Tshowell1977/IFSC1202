N=int(input("Enter From Value:")) 
U=str(input("Enter From Unit (in,ft,yd,mi):"))
#print(N)
#print(U)
if U=="in" or U=="ft" or U=="yd" or U=="mi":
    print("yes")
else:
    print("From Unit is not Valid.")
UT=str(input("Enter To Unit (in,ft,yd,mi):"))
if UT=="in" or UT=="ft" or UT=="yd" or UT=="mi":
    print("yes")
else:
    print("From Unit is not Valid.")