n,m = map(int,input().split())
arr = []
for i in range(n):
    arr.append(int(input()))

dp1 = [0] * m
dp2 = [m*m] * m
for i in range(1,n-1):
    for j in range(m+1):
        
    
    dp1 = dp2
    dp2 = [0] * m
