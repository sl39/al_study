from collections import deque


r,c = map(int,input().split())
mat = []
for i in range(r):
    mat.append(list(input().strip()))

n = int(input())
sp = list(map(int,input().split()))

cnt = 0
for i in range(r):
    for j in range(c):
        if mat[i][j] == "x":
            cnt += 1



def bk(k):
    global cnt
    h = r - sp[k]
    print(h)
    if k%2:
        t = c -1
        while mat[h][t] == '.':
            t -= 1

    
    else:
        t = 0
        while mat[h][t] == '.':
            t += 1
    mat[h][t] = '.'
    cnt -= 1


dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(i,j,visited):
    if i == r-1:
        flag = 1
    else:
        flag = 0
    count = 0
    
    q = [(i,j)]
    q = deque(q)
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < r and 0<= ny < c and mat[nx][ny] == "x" and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx,ny))
                count += 1

    if count == cnt:
        return 1
    
    if flag:
        return 1
    return 0

def down():
    visited = [[0]*c for i in range(r)]
    for i in range(r-1,-1,-1):
        for j in range(c-1,-1,-1):
            if mat[i][j] == 'x' and visited[i][j] == 0:
                if bfs(i,j,visited) == 1:
                    continue
                
                