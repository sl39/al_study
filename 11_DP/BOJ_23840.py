import sys
input =sys.stdin.readline

from heapq import heappop, heappush


n,m = map(int,input().split())
graph =[[]for i in range(n)]
for i in range(m):
    s,e,c = map(int,input().split())
    graph[s-1].append((e-1,c))
    graph[e-1].append((s-1,c))
start, end = map(int,input().split())
start -= 1
end -= 1
p = int(input())
arr = list(map(int,input().split()))
arr= [start] + arr + [end]
for i in range(1,p+1):
    arr[i] -= 1


def diks(start):
    k = [1e9]*(n)
    k[start] = 0
    q = []
    heappush(q,(0,start))
    while q:
        cost, node = heappop(q)
        if k[node] < cost:
            continue
        for i in graph[node]:
            x,c = i
            if cost + c < k[x]:
                k[x] = cost+c
                heappush(q,(k[x],x))
    return k


gogo = diks(start)

pp = [[0]*(p+2) for i in range(p+2)]
for i in range(p+2):
    ls = diks(arr[i])
    
    for j in range(p+2):
        pp[i][j] = ls[arr[j]]

dp = [[1e9]*(p+2) for i in range(1<<(p+2))]

dp[(1<<0)|(1<<(p+1))][0] = 0
for i in range((1<<0)|(1<<(p+1)),1<<(p+2)):
    for j in range(0,p+1):
        if i&(1<<j) == 0:
            continue

        for k in range(p+2):
            if i&(1>>k) or pp[j][k] == 0:
                continue
            dp[i|(1<<k)][k] = min(dp[i|(1<<k)][k] , dp[i][j] + pp[j][k])

mx = 1e9

for i in range(1,p+1):
    mx = min(dp[1<<(p+2)-1][i]+pp[i][p+1],mx) 

print(mx)