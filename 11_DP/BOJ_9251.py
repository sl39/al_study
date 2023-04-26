a = input().strip()
b = input().strip()
aa = len(a)
bb = len(b)

mat = [[0]*aa for i in range(bb)]
if b[0] == a[0]:
    mat[0][0] = 1
for i in range(1,aa):
    if b[0] == a[i]:
        mat[0][i] = 1
    else:
        mat[0][i] = mat[0][i-1]
for i in range(1,bb):
    if b[i] == a[0]:
        mat[i][0] = 1
    else:
        mat[i][0] = mat[i-1][0]

for i in range(1,bb):
    for j in range(1,aa):
        if b[i] == a[j]:
            mat[i][j] = mat[i-1][j-1] + 1
        else:
            mat[i][j] = max(mat[i-1][j], mat[i][j-1])


print(mat[-1][-1])
