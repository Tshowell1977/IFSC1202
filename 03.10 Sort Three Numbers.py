A=int(input("Enter First Number: "))
B=int(input("Enter Second Number: "))
C=int(input("Enter Third Number: "))

if A<B and A<C:
    X=A
    if B<C:
        Y=B 
        Z=C
    else:
        Y=C
        Z=B
if B<A and B<C:
    X=B
    if A<C:
        Y=A 
        Z=C
    else:
        Y=C
        Z=A
if C<A and C<B:
    X=C  
    if A<B:
        Y=A 
        Z=B
    else:
        Y=B
        Z=A

print(str(X)+str(Y)+str(Z))