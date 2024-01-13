x: int = int(input("enter the first number = "))
y: int = int(input("enter the second nuber = "))
if x % y == 0:
    print("first no is divisble by second")
else:
    print("first no is not divisible by second")



x:int = int(input("enter the total no of class held = "))
y:int = int (input("enter total of class attended = "))
z :int = int(y/x*100)
print ("total percentage of attendemce = ",z)
if (z>75):
    print("eligible to attend the class")
else:
    print ("Sorry ! not eligible ")




x:int = int(input("enter the no ="))
if ( x%2==0 and x%3==0 and x%8!=0) :
    print("divisible by 2 and 3 but not by 8")


x:int = int(input("enter the no ="))
if ( x >90 and x<100):
    print("grade is between 90 and 100")
elif ( x >80 and x<90):
    print("grade is between 80 and 90")
elif ( x >70 and x<80):
    print("grade is between 70 and 80")
elif ( x >60 and x<70):
    print("grade is between 60 and 70")
else:
    print("below 60")


x:int = int(input("enter the purchased bill value ="))
if ( x >50000):
    print("final bill = ", x - (x*0.3))
elif ( x >40000 and x<50000):
    print("final bill = ", x - (x*0.25))
elif ( x >30000 and x<39000):
    print("final bill = ", x - (x*0.20))
elif ( x >10000 and x<30000):
    print("final bill = ", x - (x*0.10))
else:
    print("final bill = ",x)

p:int = int(input("enter the p value ="))
q:int = int(input("enter the q value ="))
r:int = int(input("enter the r value ="))
s:int = int(input("enter the s value ="))
if ( p>q and p>r and p>s):
    print("p is greates no ")
elif (q>p and q>s and q>r):
    print("q is greatest")
elif (r>p and r>q and r>s):
    print("r is greatest")
else:
    print("s is greates")

x:int = int(input("enter the purchased bill value ="))
if ( x <10000):
    print("final bill = ", x + (x*0.05))
elif ( x >10000 and x<20000):
    print("final bill = ", x + (x*0.10))
elif ( x >20000 and x<40000):
    print("final bill = ", x + (x*0.20))
elif ( x >50000):
    print("final bill = ", x + (x*0.25))
else:
    print("final bill = ",x)

x:int = int(input("enter the purchased bill value ="))
if  ((x%4==0 and x%100!=0) or (x%400==0)):
    print("its leap year") 







