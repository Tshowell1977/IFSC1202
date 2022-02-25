
    
def percentchange (RO):
    P = float(((RO-RF)/(RF))*100)
    return (P)


print("{:>15s} {:>15s}".format("Price","Change"))
Stock = open("06.02 Stock.txt")

RC = Stock.readline()
for i in range(1,len(RC)):
    RO=float(RC)
    RF=float(RO-1)
    print("{:15.2f} {:15.2f}".format(RO,percentchange(RO)))
    RC = Stock.readline()


Stock.close()