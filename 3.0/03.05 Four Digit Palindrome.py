N=input("Enter a Number:")  
thd=(int(N)//1000)
hd=(int(N)//100%10)
td=(int(N)//10%10)
od=(int(N)%10)
if thd==od and hd==td:
    print("YES")
else:
    print("NO")