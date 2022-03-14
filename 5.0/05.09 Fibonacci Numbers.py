num = int(input("Enter Fibonnaci Sequence Number: "))
n1, n2 = 1, 0
count = 0
fnum=0  
while count < num:   
       nth = n1 + n2   
       n1 = n2
       n2 = nth
       count += 1
       fnum=nth
print("Fibonacci Number:",fnum)   