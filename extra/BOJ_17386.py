a1,b1,a2,b2 = map(int,input().split())

c1,d1,c2,d2 = map(int,input().split())

if (a1-a2)*(d1-d2) == (b1-b2)*(c1-c2) and not ((a1-a2)*(d1*c2 + c1*d2)==(b1*a2+a1*b2)*(c1-c2)):
    print(0)
else:
    if (a1 > c1 and a1 > c2) or (a1< c1 and a1 < c2) or (b1 > d1 and b2 > d1) or (b1 < d1 and b2 < d1):
        print(0)
    else:
        print(1)