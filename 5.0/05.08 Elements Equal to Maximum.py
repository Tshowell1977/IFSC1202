max = 0
occured = 0
fn = True
while True:
    n = int(input('Enter a Number (zero to quit): '))
    if n == 0: 
        break
    if fn or max < n:
        max = n
        occured = 1
    elif max == n:
        occured += 1
    fn = False
print('Maximum:', max)
print('Number of Occurrences:', occured)