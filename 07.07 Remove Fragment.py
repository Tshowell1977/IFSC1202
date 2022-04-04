s = str(input("Enter the string: "))
if s.count("h") >= 2:
    print(s[:s.find("h")] + s[s.rfind("h") + 1:])
else:
    print(s.count("h"))