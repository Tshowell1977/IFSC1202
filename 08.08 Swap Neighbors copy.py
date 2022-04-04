x = input("Enter values seperated by spaces: ")
lst = list(map(int, x.split()))

for i in range(0, len(lst), 2):
  popval = lst.pop(i)
  lst.insert(i+1, popval)
  
print(lst)