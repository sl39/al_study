from collections import deque

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
q = deque([start])



dep = [0]*(n+1) # 비용
bridge = [[] for i in range(n+1)]

dep[start] =0

while q:
    node = q.popleft()
    
    for j in graph[node]:
        cost, i = j
        indegree[i] -= 1
        
        if dep[i] < cost + dep[node]:
            dep[i]= cost + dep[node]


            bridge[i] = [node]

        elif dep[i] == cost + dep[node]:
            bridge[i].append(node)

        if indegree[i] == 0:
            q.append(i)

q = deque([end])
path  = set()
while q:
    now = q.popleft()
    for i in bridge[now]:
        if (now,i) not in path:
            path.add((now,i))
            q.append(i)

print(dep[end])
print(len(path))
