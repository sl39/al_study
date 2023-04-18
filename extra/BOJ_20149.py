a1,b1,a2,b2 = map(int,input().split())

c1,d1,c2,d2 = map(int,input().split())


def line(a1,b1,a2,b2,c1,d1):
    tmp = (a1-a2) * d1 - (b1-b2) * c1 + a2*b1 - a1*b2
    if tmp > 0:
        return 1
    if tmp < 0:
        return -1
    return 0


def mn(a1,b1,a2,b2,c1,d1,c2,d2):
    if (abs(a1-a2) == abs(a1-c1) + abs(a2-c1) and abs(b1-b2) == abs(b1-d1) + abs(b2-d1)) or (abs(a1-a2) == abs(a1-c2) + abs(a2-c2) and abs(b1-b2) == abs(b1-d2) + abs(b2-d2)):
        return 1
    
    return 0

ans = 0

if line(a1,b1,a2,b2,c1,d1) * line(a1,b1,a2,b2,c2,d2) <=0 and line(c1,d1,c2,d2,a1,b1) * line(c1,d1,c2,d2,a2,b2) <=0:
    if (a1-a2)*(d1-d2) != (b1-b2)* (c1-c2):
        ans = 1
    else:
        if mn(a1,b1,a2,b2,c1,d1,c2,d2):
            ans = 2
        elif mn(c1,d1,c2,d2,a1,b1,a2,b2):
            ans = 2
        else:
            pass

else:
    pass

x1 = a1-a2
y1 = b1-b2
x2 = c1-c2
y2 = d1-d2
# y = (y1/x1) * x -(a2*b1 - a1*b2)/x1
# y = (y2/x2) * x -(c2*d1 - c1*d2)/x2
# (a2*b1 - a1*b2)/x1 -  (c2*d1 - c1*d2)/x2 = x((y1/x1)-(y2/x2))
# x = ((a2*b1 - a1*b2)/x1 -  (c2*d1 - c1*d2)/x2) / ((y1/x1)-(y2/x2))

if ans == 0:
    print(0)
elif ans == 1:
    print(1)
    if x1 == 0:
        x = a1
        y = (y2/x2) * x -(c2*d1 - c1*d2)/x2
    elif x2 == 0:
        x = c1
        y = (y1/x1) * x -(a2*b1 - a1*b2)/x1
    else:
        x = ((a2*b1 - a1*b2)/x1 -  (c2*d1 - c1*d2)/x2) / ((y1/x1)-(y2/x2))
        y = (y1/x1) * x -(a2*b1 - a1*b2)/x1
    print(x,y)

else:
    print(1)
    if min(a1,a2) < c1 < max(a1,a2) or min(a1,a2) < c2 < max(a1,a2):
        pass
    elif min(c1,c2) < a1 < max(c1,c2) or min(c1,c2) < a2 < max(c1,c2):
        pass
    elif min(b1,b2) < d1 < max(b1,b2) or min(b1,b2) < d2 < max(b1,b2):
        pass
    elif min(d1,d2) < b1 < max(d1,d2) or min(d1,d2) < b2 < max(d1,d2):
        pass
    elif (a1 == c1 and b1 == d1 and a2 == c2 and b2 == d2) or (a2 == c1 and b2 == d1 and a1 == c2 and b1 == d2):
        pass
    else:
        if a1 == c1 and b1 == d1:
            print(a1,b1)
        elif a1 == c2 and b1 == d2:
            print(a1,b1)
        elif a2 == c1 and b2 == d1:
            print(a2,b2)
        elif a2 == c2 and b2 == d2:
            print(a2,b2)