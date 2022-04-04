
with open("/workspace/IFSC1202/9.0/09.06 CityTemps.txt", 'r') as file:
    temps = []

    line = file.readline()

    while line:
     
        row = line.split()
        temps.append(row)  
        line = file.readline()   

for i in range(len(temps)):
    total = 0    

    for temp in temps[i][1:]:
        total = total + float(temp)  
   
    average = total / (len(temps[i]) - 1)
    temps[i].append(int(average))  

print(f"{'City' : <12}{'Mo' : <12}{'Tu' : <12}{'We' : <12}{'Th' : <12}{'Fr' : <12}{'Sa' : <12}{'Su' : <12}{'Avg' : <12}")
 
 
for i in range(len(temps)):
    for j in range(len(temps[0])):
        print(f"{temps[i][j] : <12}", end='')
    print("")