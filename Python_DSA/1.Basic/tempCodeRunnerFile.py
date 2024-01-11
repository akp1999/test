x: int = int(input("enter the total no of games played = "))
y: int = int(input("enter the total no of games won = "))
z: int = int(input("enter the total no of games loss = "))
tie :int = x-y-z
points = ((y*4)+(tie*2))
points = print("total poins for win " , points)