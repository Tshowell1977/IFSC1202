N=int(input("Enter N: "))
 
for i in range(2,N):
    if N % i == 0:
        print("Composite")
        break
else:
    print("Prime")     