from collections import deque

n,m = map(int,input().split())
mat = []
for i in range(n):
    mat.append(list(map(int,input().split())))

fire = []
wall = []


for i in range(n):
    for j in range(m):
        if mat[i][j] == 2:
            fire.append((i,j))
        if mat[i][j] == 1:
            wall.append((i,j))
result = m*n
w = len(wall)
f = len(fire)
def com(i,res,depth):
    global result

    if depth == 3:
        visited = [[0]*m for i in range(n)]
        for j in res:
            x,y = j
            mat[x][y] = 1

        result = min(bfs(visited, 0), result)
        for j in res:
            x, y = j
            mat[x][y] = 0
        return

    if i == n*m:
        return

    if mat[i//m][i%m] == 0:
        com(i+1, res+[[i//m,i%m]], depth+1)
    com(i+1, res, depth)


dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(visited,cnt):
    q = deque(fire)
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0<= ny <m and mat[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                cnt += 1
                q.append(((nx,ny)))
            if cnt >= result:
                return n*m
    return cnt


com(0,[],0)
print(m*n-3- w-f-result)