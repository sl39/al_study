import sys
input = sys.stdin.readline

from heapq import heappop,heappush

n,m,t,d = map(int,input().split())

mat = []
for i in range(n):
    mat.append(list(input().strip()))
def alpha(s):
    if s.isupper():
        ans  = ord(s) - ord("A")
    else:
        ans = ord(s) - ord("a") + 26
    return ans

start = (0,0)
for i in range(n):
    for j in range(m):
        mat[i][j] = alpha(mat[i][j])

go = [[100000]*m for i in range(n)]
back = [[100000]*m for i in range(n)]



dx = [1,-1,0,0,1,1,-1,-1]
dy = [0,0,1,-1,1,-1,1,-1]

q = []
heappush(q,(0,0,0))

while q:
    c,x,y, = heappop(q)
    if go[x][y] <= c:
        continue
    
    go[x][y] = c
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < n and 0<= ny < m:
            a = mat[nx][ny]-mat[x][y]
            if abs(a) <= t:
                if a > 0:
                    cost = a**2 + c
                    heappush(q,(cost,nx,ny))
                else:
                    cost = 1 + c
                    heappush(q,(cost,nx,ny))


q = []
heappush(q,(0,0,0))

while q:
    c,x,y, = heappop(q)
    if back[x][y] <= c:
        continue
    
    back[x][y] = c
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < n and 0<= ny < m:
            a = mat[nx][ny]-mat[x][y]
            if abs(a) <= t:
                if a >= 0:
                    cost = 1 + c
                    heappush(q,(cost,nx,ny))
                else:
                    cost = a**2 + c
                    heappush(q,(cost,nx,ny))





for i in range(n):
    for j in range(m):
        go[i][j] += back[i][j]
    
mx = 0
for i in range(n):
    for j in range(m):
        if mx < mat[i][j] and go[i][j] <= d:
            mx = mat[i][j]
            
            
print(mx)