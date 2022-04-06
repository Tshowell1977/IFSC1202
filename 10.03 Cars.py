class Car: 
        def __init__(self,year,make):
                self.Year=year 
                self.Make=make 
                self.Speed=0         
        def Accelerate(self,x):
                self.Speed=self.Speed+x      
        def Brake(self,x):
                if self.Speed<x: 
                        x=x-self.Speed
                self.Speed=self.Speed-x        
def changespeed(speed,c):
        print("\nChange Speed")
        for i in speed:
                print(i,end="\t")
                if i>0: 
                        c.Accelerate(i)
                else:
                        i=i*(-1)
                        c.Brake(i) 
                print(c.Speed) 
words=[]
speed=[]
with open("/workspace/IFSC1202/10.03 Cars.txt",mode='r') as file: 
        line=file.read()
        lines=line.split("\n")
        word=lines[0].split(",")
        for k in word:
                words.append(k)
        yr=words[0] 
        mk=words[1] 
        for k in range(1,len(lines)):
                speed.append(int(lines[k])) 
c=Car(yr,mk)
print("Make: ",c.Make) 
print("Year: ",c.Year) 
changespeed(speed,c) 