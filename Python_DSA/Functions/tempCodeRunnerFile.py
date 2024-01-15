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

amount:int=int(input("enter the bill amount"))
discountedBill(amount)