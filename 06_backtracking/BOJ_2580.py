import sys
input = sys.stdin.readline


mat = []
for i in range(9):
    mat.append(list(map(int,input().split())))

visited = [9]* 10
zero = []
for i in range(9):
    for j in range(9):
        if mat[i][j] > 0:
            visited[mat[i][j]] -= 1
        if mat[i][j] == 0:
            zero.append((i,j))

zero_visited = [0] *len(zero)
dx = [0,1,-1,0,0,1,1,-1,-1]
dy = [0,0,0,1,-1,1,-1,1,-1]

count = 0
res = 0
def sudoku(k):
    global count,res
    if k == len(zero):
        a = check(mat)

        if a:
            count = 1
            for i in mat:
                print(*i)
            exit(0)
        return
    if count == 1:
        return

    for i in range(1,10):
        if visited[i] and not zero_visited[k]:
            x,y = zero[k]
            if not check_v(x,y,i):
                zero_visited[k] = 1
                visited[i] -= 1
                mat[x][y] = i
                sudoku(k+1)
                visited[i] += 1
                mat[x][y] = 0
                zero_visited[k] = 0


def check_v(x,y,i):
    cnt = 0
    if i in mat[x]:
        cnt = 1
        return cnt
    for j in range(9):
        if i == mat[j][y]:
            cnt = 1
            return cnt
    return cnt



def check(mat):
    cnt = 0
    for i in range(3):
        for j in range(3):
            x = 1 + i*3
            y = 1 + j*3
            res = []
            for k in range(9):
                nx = x + dx[k]
                ny = y + dy[k]
                res.append(mat[nx][ny])
            if len(set(res)) != 9:
                cnt = 1
                break
    if cnt:
        return 0
    else:
        return 1


sudoku(0)
