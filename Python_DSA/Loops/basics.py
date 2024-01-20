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


def calSum(n1: int, n2: int):
    i = n1
    total = 0
    while i <= n2:
        if i % 3 == 0 and i % 6 == 0:
            total = total + i
        i += 1
    return total

x = calSum(1, 20)
print(x)

def printFactors(num: int):
    i = 1
    while i <= num:
        if num % i == 0:
            print(i, end=" ")
        i += 1
    print()

def countFactors(num: int):
    i = 1
    count = 0
    while i <= num:
        if num % i == 0:
            count = count + 1
        i += 1
    print(f"Total factors = {count}")

def checkPrime(num: int):
    i = 1
    factors = 0
    while i <= num:
        if num % i == 0:
            factors = factors + 1
        i += 1
    # ---
    if factors == 2:
        print("It is a prime number")
    else:
        print("It is not a prime number")

# countFactors(10)
# countFactors(7)
checkPrime(10)
checkPrime(7)