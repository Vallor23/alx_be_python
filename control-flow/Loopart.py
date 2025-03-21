rows = 5

i = 0
while i < rows:
    print(" "* (rows - i), end=' ')
    j = 0
    while j <= i:
        print("*", end=' ')
        j += 1
    i += 1
    print()