from collections import deque

n,m = map(int,input().split())

mat = []
for i in range(n):
    mat.append(list(map(int,input().split())))
virus = []


cnt = 3

for i in range(n):
    for j in range(m):
        if mat[i][j] == 2:
            virus.append((i,j))
            cnt += 1
        if mat[i][j] == 1:
            cnt += 1

nsafe = m*n

dx = [0,0,1,-1]
dy = [1,-1,0,0]



def bfs(res):
    
    global nsafe
    
    count = 0
    
    visited = [[0]*m for i in range(n)]
    
    for i in res:
        x = i//m
        y = i%m
        visited[x][y] = 1
        
    q =deque()
    
    for i in virus:
        q.append(i)

    while q:

        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0<= ny < m and mat[nx][ny] == 0 and visited[nx][ny] ==0:
                visited[nx][ny] = 1
                count += 1
                if nsafe <= count:
                    return
                q.append((nx,ny))
    nsafe = min(nsafe,count)
    


def comb(k,depth,res):
    
    if depth == 3:
        bfs(res)
        return
            
    if k == n*m:
        return
    if mat[k//m][k%m] == 0:
        comb(k+1,depth+1,res+[k])
    comb(k+1,depth,res)

comb(0,0,[])
print(m*n-nsafe-cnt)
