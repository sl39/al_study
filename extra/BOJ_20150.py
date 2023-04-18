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

n = int(input())
lin = []
for i in range(n):
    a,b,c,d = map(int,input().split())
    lin.append((a,b,c,d))

ans = 0
for i in range(n-1):
    a1,b1,a2,b2 = lin[i]
    for j in range(i+1,n):
        c1,d1,c2,d2 = lin[j]



        if line(a1,b1,a2,b2,c1,d1) * line(a1,b1,a2,b2,c2,d2) <=0 and line(c1,d1,c2,d2,a1,b1) * line(c1,d1,c2,d2,a2,b2) <=0:
            if (a1-a2)*(d1-d2) != (b1-b2)* (c1-c2):
                ans = 1
            else:
                if mn(a1,b1,a2,b2,c1,d1,c2,d2):
                    ans = 1
                elif mn(c1,d1,c2,d2,a1,b1,a2,b2):
                    ans = 1
                else:
                    pass

        if ans == 1:
            print(1)
            exit()

print(0)