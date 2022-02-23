from math import pi
    
def area(R):
    A = float(math.pi*R^2)
    Return (A)
def Circumference(R):
    C= float(math.pi*R*2)
    Return (C)
def diameter(R):
    D = float(2*R)
    Return (D)


Radius = open("06.01 Radius.txt")

R = Radius.readline()
while R != "":


	print(R)



	R = Radius.readline()


Radius.close()