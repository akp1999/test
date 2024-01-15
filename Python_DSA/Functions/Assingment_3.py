def laregestNo(p:int,q:int,r:int):
    if (p>q and p>r):
        print("p is gretaest")
    elif(q>p and q>r):
        print("q is greatest")
    else:
        print("s is greatest")

p:int = int(input("enter the first no = "))
q:int = int(input("enter the second no = "))
r:int = int(input("enter the third no = "))
laregestNo(p,q,r)

def smallestNo(p:int,q:int,r:int):
    if (p<q and p<r):
        print("p is smallest")
    elif(q<p and q<r):
        print("q is smallest")
    else:
        print("s is smallest")

p:int = int(input("enter the first no = "))
q:int = int(input("enter the second no = "))
r:int = int(input("enter the third no = "))
smallestNo(p,q,r)

def leapYear(year:int):
    if ((year%4==0 and year%100!=0) or (year%400==0)):
        print("its leap year")
    else:
        print("its NOT leap year")

year:int = int(input("enter the year you want to check as leap year or not = "))
leapYear(year)


def discountedBill(amount:int):
    if ( amount >50000):
        print("final bill = ", amount - (amount*0.3))
    elif ( amount >40000 and amount<50000):
        print("final bill = ", amount- (amount*0.25))
    elif ( amount >30000 and amount<39000):
        print("final bill = ", amount - (amount*0.20))
    elif ( amount >10000 and amount<30000):
        print("final bill = ", amount - (amount*0.10))
    else:
        print("final bill = ",amount)

amount:int=int(input("enter the bill amount= "))
discountedBill(amount)

#remaining questions are same as above question so , leave it here :