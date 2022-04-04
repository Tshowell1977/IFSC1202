import math
N=float(input("Enter a Number:"))  
x=math.floor(N)
#print (x)
#print (N)
t=round(N-x,10)
ft=int(t%10*10)
A=("Tenths Value: ")+str(ft)
print("{:s}".format (A))