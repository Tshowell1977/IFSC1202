f1 = open("06.05 CompareFileA.txt")
f2 = open("06.05 CompareFileB.txt")
list1 = []
list2 = []
for i in f1:
    list1.append(i)
for i in f2:
    list2.append(i)

ct=0

for i in range(len(list1)):
    if (list1[i]!=list2[i]):
        print(f"line :{i+1} - {list1[i]}")
        print(f"line :{i+1} - {list2[i]}")
        ct+=1

print (ct,"differences")
f1.close()
f2.close()