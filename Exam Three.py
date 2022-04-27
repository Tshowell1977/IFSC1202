class House:
    def __init__(self,address,sqft,price):
        self.address = address
        self.sqft = sqft
        self.price = price
    def costpersqft(self):
        return (self.price/self.sqft)
    def payment(self,ar,ny):
        r = (ar/100)/12
        n = ny*12
        temp = (1+r)**n
        payment = (self.price)*((r*temp)/(temp-1))
        return payment
def main():
    try:
        HouseList = []
        infile = open("/workspace/IFSC1202/Exam Three Houses.txt","r")
        filecontent = infile.readlines()
        for line in filecontent:
            line = line[:-1].split(",")
            houseobj = House(line[0],float(line[1]),float(line[2]))
            HouseList.append(houseobj)
        interestrate = float(input("Enter interest rate :"))
        years = float(input("Enter years of Mortgage : "))
        print("\nOUTPUT : \n\n\tAddress\t\t\tSq Ft\tSqFt Cost\tPrice\t\tPayment")
        for house in HouseList:
            print("\t{:s}\t\t{:.0f}\t{:.2f}\t\t{:.0f}\t\t{:.2f}".format(house.address,house.sqft,house.costpersqft(),(house.price),house.payment(interestrate,years)))
    except IOError as err:
        print("File Operation Failed!!!"+str(err))
if(__name__ == "__main__"):
    main()