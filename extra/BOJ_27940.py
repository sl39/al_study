import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
arr = [0] * (n+1)


mys = 0
for i in range(m):
    x,y  = map(int,input().split())
    mys += y
    
    if mys > k:
        print(i+1,1)
        break
    
else:
    print(-1)
