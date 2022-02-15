N=input("Enter a Number (zero to quit):")
while N != 0:
    sum=0
    for x in range(1,int(N)+1):
     sum +=x
    
print(sum)