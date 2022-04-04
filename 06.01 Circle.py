from math import pi
    
def area(R):
    A = float(pi*R*R)
    return (A)
def circumference(R):
    C= float(pi*R*2)
    return (C)
def diameter(R):
    D = float(2*R)
    return (D)

print("{:>15s} {:>15s} {:>15s} {:>15s}".format("Radius","Diameter","Circumference","Area"))
Radius = open("06.01 Radius.txt")

R = Radius.readline()
while R != "":
    RFP=float(R)
    print("{:15.5f} {:15.5f} {:15.5f} {:15.5f}".format(RFP,diameter(RFP),circumference(RFP),area(RFP)))
    R = Radius.readline()


Radius.close()