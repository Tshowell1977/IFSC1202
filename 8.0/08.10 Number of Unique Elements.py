inputlist = list()

Input = input("Enter values seperated by spaces: ").split()

# n will be length of input

n = len(Input)

for i in range(n):

    inputlist.append(int(Input[i]))

for i in range(n):

    count = 1 

for j in range(n):

    if inputlist[i] == inputlist[j] and i != j:

        count += 1

if count == 1:

    print("Unique Elements: ",inputlist[i], end="   ",)\
 

