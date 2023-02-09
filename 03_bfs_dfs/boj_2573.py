### 이게 시간초과가 안나서 놀랍다!
### 아이디어
### visited 행렬을 하나 만드는데
### N X M 행렬을 만든다
### 모든 요소를 [0]으로 일단 채우고
### 만약에 빙산이 모여 있는 행렬 mat의 i,j
### mat[i][j]에 값이 있다면
### visited[i][j] 의 값은 [값이 있다는 표시인 1, 그리고 상하좌우에 0의 개수] 로 정한다
### 그리고 mat 행렬안의 값의 개수와
### visited안의 아무 좌표를 잡고 이동하는 거리가 같으면
### 다음 작업을 하고
### 아니면 걸린 시간을 출력한다
### mat 행렬안의 값의 개수가 0이면
### 0을 출력한다


import sys
input = sys.stdin.readline
N, M = map(int,input().split())
mat = []
from collections import deque
for i in range(N):
    mat.append(list(map(int,input().split())))



dx = [1,-1,0,0]
dy = [0,0,1,-1]
t = 0
count = 1
while count:
    count = 0
    visited = [[[0] for _ in range(M)] for i in range(N)]
    for i in range(1,N):                                    
        for j in range(1,M):                            
            if mat[i][j]:                                   # mat 행렬안에 값이 있으면
                res = 0
                for k in range(4):
                    if mat[i+dx[k]][j+dy[k]] == 0:          # 값 주면에 0 이 있으면
                        res += 1                            # 그 수를 세고
                visited[i][j][0]  = 1                       # 값이 있다는 표시와
                visited[i][j].append(res)                   # 0의 개수를 추가 한다
                count += 1                                  # 그리고 mat 행렬 안에 값들을 셈함
                x = i
                y = j

    count2 = 0

    q = deque([[x,y]])
    while q:
        v = q.popleft()
        for i in range(4):
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]
            if visited[nx][ny][0]:                          # visited 행렬안에 값이 있는 아무 좌표를 잡고
                visited[nx][ny][0]  = 0
                count2 += 1                                 # 그 좌표를 시작으로 bfs 탐색을 통해 갈수 있는 좌표의 개수를 구함
                q.append([nx,ny])

    if count == count2:                                     # mat 행렬안에 값의 개수와 좌표가 갈수 있는 개수가 같으면 
        for i in range(1,N-1):                              # 빙하들을 녹임
            for j in range(1,M-1):
                if mat[i][j]:
                    if mat[i][j] <= visited[i][j][1]:
                        mat[i][j] = 0
                    else:
                        mat[i][j] -= visited[i][j][1]
        t += 1                                              # 그리고 시간을 젬
    else:                                                   # 아니면 두개 이상으로 나눠져 있다는 이야기이므로 while 문을 종료
        break
if count == 0:                                              # count = 0 이면 다 녹았다는 말이므로 0을 출력
    print(0)
else:                                                       # 아니면 얼마나 걸렸는지 출력
    print(t)


