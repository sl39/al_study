import sys
input = sys.stdin.readline

mat = []
for i in range(9):
    mat.append(list(map(int,list(input().strip()))))

blank = []

for i in range(9):
    for j in range(9):
        if mat[i][j] == 0:
            blank.append((i,j))



def check_col(x,num):
    for i in range(9):
        if mat[x][i] == num:
            return 0
    return 1
def check_row(y,num):
    for i in range(9):
        if mat[i][y] == num:
            return 0
    return 1


def check_9(x,y,num):
    nx = x//3* 3
    ny = y//3* 3
    for i in range(3):
        for j in range(3):
            if mat[nx+i][ny+j] == num:
                return 0
    return 1

def sudoku(t):
    if t == len(blank):
        for i in range(9):
            for j in range(9):
                print(mat[i][j], end="")
            print()
        exit(0)

    for a in range(1,10):
        x,y = blank[t]
        if check_col(x,a) and check_row(y,a) and check_9(x,y,a):
            mat[x][y] = a
            sudoku(t+1)
            mat[x][y] = 0

sudoku(0)
