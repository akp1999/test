def add (num1: int , num2:int):
    total = num1+num2
    return total 

x=add (10,10)
print(x)
print(add(20,30))


def addition (n1:int , n2:int) -> int :
    total = n1+n2
    return total

n1 = int(input("enter the first number to be printed = "))
n2 = int(input("enter second number to be printed = "))
x= addition(n1,n2)
print(x)

def even_odd(x:int):
    if (x%2==0):
        print("even")
    else :
        print("odd")



