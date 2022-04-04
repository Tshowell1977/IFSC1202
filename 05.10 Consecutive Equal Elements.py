n = 1
previous = 0
i = 0
ct = 0
x = None
maxct = 0
while n != 0:
    n = int(input("Enter a Number (zero to quit): "))
    if n != 0:
        if i == 0:
            previous = n
            ct = 1
        else:
            if n == previous:
                ct += 1
            else:
                if ct > maxct:
                    maxct = ct
                    x = previous
        i += 1
        previous = n

print(x, "repeated", maxct, "times")