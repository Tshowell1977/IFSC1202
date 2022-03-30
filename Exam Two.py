carsales = open("carsales.txt", "r")
saleslist = []
line = carsales.readline()
while line:
    make, price = line.split(",")
    saleslist.append([make, int(price)])
    line = carsales.readline()
carsales.close()
ttlcars = 0
avgsaleprice = 0
for i in saleslist:
    ttlcars += 1
    avgsaleprice += i[1]
avgsaleprice = avgsaleprice / ttlcars
avgprice= round(avgsaleprice,2)
print(f"{ttlcars} Total Cars - Average Price: ${avgprice}")

while True:
    carmake = input("Enter Car Make: ")
    if carmake == "":
        break
    carmake = carmake.upper()
    ttlctofcar = 0
    ttlprices = 0
    numbcars = 0
    for j in saleslist:
        if j[0].upper() == carmake:
            ttlctofcar += 1
            ttlprices += j[1]
            numbcars += 1

    if ttlctofcar == 0:
        print("Car Make not found")
        continue
    
    avgprice = ttlprices / numbcars
    ravgprice=round(avgprice)
    perdiff = (avgprice - avgsaleprice) * 100 / avgsaleprice

    print("%6d Cars sold" %(numbcars))
    print("$%5g Average price" %(ravgprice))
    print("%.2f%% Above/Below Average" %(perdiff))
    print()