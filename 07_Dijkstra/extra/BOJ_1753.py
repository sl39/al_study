from heapq import heappop, heappush

v,e = map(int,input().split())
start = int(input())

visited = [300001] * (v+1)
graph = [[] for i in range(v+1)]
for i in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))

q = []
visited[start] = 0
heappush(q,(0,start))
while q:
    x,y = heappop(q)
    if visited[y] < x:
        continue
    for i in graph[y]:
        res = i[0] + x
        if visited[i[1]] > res:
            visited[i[1]] = res
            heappush(q,(res,i[1]))
for i in range(1,v+1):
    if visited[i] == 300001:
        print("INF")
    else:
        print(visited[i])