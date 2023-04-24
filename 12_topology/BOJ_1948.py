from heapq import heappop, heappush

n = int(input())
m = int(input())

graph = [[] for i in range(n+1)]
visited = [[0]*(n+1) for i in range(n+1)]
indegree = [0] * (n+1)
for i in range(m):
    s,e,cost = map(int,input().split())
    graph[s].append((cost,e))

    indegree[e] += 1

start, end = map(int,input().split())
q = []
heappush(q,(0,start))


dep = [[0,0] for i in range((n+1))] # 다리수, 비용
dep[start] =[0,0]



while q:
    total,node = heappop(q)
    total = -total
    for j in graph[node]:
        cost, i = j
        indegree[i] -= 1
        if indegree[i] == 0:
            if dep[i][1] < cost + dep[node][1]:
                dep[i][1] = cost + dep[node][1]
                dep[i][0] = dep[node][0] + 1
                heappush(q,(-dep[i][1],i))
            elif dep[i][1] == cost + dep[node][1]:
                dep[i][0] += dep[node][0]
                heappush(q,(-dep[i][1],i))

print(dep)