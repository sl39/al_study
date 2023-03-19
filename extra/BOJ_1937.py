# import sys
# sys.stdin = open("in.txt")

n = int(input())
mat = []
for i in range(n):
    mat.append(list(map(int,input().split())))

visited = [[1]*n for i in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]
def dfs(x,y,depth):

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<= nx < n and 0<= ny < n and mat[x][y] < mat[nx][ny] and visited[nx][ny] < depth+1:
                visited[nx][ny] = depth + 1
                dfs(nx,ny,depth+1)
        return 


for i in range(n):
    for j in range(n):
        dfs(i,j,visited[i][j])
ans =0 

for i in visited:
    ans = max(ans,max(i))

print(ans)