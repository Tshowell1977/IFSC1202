matrix=[]
for i in range(1,7):
    new_row=[]
    for j in range(1,7):
        new_row.append(i+j)
    matrix.append(new_row)
for row in matrix:
    print(row)