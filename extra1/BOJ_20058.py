from collections import deque


N,M = map(int,input().split())

mat = []
for i in range(1<<N):
    mat.append(list(map(int,input().split())))
arr = list(map(int,input().split()))



def rotations(start,end,xstart,ystart,L):
    visited = [[0]*(1<<L) for i in range(1<<L)]
    for i in range(start,end):
        for j in range(xstart,ystart):
            visited[j-xstart][end-1-i] = mat[i][j]
    
    for i in range(start,end):
        for j in range(xstart,ystart):
            mat[i][j] = visited[i-start][j-xstart]

def binary(start,end,xstart,ystart,L):
 
    if end-start == 1<<L and ystart-xstart== 1<<L:
        rotations(start,end,xstart,ystart,L)

        return
    
    if end-start < 1<<L or ystart-xstart < 1<<L:
        return

    mid = (start+end)//2
    mida = (xstart+ystart)//2

    binary(start,mid,mida,ystart,L)
    binary(mid,end,xstart,mida,L)
    binary(start,mid,xstart,mida,L)
    binary(mid,end,mida,ystart,L)

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def melt():
    ice = []


    for i in range(1<<N):
        for j in range(1<<N):
            cnt = 0
            for k in range(4):
                nx = dx[k] + i
                ny = dy[k] + j
                if 0<= nx < 1<<N and 0<= ny < 1<<N:
                    if mat[nx][ny]:
                        cnt += 1
                    
            if cnt < 3:
                ice.append((i,j))
    for i in ice:
        x,y = i
        if mat[x][y]:
            mat[x][y] -=1


def bfs(i,j):
    global res,mx
    res += mat[i][j]
    cnt = 1
    visited[i][j] = 1
    q = deque([(i,j)])
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < 1<<N and 0<= ny < 1<<N and visited[nx][ny] ==0 and mat[nx][ny]:
                visited[nx][ny] = 1
                res += mat[nx][ny]
                cnt += 1
                q.append((nx,ny))
    mx = max(cnt,mx)




for L in arr:
    binary(0,1<<N,0,1<<N,L)
    melt()



visited = [[0]*(1<<N) for i in range(1<<N)]
res = 0
mx = 0

for i in range(1<<N):
    for j in range(1<<N):
        if visited[i][j] == 0 and mat[i][j]:
            bfs(i,j)

print(res)
print(mx)








