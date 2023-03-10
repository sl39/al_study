from heapq import heappop, heappush

node = int(input())
n = int(input())

graph = [[] for i in range(node+1)]
visited = [1e9+1] * (node + 1)
path = [[] for i in range(node+1)]
for i in range(n):
    s,e,c = map(int,input().split())
    graph[s].append((c,e))

start, end = map(int,input().split())
visited[start] = 0
path[start] = [start]

q = []
heappush(q,(0,start))
while q:
    x,y = heappop(q)
    if visited[y] < x:
        continue

    for i in graph[y]:
        res = x+i[0]
        if res < visited[i[1]]:
            visited[i[1]] = res
            heappush(q,(res,i[1]))
            path[i[1]] = path[y] + [i[1]]

print(visited[end])
print(len(path[end]))
print(*path[end])
