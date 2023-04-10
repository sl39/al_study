TC = int(input())
arr = []
for i in range(TC):
    arr.append(int(input()))

mat =[[0]*(max(arr)+1) for i in range(5)]

mat[0][1] = 1

for i in range(2,max(arr)+1):
    mat[0][i] = mat[0][i-1] + mat[1][i-1] + mat[4][i-1] + mat[3][i-1] + mat[0][i-2]
    mat[1][i] = mat[0][i-1] + mat[4][i-1]
    mat[2][i] = mat[3][i-1]
    mat[3][i] = mat[0][i-1] + mat[2][i-1]
    mat[4][i] = mat[0][i-1] + mat[1][i-1]
for i in mat:
    print(i)