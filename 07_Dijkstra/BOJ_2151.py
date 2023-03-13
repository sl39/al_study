from collections import deque

n = int(input())
mat = []

for i in range(n):
    mat.append(list(input().strip()))

door = []

for i in range(n):
    for j in range(n):
        if mat[i][j] == "#":
            door.append((i,j))

dx = [0,0,-1,1]
dy = [1,-1,0,0]
# 튜플안에 (x,y,cnt,dir)


start, end = door
x,y = start
q = deque([])
for i in range(4):
    q.append((x,y,0,i))

while q:
    x,y,cnt,dir = q.popleft()
    
    nx = x + dx[dir]
    ny = y + dy[dir]
    while 0<= nx < n and 0<= ny < n and mat[nx][ny] != "*":
        if mat[nx][ny] == "!":
            if dir == 0 or dir == 1:
                q.append((nx,ny,cnt+1,2))
                q.append((nx,ny,cnt+1,3))
            else:
                q.append((nx,ny,cnt+1,0))
                q.append((nx,ny,cnt+1,1))
        
        if (nx,ny) == end:
            q = []
            break
        
        
        nx += dx[dir]
        ny += dy[dir]


print(cnt)