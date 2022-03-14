A=int(input("Enter Classroom A:"))
B=int(input("Enter Classroom B:"))
C=int(input("Enter Classroom C:"))

A1=int(A // 2)
A2=int(A % 2)
A3=int(A1 + A2)

B1=int(B // 2)
B2=int(B % 2)
B3=int(B1 + B2)

C1=int(C // 2)
C2=int(C % 2)
C3=int(C1 + C2)

print(A3 + B3 + C3)