N=input("Enter Number: ")
prod=1
sum=0
for x in range(1,int(N)+1):
    prod *=x
    sum +=prod

print(sum)