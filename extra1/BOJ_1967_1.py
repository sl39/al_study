from heapq import heappop, heappush


def dijkstra(start):
    q = []
    heappush(q, start)
    visited = [int(1e9)] * (N+1)
    visited[start[1]] = 0
    visited[0]= 0
    while q:
        cost, now = heappop(q)
        if visited[now] < cost:
            continue
        for z in edge[now]:
            total = cost + z[0]
            if total < visited[z[1]]:
                visited[z[1]] = total
                heappush(q, (total, z[1]))
    return visited


N = int(input())

edge = [[] for _ in range(N+1)]



for i in range(N-1):
    n, m, distance = map(int, input().split())
    edge[n].append([distance, m])
    edge[m].append([distance, n])


a = dijkstra([0, 1])

mx = max(a)
for i in range(1,N+1):
    if a[i] == mx:

        b = dijkstra([0,i])
        
        break
print(max(b))
