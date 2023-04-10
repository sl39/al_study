from collections import deque
# import sys

# for test in range(1,26):
#     sys.stdin = open(f'./test/{test}.in')

n,m = map(int,input().split())

mat = []
for i in range(m):
    mat.append(list(input().strip()))

X = []

for i in range(m):
    for j in range(n):
        if mat[i][j] == "S":
            start = (i,j)
        elif mat[i][j] == "E":
            end = (i,j)
        elif mat[i][j] == "X":
            X.append((i,j))
X = [start] + X + [end]
XX = len(X)
graph = [[n*m]*(XX) for i in range((XX))]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(node,idx):
    visited = [[0]*n for i in range(m)]
    q = deque()
    q.append(node)

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < m and 0<= ny < n and not visited[nx][ny] and mat[nx][ny] != "#":
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx,ny))
                if visited[nx][ny] != '.':
                    for k in range(XX):
                        if node != (nx,ny) and X[k] == (nx,ny):
                            graph[idx][k] = visited[nx][ny]
    return

for i in range(XX):
    bfs(X[i],i)
ans = 5 * n*m
arr = [0] * XX
def permu(depth,res,i):
    global ans

    if depth == XX-2:
        res += graph[i][XX-1]
        ans = min(res,ans)

        return
    
    if res >= ans:
        return
    
    for k in range(1,XX-1):
        if not arr[k]:
            arr[k] = 1
            permu(depth+1,res+graph[i][k],k)
            arr[k] = 0
    
    return


permu(0,0,0)
print(ans)
