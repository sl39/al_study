from heapq import heappop, heappush

n = int(input())

mat = []
for i in range(n):
    mat.append(list(input()))
q = []
total = 0

for i in range(n):
    for j in range(n):
        if ord(mat[i][j]) >= 97:
            mat[i][j] = ord(mat[i][j]) - 96
        else:
            mat[i][j] = ord(mat[i][j]) -38
        total += mat[i][j]
        heappush(q, (mat[i][j],i,j))


visited = [i for i in range(n)]

def parant(i):