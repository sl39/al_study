c, n = map(int,input().split())
mat = [[1e9]*(c+101) for i in range(n)]
adv = []
for i in range(n):
    adv.append(list(map(int,input().split())))
adv.sort(key= lambda x: x[1])



for i in range(n):
    cost, people = adv[i]
    for j in range(c+101):
        if j == people:
            mat[i][j] = min(mat[i-1][j],cost)
        elif j > people:
            mat[i][j] = min(mat[i-1][j] , mat[i][j-people] +cost,mat[i-1][j])
        else:
            mat[i][j] = mat[i-1][j]

print(min(mat[-1][c:]))