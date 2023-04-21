from collections import deque

n,m = map(int,input().split())
arr = [0] * (n+1)
year = [0] * (n+1)
graph =[[] for i in range(n+1)]

for i in range(m):
    s,e = map(int,input().split())
    graph[s].append(e)
    arr[e] += 1

q = []
for i in range(1,n+1):
    if arr[i] == 0:
        q.append((i,1))

q= deque(q)
while q:
    node,y = q.popleft()
    year[node] = y

    for i in graph[node]:
        arr[i] -= 1
        if arr[i] == 0:
            q.append((i,y+1))
year = year[1:]
print(*year)

