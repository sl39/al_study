from collections import deque
from copy import deepcopy
mat = []
for i in range(3):
    mat.append(list(map(int,input().split())))
result = [[1,2,3],[4,5,6],[7,8,0]]

dit = dict()

st = ""
zero = (0,0)
for i in range(3):
    for j in range(3):
        st += str(mat[i][j])
        if mat[i][j] == 0:
            zero = (i,j)
dit[st] = True
def findB(mat,zero):
    global result
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]
    if mat == result:
        return 0
    q = deque()
    q.append((mat,zero,0))
    while q:
        arr, zero, cnt = q.popleft()
        x,y = zero
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < 3 and 0<= ny < 3:
                nextArr = deepcopy(arr)

                nextArr[nx][ny] , nextArr[x][y] = nextArr[x][y] , nextArr[nx][ny]

                if nextArr == result:
                    return cnt + 1
                else:
                    st = ""
                    for i in range(3):
                        for j in range(3):
                            st += str(nextArr[i][j])
                    if st in dit:
                        pass
                    else:
                        dit[st] = True
                        q.append((nextArr,(nx,ny),cnt+1))
    return -1

                
print(findB(mat,zero))     


