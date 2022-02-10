N=input("Enter N: ")
c=1
if int(N)<9 or int(N)==9:
    for x in range(1,int(N)+1):
        N = int(N)-1
        for t in range(1,int(c)):
            c = c+1
        print(c)
    
