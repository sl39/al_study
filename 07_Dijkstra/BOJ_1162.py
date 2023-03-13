from heapq import heappop, heappush

n, m, k = map(int, input().split())
graph =[[] for i in range(n+1)]
for i in range(n):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

