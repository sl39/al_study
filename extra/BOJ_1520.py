n,m = map(int,input().split())
mat = []
for i in range(n):
    mat.append(list(map(int,input().split())))

dx = [0,0,-1,1]
dy = [1,-1,0,0]
visited = [[-1]*m for i in range(n)]

start = (0,0)

def dfs(start):

    if start == (n-1,m-1):
        return 1
    
    x,y = start
    if visited[x][y] == -1:
        visited[x][y] = 0

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<= nx < n and 0<= ny < m and mat[nx][ny] < mat[x][y]:
                visited[x][y] += dfs((nx,ny))
    return visited[x][y]

print(dfs(start))