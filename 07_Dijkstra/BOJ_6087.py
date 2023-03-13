from collections import deque
import sys
input = sys.stdin.readline
m,n = map(int,input().split())

mat = []
for i in range(n):
    mat.append(list(input().strip()))

C = []

for i in range(n):
    for j in range(m):
        if mat[i][j] == "C":
            C.append((i,j))

visited = [[0] * m for i in range(n)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

start, end = C
def bfs():
    q = deque([start])
    while q:
        x,y= q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            while 0<= nx< n and 0<= ny <m and mat[nx][ny] != "*":
                if not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] +1
                    q.append((nx,ny))
                nx += dx[i]
                ny += dy[i]
                

bfs()
print(visited[end[0]][end[1]] - 1)