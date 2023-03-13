from heapq import heappop, heappush


n,m = map(int,input().split())

mat = []
for i in range(n):
    mat.append(list(input().strip()))

for i in range(n):
    for j in range(m):
        if mat[i][j] == "S":
            S = (0,0,i,j)
        if mat[i][j] == "F":
            F = (i,j)
        
visited = [[0]*m for i in range(n)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]
def path():
    q = []
    heappush(q,S)
    while q:
        g,gs,x,y =  heappop(q)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < n and 0<= ny < m and not visited[nx][ny]:
                gcnt = g
                gscnt = gs
                if nx == F[0] and ny == F[1]:
                    visited[nx][ny] = (gcnt,gscnt)
                    return 
                if mat[nx][ny] == "g":
                    gcnt += 1
                    visited[nx][ny] = 1
                    heappush(q,(gcnt,gscnt,nx,ny))
                else:
                    for j in range(4):
                        nnx = nx + dx[j]
                        nny = ny + dy[j]
                        if 0<= nnx < n and 0<= nny < m and mat[nnx][nny] == "g":
                            gscnt += 1
                            break
                heappush(q,(gcnt,gscnt,nx,ny))
                visited[nx][ny] = 1

path()
print(*visited[F[0]][F[1]])