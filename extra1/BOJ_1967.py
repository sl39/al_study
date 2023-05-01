from collections import deque

n = int(input())

graph =[[]for i in range(n+1)]
for i in range(n-1):
    s,e,c = map(int,input().split())
    graph[s].append((c,e))
    graph[e].append((c,s))

def dfs(start):
    q = deque([start])
    arr = [1e9] * (n+1)
    arr[start] = 0
    while q:
        node = q.popleft()
        for i in graph[node]:
            cost, nt = i
            if cost + arr[node] < arr[nt]:
                arr[nt] = cost+arr[node]
                q.append(nt)
    return arr
ans = 0
p = dfs(1)
mx = max(p[1:])
for i in range(1,n+1):
    if p[i] == mx:
        pp = dfs(i)
        ans = max(max(pp[1:]),ans)
        break

print(ans)