n1=0
n2=0
ct=1
while 1:
    n = int(input('Enter a Number (zero to quit): '))
    if n == 0: 
        break
    else:
        if n1!=n:
            n1=n
        else:
            ct+=ct
    n2=ct
print(n1,'repeated', n2,'times')