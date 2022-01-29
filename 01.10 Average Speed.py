k=float(input("Enter kILOMETERS:"))
m = float(k) / 1.61
M=int(input("Enter Minutes:"))
S=int(input("Enter Seconds:"))
Mhr=float(M / 60)
Shr=float((S/60)/60)
hrtotal=float(Mhr + Shr)
miles=k/1.61
mph= miles/hrtotal
print(mph)