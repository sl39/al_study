from collections import deque

n,m = map(int,input().split())
mat = []
for i in range(n):
    mat.append(list(map(int,input().split())))

visited = [[0]*m for i in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]




t= 1
for i in range(n):
    for j in range(m):
        if mat[i][j] == 1 and not visited[i][j]:
            q = [(i,j)]
            visited[i][j] = t

            q = deque(q)
            while q:
                x,y = q.popleft()
                for k in range(4):
                    nx = dx[k] + x
                    ny = dy[k] + y
                    if 0<= nx < n and 0<= ny < m and mat[nx][ny] and visited[nx][ny] == 0:
                        visited[nx][ny] = t
                        q.append((nx,ny))
            t += 1

arr = [[1e9] * (t) for i in range(t)]


def bridge(start):
    x,y = start
    for i in range(4):
        length = 0
        nx = x + dx[i]
        ny = y + dy[i]
        while 0<= nx < n and 0<= ny < m:
            if visited[nx][ny] == visited[x][y]:
                break

            if visited[nx][ny] == 0:
                length += 1
            elif visited[nx][ny] != visited[x][y]:
                if length <= 1:
                    break
                arr[visited[x][y]][visited[nx][ny]] = min(arr[visited[x][y]][visited[nx][ny]],length)
                break
            nx = nx + dx[i]
            ny = ny + dy[i]



for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:

            continue
        bridge((i,j))


visited=[]

for i in range(1,t):
    for j in range(1,t):
        if arr[i][j] != 1e9:
            visited.append((arr[i][j],i,j))

visited.sort()
arr = [i for i in range(t)]

def find(p):
    if p != arr[p]:
        arr[p] = find(arr[p])
    return arr[p]
res = 0
for i in visited:
    c,s,e = i
    ss = find(s)
    ee = find(e)
    if ee == ss:
        continue
    if ee > ss:
        arr[ee] = ss
    else:
        arr[ss] = ss
    res += c



if res == 0:
    print(-1)
else:
    print(res)