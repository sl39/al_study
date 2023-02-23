import sys
sys.stdin = open("input.txt")



# def parents(x):
#     ls = [x]
#     while x > 0:
#         x = (x+k-2)//k
#         ls.append(x)
#     return ls

import sys
input = sys.stdin.readline

def find(x,y):
    cnt = 0
    while x!=y:
        if x>y:
            x=(x+k-2)//k
            cnt += 1
        else:
            y=(y+k-2)//k
            cnt += 1
    return cnt

n,k,q =map(int,input().split())
for i in range(q):
    x,y = map(int,input().split())
    if k == 1:
        print(abs(x-y))
    else:
        print(find(x,y))

    # a = parents(x)
    # b = parents(y)

    # cnt = 1
    # la = len(a)
    # lb = len(b)
    # while a[-cnt] == b[-cnt]:

    #     if cnt == min(la,lb):
    #         cnt += 1
    #         break
    #     else:
    #         cnt += 1
    # pp = a[-cnt+1]
    # print(la+lb- 2*cnt+2)
    
    