i = 1
while i <= 5:
    print("Hello World")
    i = i + 1
    print("Done")

x:int= int(input("enter no = "))
i = 1
while i <= x:
    print(i,end =" ")
    i = i + 1
    

def fun(n1,n2):
    i=n1
    while(i<=n2):
        print(i)
        i+=1
fun (1,7)



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