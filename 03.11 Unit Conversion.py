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
import math

  #inch to======>  

if U=="in" and UT=="in":
    conversion=N*1
if U=="in" and UT=="ft":
    conversion=N*0.0833333333333333
if U=="in" and UT=="yd":
    conversion=N*0.0277777777777778
if U=="in" and UT=="mi":
    conversion=N*1.578282828282828e-5


#foot to======>

if U=="ft" and UT=="in":
    conversion=N*12
if U=="ft" and UT=="ft":
    conversion=N*1
if U=="ft" and UT=="yd":
    conversion=N*0.3333333333333333
if U=="ft" and UT=="mi":
    conversion=N*1.893939393939394e-4


#Yard to======>

if U=="yd" and UT=="in":
    conversion=N*36
if U=="yd" and UT=="ft":
    conversion=N*3
if U=="yd" and UT=="yd":
    conversion=N*1
if U=="yd" and UT=="mi":
    conversion=N*5.681818181818182e-4

    #Miles to======>

if U=="mi" and UT=="in":
    conversion=N*63360
if U=="mi" and UT=="ft":
    conversion=N*5280
if U=="mi" and UT=="yd":
    conversion=N*1760
if U=="mi" and UT=="mi":
    conversion=N*1

print(N)
print(U)
print(round(float(conversion),7))
print(UT)

#Print(N + U +"==>"+ g + h)