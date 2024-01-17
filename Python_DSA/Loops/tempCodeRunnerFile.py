def printNumbers(n1, n2):
    if n1 < n2:
        i = n1
        while i <= n2:
            print(i, end=" ")
            i += 1
        print()
    elif n2 < n1:
        i = n2
        while i <= n1:
            print(i, end=" ")
            i += 1
        print()
    else:
        print(n1)

printNumbers(5, 8)
printNumbers(9, 3)