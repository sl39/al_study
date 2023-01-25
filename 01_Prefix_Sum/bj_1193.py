X = int(input()) 
n = round((2*X)**(1/2))
T = X - n*(n+1)//2
if n % 2 == 0:
    print(f"{n+T}/{1-T}")
else:
    print(f"{1-T}/{n+T}")
