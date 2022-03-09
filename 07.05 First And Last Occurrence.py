st = input ("Enter a string : ")
string = st[::-1]
ind1 = st.find('f')
ind = st.rfind('f')

if ind1 == -1:
  print(0)
else:
    n= len(st)
    ind2 = n - ind1
    if ind1 == ind2:
      print (ind1)
    else:
      print (ind1, ind)