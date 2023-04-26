n = int(input())
arr = []
for i in range(n):
    s,e = map(int,input().split())
    arr.append((s,e))

arr.sort()

dp = [1] * n
for i in range(n):
    for j in range(i):
        if arr[i][1] > arr[j][1]:
            dp[i] = max(dp[j]+1,dp[i])


print(n-max(dp))



