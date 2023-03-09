from heapq import heappop, heappush

n,m = map(int,input().split())

graph = [[] for i in range(n+1)]

for i in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

visited = [int(1e9)] *(n+1)
visited[0] = 0


q = []
heappush(q,(0,1))
while q:
    cost, now = heappop(q)
    if visited[now] < cost:
        continue
    for i in graph[now]:
        res = cost + i[0]
        if res < visited[i[1]]:
            visited[i[1]] = res
            heappush(q,(res,i[1]))


print(visited[n])