A=int(input("Enter A: "))
B=int(input("Enter B: "))
for n in range(A,B+1):
    if n > 1:
        for i in range(2,n):
            if n % i == 0:
                break
        else:
            print(n)     