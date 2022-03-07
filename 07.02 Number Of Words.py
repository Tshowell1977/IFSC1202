def space(st):    
    ct = 0  
    for i in range(0, len(st)):   
        if st[i] == " ":
            ct += 1   
    return ct
st = input("Enter your sentence: ")
print(space(st)+1,"Words")