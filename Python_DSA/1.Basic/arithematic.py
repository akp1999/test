"""
Types of Operators:
1. Arithmetic
2. Assignment
3. Comparision
4. Logical
5. Membership
6. Identity
7. Bitwise
"""

"""
Arithmetic Operators
+, -, / , *
**
// (Floor division) (Answer always in Integer)
% (Remainder) (Modulus)
"""
a = -16
b = 5
print(a / b)
print(a // b)
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)  # Always answer is in float
# print(a**b)  # a^b = 10^5 = 10x10x10x10x10
# print(a % b)


# below example signifies that we can easily chane variables value at any time.
c=5
c += 5
print (c)

c=5
c *=5
print(c)

c=5
c /=5
print(c)

c=5
c %=5
print(c)

c=10
c //5
print(c)

c=5
c **5
print(c)


"""
To compare values
Answer always comes in BOOLEAN (True/False)
>, <, >=, <=, ==, !=
"""
a = 10
b = 10
# print(a > b)
# print(a < b)
# print(a >= b)
# print(b >= a)
# print(a == b)
print(a != b)


"""
AND, OR, NOT (To compare, 2 or more conditions) (answer is always in BOOL)
AND
C1  C2  Result
F   F   F
F   T   F
T   F   F
T   T   T
OR
C1  C2  Result
F   F   F
F   T   T
T   F   T
T   T   T
NOT (Ulta kar deta hai)
"""
physics = 17
chemistry = 85
# print(physics >= 33 or chemistry >= 33)  # F or T = T
# print(not physics >= 33)
# print(not (physics >= 33 or chemistry >= 33))  # not T
print(not physics >= 33 or not chemistry >= 33)
# not F or not T
# T or F
# T