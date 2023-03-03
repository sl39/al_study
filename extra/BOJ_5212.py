r,c = map(int,input().split())

mat = [["."]*(c+2)]

for i in range(r):
    mat.append(["."]+list(input().rstrip())+["."])
mat.append(["."]*(c+2))

land = []

dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(r+2):
    for j in range(c+2):
        if mat[i][j] == "X":
            count = 0
            for k in range(4):
                nx = dx[k] + i
                ny = dy[k] + j
                if mat[nx][ny] == ".":
                    count += 1
            if count > 2:
                land.append((i,j))


for i in land:
    x,y = i
    mat[x][y] = "."


row1 = r
col1 = c 
row2 = 0
col2 = 0
for i in range(r+2):
    for j in range(c+2):
        if mat[i][j] == "X":
            if i < row1:
                row1 = i
            if i > row2:
                row2 = i
            if j < col1:
                col1 = j
            if j > col2:
                col2 = j

for i in range(row1, row2 +1):
    print("".join(mat[i][col1:col2+1]))
