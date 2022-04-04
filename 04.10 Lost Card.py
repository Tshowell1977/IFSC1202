N=int(input('Enter Number of Cards: '))
ct=0
#counting the total cards
for i in range(1,N+1):
  ct=ct+i
  #print(ct)
#counting the total of entered cards  
  ct1=0
for j in range(N-1):
  count=int(input("Enter Number : "))
  ct1+= count
  #print(ct1)

#value of mmissing card
d=ct-ct1
print("Missing Card: " + str(d))