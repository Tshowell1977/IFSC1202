a = [int(s) for s in input(" Enter Values Seperated by Spaces:").split()]
elements = 0
for i in range(1, len(a) - 1):
  if a[i - 1] < a[i] > a[i + 1]:
    elements += 1
print(elements)