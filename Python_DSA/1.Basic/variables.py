"""
RUles to name a variable:
1. It should always start with a-z A-Z _
2. It can contain a-z A-Z _ 0-9
3. It cannot contain symbols
4. Cannot use reserved keywords - if else while 33-36
5. It is case sensitive

"""

x = 5
y = 10
z = x + y
Y = 3
print(z + Y)

"""
Data Types in Python
Integer (int)
Float (float) (decimals)
String (str)
"""

print(type(z))

# print types
print(Y)
print("value of x", x, "value of y", y)
# below is the best method for devlopers to pass variables.
print(f"value of x {x}")
print(f" {x} ")
