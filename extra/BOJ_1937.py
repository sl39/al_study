import sys
sys.stdin = open("in.txt")

n = int(input())
mat = []
for i in range(n):
    mat.append(list(map(int,input().split())))

visited = [[-1]*n for i in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]
def dfs(x,y):
    if visited[x][y] == -1:
        visited[x][y] = 0
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<= nx < n and 0<= ny < n and mat[x][y] < mat[nx][ny]:
                visited[x][y] = max(dfs(nx,ny),visited[x][y])
    return visited[x][y] + 1


ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans,dfs(i,j))

print(ans)