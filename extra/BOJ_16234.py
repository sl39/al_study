import sys
input = sys.stdin.readline
from collections import deque
n , l ,r = map(int,input().split())
mat = []

for i in range(n):
    mat.append(list(map(int,input().split())))

dx = [1,0,-1,0]
dy = [0,1,0,-1]
test  = 0
def check():
    global test
    count = 0
    visited = [[0]*(n) for i in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                q = deque([(i,j)])
                cnt = 0
                nations = []
                while q:
                    x,y = q.popleft()
                    for dir in range(4):
                        nx = x + dx[dir]
                        ny = y + dy[dir]
                        if 0<= nx < n and 0<= ny < n and not visited[nx][ny] and l<= abs(mat[x][y]- mat[nx][ny]) <= r:
                            visited[nx][ny] = 1
                            cnt += mat[nx][ny]
                            q.append((nx,ny))
                            nations.append((nx,ny))
                            count += 1
                
                lenth = len(nations)
                if lenth:
                    value = cnt//lenth
                    for k in nations:
                        a,b = k
                        mat[a][b] = value
    if not count:
        print(test)
        exit()
    test += 1


while True:
    check()


