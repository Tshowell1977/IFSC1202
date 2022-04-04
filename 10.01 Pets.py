# Step 1 - Define the class object
class Pet():
# Step 2 - Define the initializer and any default values
    def __init__(self):

# Step 3 - Define the object attributes
        self.name=""
        self.Type=""
        self.age=0

# Step 4 - Define Actions (Methods) associated with the object
#open file

f = open('/workspace/IFSC1202/10.01 Pets.txt')

#create a list to hold objects of Pets

#read data from txt and store it

line = f.readline()
line=line.replace ("\n","")
data = line.split(',')
mypet1=Pet()
mypet1.name=data[0]
mypet1.Type=data[1]
mypet1.age=int(data[2])

line = f.readline()
line=line.replace ("\n","")
data = line.split(',')
mypet2=Pet()
mypet2.name=data[0]
mypet2.Type=data[1]
mypet2.age=int(data[2])

line = f.readline()
line=line.replace ("\n","")
data = line.split(',')
mypet3=Pet()
mypet3.name=data[0]
mypet3.Type=data[1]
mypet3.age=int(data[2])
#print header

print("{:>11} {:>17} {:>17} ".format("Name","Type","Age"))


print("{:>11} {:>17} {:>17} ".format(mypet1.name,mypet1.Type,mypet1.age))

print("{:>11} {:>17} {:>17} ".format(mypet2.name,mypet2.Type,mypet2.age))

print("{:>11} {:>17} {:>17} ".format(mypet3.name,mypet3.Type,mypet3.age))
#close file

f.close()