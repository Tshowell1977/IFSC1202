A=input("Enter A: ")
B=input("Enter B: ")
prod=0

for x in range(int(A),int(B)+1):
    prod =x*x
    print(str(x)+"*"+str(x)+"="+str(prod))
    