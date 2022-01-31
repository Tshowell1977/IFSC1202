f = int(input("Enter first number: "))
s = int(input("Enter second number: "))
t = int(input("Enter third number: "))
if f < s and f < t:
    print(f)
elif s < f and t > s:    
    print(s)
elif t < f and s > t:    
    print(t)