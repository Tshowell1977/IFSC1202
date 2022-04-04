import math
N=float(input("Enter a Number:"))  
x=math.floor(N)
t=round(N-x,10)
A=("Fractional part: ")+str(t)
print("{:s}".format (A))