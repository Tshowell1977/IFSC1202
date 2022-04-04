s=input(" Enter Values Seperated by Spaces:")
a=s.split()
x=1
for i in range (len(a)):
    if int(a[i]) >x:
        print(a[i])
        x=(a[i])