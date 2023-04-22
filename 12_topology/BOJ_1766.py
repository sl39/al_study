from heapq import heappop, heappush

n,m = map(int,input().split())

graph = [[] for i in range(n+1)]
indegree = [0]*(n+1)

for i in range(m):
    s,e = map(int,input().split())
    graph[s].append(e)
    indegree[e] += 1

q = []
for i in range(1,n+1):
    if not indegree[i]:
        heappush(q,i)

arr = []
while q:
    node = heappop(q)
    arr.append(node)
    for i in graph[node]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heappush(q,i)

print(*arr)