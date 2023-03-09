
from collections import deque
n, m, k, x =map(int,input().split())
arr = [[] for i in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    arr[a].append(b)
res = []

visited = [0] *(n+1)
q = deque([x])
while q:
    p = q.popleft()
    for j in arr[p]:
        if not visited[j]:
            visited[j] = visited[p] + 1
            q.append(j)
            if visited[j] == k and j!= x:
                res.append(j)
if res:
    res.sort()
    for i in res:

        print(i)
else:
    print(-1)