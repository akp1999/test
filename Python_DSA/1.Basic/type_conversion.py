"""
To convert from one DT to another DT
str -> int
int -> str
float -> int
int -> float
"""
a = "100"
b = "200"
print(a + b)
# below line is used to type cast string into integer.
c = int(a)
d = int(b)
print(c + d)

a = input("enter you name  = ")
b = int(input("entter ypur age = "))
c = input("enter your gender = ")

print(a, end=" ")
print(b, end=" ")
print(c, end=" ")

print(f"{a}{b}{c}")
