from heapq import heappop, heappush

n,m = map(int,input().split())

graph = [[] for i in range(n+1)]
visited = [10*n] * (n+1)
path =[[i for i in range(1,n+1)]for i in range(n+1)]
visited[1] = 0
path[1] = [1]
for i in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

q = []
heappush(q,(0,1))
while q:
    x,y = heappop(q)

    if x > visited[y]:
        continue
    
    for i in graph[y]:
        cost, node = i
        res = visited[y] + cost
        if res < visited[node]:
            path[node] = path[y] + [node]
            visited[node] = res
            heappush(q,(res,node))

        # elif  cost == visited[node] and len(path[node]) > len(path[y])+1:
        #     path[node] = path[y] + [node]
        #     visited[node] = res
        #     heappush(q,(res,node))



print(n-1)
for i in range(2,n+1):
    print(path[i][-1],path[i][-2])