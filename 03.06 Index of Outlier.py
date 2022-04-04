fn=input("Enter First Number:") 
sn=input("Enter Second Number:") 
tn=input("Enter Third Number:") 
if fn!=sn and fn!=tn:
    print("1")
if sn!=tn and sn!=fn:
    print("2")
if tn!=fn and tn!=sn:
    print("3")