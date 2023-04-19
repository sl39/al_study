from heapq import heappop, heappush

n,m,x = map(int,input().split())
x = x-1
graph = [[]for i in range(n)]
for i in range(m):
    s,e,c = map(int,input().split())
    graph[s-1].append((c,e-1))
arr = [0] * n
def diks(start):
    q = []
    vis = [1e9] * n
    vis[start] = 0
    for i in graph[start]:
        heappush(q,i)
    while q:
        cost , now = heappop(q)
        if vis[now] < cost:
            continue
        vis[now] = cost
        for i in graph[now]:
            c , next = i
            if vis[next] >  c + cost:
                heappush(q,(c+cost,next))
    
    return vis

a = diks((x))
mx = 0
b = diks(i)
for i in range(n):
    if i != x:
        mx = max(b[x]+a[i],mx)

print(mx)
    


