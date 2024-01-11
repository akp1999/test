a: int = 5
b: int = 10
print(a > 5 and b >= 10)
print(a >= 5 or not b > 10)
print(not (a > 5 and b > 5))
print(not (a < 10 or not b < 10))
print(not (not a <= 5 or not b >= 10))

km: int = int(input("enter the no of km ="))
miles: float = float(0.6)
print("miles = ", km * miles)

x: int = int(input("enter the first number = "))
y: int = int(input("enter the first number = "))
z: int = int(input("enter the first number = "))
a = (x + y + z) / 3
print("Average is = ", a)

rs: int = int(input("enter the rs details = "))
ps: int = int(rs * 100)
print("paise details are = ", ps)

side: int = int(input("enter the side details of square = "))
area: int = side * side
print("Area of Square = ", area)

x: int = int(input("enter the no u want to check it is divisble by 3 or not = "))
y: int = x % 3
if y == 0:
    print("no is divisible by 3")
else:
    print ("no is not divisble by 3")


x: int = int(input("enter the no u want to check it is even or odd = "))
y: int = x % 2 
if y == 0:
    print("no is even")
else:
    print ("no is odd")

x: int = int(input("enter the first side = "))
y: int = int(input("enter the second side= "))

if y == x:
    print("its square")
else:
    print ("not square")


x: int = int(input("enter the total no of games played = "))
y: int = int(input("enter the total no of games won = "))
z: int = int(input("enter the total no of games loss = "))

