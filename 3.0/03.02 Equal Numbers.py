f = int(input("Enter first number: "))
s = int(input("Enter second number: "))
t = int(input("Enter third number: "))
if f == s and s == t:
    print(3)
if f == s and s != t: 
    print(2)
if s == t and f != s:
    print(2)
if f != s and s != t and t!=f:
    print(0)
