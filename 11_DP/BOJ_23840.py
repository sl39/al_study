n,m = map(int,input().split())
graph =[[1e9]*n for i in range(n)]
for i in range(m):
    s,e,c = map(int,input().split())
    graph[s-1][e-1] = c
    graph[e-1][s-1] = c
start, end = map(int,input().split())
start -= 1
end -= 1
p = int(input())
arr = list(map(int,input().split()))
for i in range(p):
    arr[i] -= 1

for i in range(n):
    for j in range(n):
        if i==j:
            continue
        for k in range(n):
            if i == k or j == k:
                continue
            graph[j][k] = min(graph[j][k],graph[j][i] + graph[i][k])


import sys
input = sys.stdin.readline

patha = (1<<start) | (1<<end)

dp = [[1e9]*n for i in range((1<<n))]

dp[(1<<start)][start] = 0

last = patha
for i in arr:
    last = last|(1<<i)



for i in range((1<<start),1<<n):
    for j in range(n):
        if dp[i][j] == 1e9:
            continue
        for k in range(n):
            if i&(1<<k) or graph[j][k] == 1e9:
                continue
            dp[i|(1<<k)][k] = min(dp[i|(1<<k)][k],dp[i][j]+graph[j][k])


mx = 1e9
for i in range(last,1<<n):
    if i&(last)== last:
        mx = min(mx, dp[i][end])


print(mx)