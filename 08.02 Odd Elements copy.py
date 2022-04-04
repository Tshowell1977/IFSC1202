s=input(" Enter Values Seperated by Spaces:")
a=s.split()
for i in range (len(a)):
    if int(a[i]) % 2==1:
        print(a[i])