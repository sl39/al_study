from collections import deque
n,q = map(int,input().split())
mat = [[] for i in range(n+1)]
for i in range(n-1):
    a,b,c = map(int,input().split())
    mat[a].append((b, c))
    mat[b].append((a,c))

def bfs(k,i):
    visited = [0] * (n+1)
    q = deque([])
    for j in mat[i]:
        t,s = j
        visited[t] = s
        q.append(t)
    while q:
        node = q.popleft()
        for j in mat[node]:
            t,s = j
            if not visited[t]:
                visited[t] = min(visited[node],s)
                q.append(t)
    cnt = 0
    for j in range(1,n+1):
        if j == i:
            continue
        if visited[j] >= k:

            cnt += 1
    return cnt

for _ in range(q):
    k,i = map(int,input().split())
    print(bfs(k,i))