def isEven(number):
    return number %2 ==0
def isOdd(number):
    return number %2 ==1
def isPrime(number):
    if(number> 1):

        for index in range(2,number//2):

            if(number % index == 0):
                return False
        return True
    else:
        return False

inputFile = open("06.06 Numbers.txt","r")
outputEven = open("06.06 Evennumbers.txt","w+")
outputOdd = open("06.06 Oddnumbers.txt","w+")
outputprime = open("06.06 Primenumbers.txt","w+")
cteven=0
ctodd=0
ctprime=0
ct=0
for line in inputFile:
    line = int(line.strip())
    if isEven(line):
        outputEven.write(str(line) + "\n")
        cteven+=1
    elif isOdd(line): 
        outputOdd.write(str(line) + "\n")
        ctodd+=1
    if isPrime(line):
        outputprime.write(str(line) + "\n")
        ctprime+=1

    ct+=1
print(cteven,"even numbers")
print(ctodd,"odd numbers")
print(ctprime,"prime numbers")
print(ct,"numbers read")