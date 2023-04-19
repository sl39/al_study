import sys
input = sys.stdin.readline
from heapq import heappop, heappush
def diks(t):
    q = []
    heappush(q,(mat[0][0],0,0))
    visited = [[1e9]* n for i in range(n)]
    visited[0][0] = mat[0][0]
    while q:
        cost, x, y = heappop(q)

        
        if x  ==n-1 and y == n-1:
            print(f"Problem {t}: ", end="")
            print(visited[-1][-1]) 
            return

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0<= ny < n and visited[nx][ny] == 1e9:
                if visited[nx][ny] > cost + mat[nx][ny]:
                    visited[nx][ny] =  cost + mat[nx][ny]
                    heappush(q,(cost+mat[nx][ny],nx,ny))
 


t = 1
while True:
    n = int(input())
    if n == 0:
        break
    mat = []
    for i in range(n):
        mat.append(list(map(int,input().split())))

    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    
    diks(t)
    t+= 1

