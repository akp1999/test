x= None
print(x)
print(type(x))



def laregestNo(p=None,q=None,r=None) -> int : 
     if p!= None and q != None and r != None:
            if (p>q and p>r):
                return p
            elif(q>p and q>r):
                return q
            else:
                return r
     else :  
         return (-1)
    


print(laregestNo(10,20,30))
print(laregestNo())

def power(base: int = 2 , exponent : int = 3) ->int :
     return base**exponent

print(power(3,3))
print(power())


def middle(p:int =0,q:int = 0,r:int =0) :
     return q

def divisiblity(num:int) -> int:
     if (num%3==0 and num%4==0):
          return num 
     else:
          return (-1)
     
print(divisiblity(middle(10,12,30)))


"""
Write a Python program that takes four numbers from the user. 
Implement a function to find the average of the first three numbers. 
Then, create another function to check if the average is greater than or equal to the fourth number. 
Make sure to use these two functions to determine and print whether the average 
is greater than or equal to the fourth number or not.
"""


def calculate_average(num1: int, num2: int, num3: int) -> float:
    return (num1 + num2 + num3) / 3


def is_average_greater_or_equal(average: float, fourth_number: int) -> bool:
    return average >= fourth_number


num1: int = int(input("Enter the first number: "))
num2: int = int(input("Enter the second number: "))
num3: int = int(input("Enter the third number: "))
num4: int = int(input("Enter the fourth number: "))

average_value: float = calculate_average(num1, num2, num3)

# Check if the average is greater than or equal to the fourth number
result = is_average_greater_or_equal(average_value, num4)

# Display the result
print(f"The average of {num1}, {num2}, and {num3} is: {average_value}")

if result:
    print(f"The average is greater than or equal to {num4}.")
else:
    print(f"The average is less than {num4}.")