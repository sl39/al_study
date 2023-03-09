from heapq import heappop, heappush


n,m = map(int,input().split())

visited = [int(1e10)+1] *n
arr = list(map(int,input().split()))
graph = [[] for i in range(n)]

for i in range(m):
    start, end, cost = map(int,input().split())
    graph[start].append((cost,end))
    graph[end].append((cost,start))
q = []
visited[0] = 0
heappush(q,(0,0))
while q:
    dis, now = heappop(q)
    if visited[now] < dis:
        continue

    for i in graph[now]:
        res = visited[now] + i[0]
        if res < visited[i[1]] and (not arr[i[1]] or i[1]== n-1):
            visited[i[1]] = res
            heappush(q,(res,i[1]))

if visited[n-1] == int(int(1e10)+1):
    print(-1)
else:
    print(visited[n-1])