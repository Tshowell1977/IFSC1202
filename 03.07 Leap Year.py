N=input("Enter a Year:")  
n=int(N)/4
j=int(N)/100
k=int(N)/400
import math 
x=math.floor(n)
t=round(n-x,10)
ft=int(t%10*10)
z=math.floor(k)
r=round(k-z,10)
kt=int(r%10*10)
#A=("Tenths Value: ")+str(ft)
#B=("Tenths Value f2: ")+str(kt)
#print("{:s}".format (A))
#print("{:s}".format (B))
#print(n)
if ft==0 and j!=0:
    print("Leap Year") 
else:
    print("COMMON YEAR")