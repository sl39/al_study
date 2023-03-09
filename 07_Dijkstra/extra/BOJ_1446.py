n,d, = map(int,input().split())
dp = [i for i in range(10001)]
for i in range(n):
    start, end, dis = map(int,input().split())
    if dp[end] > dp[start] + dis:
        dp[end] = dp[start] + dis
    
print(dp[50])