from collections import deque
import sys
input = sys.stdin.readline
dx = [1,-1,0,0]
dy = [0,0,1,-1]

n,m = map(int,input().split())

mat = []
for i in range(n):
    mat.append(list(map(int,input().split())))

BBQ = []
for i in range(n):
    for j in range(n):
        if mat[i][j] == 2:
            BBQ.append((i,j))

cs = len(BBQ)
mx = 13*2500
def com(i,depth, res):
    global mx
    if depth == m:
        mx = min(mx,distance(res))
        return
    if i == cs:
        return
    com(i+1,depth+1, res + [BBQ[i]])
    com(i+1,depth,res)



def distance(res):
    q = deque(res)
    count = 0
    visited = [[0]*n for j in range(n)]
    for ch in res:
        a,b =ch
        visited[a][b] = -1
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<= nx < n and 0<= ny < n and not visited[nx][ny]:
                if visited[x][y] == -1:
                    visited[nx][ny] = 1
                else:
                    visited[nx][ny] = visited[x][y] + 1
                if mat[nx][ny] == 1:
                    count += visited[nx][ny]
                if count > mx:
                    return 13*2500
                q.append((nx,ny))
    return count

com(0,0,[])

print(mx)