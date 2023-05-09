n = int(input())
arr = list(map(int,input().split()))

ans = 1
t = 1

while t < n:
    if arr[t-1] <= arr[t]:
        ans += 1
    
    t += 1

print(ans)