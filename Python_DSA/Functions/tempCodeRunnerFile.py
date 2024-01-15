def greet(name: str, age: int, gender: str):
    print(name, age, gender,sep="\n")


name = str(input("enter name ="))
age = int(input("enter age ="))
gender = str(input("enter gender="))
greet(name, age, gender)