s = input("Enter a string: ")
a=s.find('h') 
a=a+1 
b=s.rfind('h') 
if(a==b): 
   print(a)
else:
   print(s[:a],end="") 
   t=s[a:b] 
   print(t[::-1],end="") 
   print(s[b:],end="") 