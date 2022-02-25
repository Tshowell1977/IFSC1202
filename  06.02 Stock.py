Stock=open("06.02 Stock.txt","r")

RC = Stock.read()
RC = [float(i) for i in RC.split()]
    
print("{:>15s} {:>15s}".format("Price","Change"))

print("{:>15}".format(RC[0]))

for i in range(1,len(RC)):
    

    percentchange = ((RC[i] - RC[i-1])/RC[i-1]) * 100

    print("{:15.2f} {:15.2f}".format(RC[i],percentchange))
    

Stock.close()