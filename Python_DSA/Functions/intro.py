"""
typesof functions:

1. Without Parameter, without return
2. With Parameter, without return
3. Without Parameter, with return
4. With Parameter, with return
"""


# 1. Without Parameter, without return
def displayMotherInfo():
    print("Hello World")
    print("Good bye")
    print("We are learning python")


def coding():
    print("We are doing coding")


displayMotherInfo()
displayMotherInfo()
coding()


# scoping
# variables inside function called local variable , and its life only under function
def adddd():
    a = 10
    b = 5
    print(a + b)


a = 5
adddd()
print(a)


def mull():
    a = int(input("Enter value of a = "))
    b = int(input("Enter value of b = "))
    print(a * b)


def div():
    a = int(input("Enter value of a = "))
    b = int(input("Enter value of b = "))
    print(a / b)


mull()
div()


def addd(a, b, c, d):
    print(a + b + c + d)


def mul(a, b, c, d):
    print(a * b * c * d)


addd(10, 20, 20, 40)
mul(10, 20, 30, 40)


# below line is best explain annotation , like we are letting know python that a,b,c would be int , but it wont anything
def add(a: int, b: int, c: int):
    print(a + b + c)


add(10, 20, 30)


def greet(name: str, age: int, gender: str):
    print(name, age, gender, sep="\n")


name = str(input("enter name ="))
age = int(input("enter age ="))
gender = str(input("enter gender="))
greet(name, age, gender)

# named arugument


def marks(physics, chemistry, english, science, hindi):
    total = physics + chemistry + english + science + hindi
    per = total / 500 * 100
    print(f"Your total marks = {total}")
    print(f"Your percentage scored = {per:.2f}")


# marks(67, 45, 32, 12, 99)
# marks(english=10, hindi=99, physics=67, chemistry=67, science=91)
marks(67, 99, hindi=100, science=11, english=44)
