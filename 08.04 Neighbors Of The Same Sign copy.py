s=input(" Enter Values Seperated by Spaces:")
lst = list(map(int, s.split()))
i = 1

for i in range(1, len(lst)):
  if lst[i] * lst[i-1] > 0:
    print(str(lst[i - 1]), str(lst[i]))
    break
  elif i == len(lst)-1:
    print("0")
