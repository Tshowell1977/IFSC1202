# opening 09.06 CityTemps.txt file in reading mode
with open("/workspace/IFSC1202/9.0/09.06 CityTemps.txt", 'r') as file:
    temps = []  # initializing temps list to store data

    # reading first line of input file
    line = file.readline()

    # using while loop to read through each line
    while line:

        # spitting line into list by taking space as delimiter
        row = line.split()
        temps.append(row)  # appending list to temps list
        line = file.readline()   # read next line

# using for loop to go through each city temperatures
for i in range(len(temps)):
    total = 0    

    for temp in temps[i][1:]:
        total = total + float(temp)   # adding temperature to total

    # calculating average
    average = total / (len(temps[i]) - 1)
    temps[i].append(int(average))  # appending average to temps list

# printing  heading of table
print(f"{'City' : <10}{'Mo' : <10}{'Tu' : <10}{'We' : <10}{'Th' : <10}{'Fr' : <10}{'Sa' : <10}{'Su' : <10}{'Avg' : <10}")
  
# printing data in table form using f-string 
for i in range(len(temps)):
    for j in range(len(temps[0])):
        print(f"{temps[i][j] : <10}", end='')
    print("")