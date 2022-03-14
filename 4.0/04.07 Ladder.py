N=int(input("Enter N: "))
if int(N)<9 or int(N)==9: 
    for i in range(N):
        for k in range(i+1):
            print(k+1,end="")
        print()