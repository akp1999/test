x:int = int(input("enter the purchased bill value ="))
if  ((x%4==0 and x%100!=0) or (x%400==0)):
    print("its leap year") 
