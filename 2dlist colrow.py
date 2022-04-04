n=int(input("Input the Number of Rows and Columns: "))

matrix=[]
for i in range(1,n+1):
    new_row=[]
    temp=int(input("Input the Number : "))
    for j in range(1,n+1):
        new_row.append(temp)
    matrix.append(new_row)
for row in matrix:
    print(row)