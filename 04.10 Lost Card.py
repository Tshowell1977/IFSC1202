N=int(input('Enter Number of Cards:'))
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


d=ct-ct1
print("Missing Card: " + str(d))
  





#sum of the values from 1 to N (Total Value of Cards)


#sum of the values on remaining cards (sum of elements of array A)


#value on the lost card
