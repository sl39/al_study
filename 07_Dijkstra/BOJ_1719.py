from heapq import heappop, heappush

n,m = map(int,input().split())


graph = [[] for i in range(n+1)]

for i in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))




def di(node):
    path = [[] for i in range(n+1)]
    visited = [int(1e9)] * (n+1)
    visited[node] = 0
    path[node] = [node]
    q = []
    heappush(q,(0,node))
    while q:
        cost, now = heappop(q)

        # 그냥 큐로 하면 되는줄 알았는데 우선순위 큐를 이용하는 거더라
        # 생각 보다 이것만 알면 되는데 이걸 몰라서 너무 헤멨다
        # 이것만 알면되는거 였다
        # 이걸 알아와서 공부를 하니 되더라
        
        if cost > visited[now]:
            continue
        for i in graph[now]:
            res = cost + i[0]
            if res < visited[i[1]]:
                visited[i[1]] = res
                heappush(q,(res,i[1]))
                path[i[1]] = path[now] + [i[1]]
    path[node] = ["-","-"]
    for i in range(1,n+1):
        print(path[i][1],end=" ")
    print()

for node in range(1,n+1):
    di(node)