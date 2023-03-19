import sys
input = sys.stdin.readline



n,m = map(int,input().split())
mat = [[0]*(m+1)]
for i in range(n):
    mat.append([0] + list(map(int,list(input().strip()))))



for i in range(1,n+1):
    for j in range(1,m+1):
        mat[i][j] += mat[i][j-1]

for j in range(1,m+1):
    for i in range(1,n+1):
        mat[i][j] += mat[i-1][j]

t = 0
for i in range(1,n+1):
    for j in range(1,m+1):
        x = i+t
        y = j+t
        while x< n+1 and y < m+1:
            if mat[x][y] + mat[i-1][j-1] - mat[x][j-1] - mat[i-1][y] == (t+1)**2:
                t += 1
                x += 1
                y += 1
            else:
                break
print(t**2)