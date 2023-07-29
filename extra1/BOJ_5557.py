n = int(input())
arr = list(map(int,input().split()))
mat = [[0]*(n-1) for i in range(21)]
mat[arr[0]][0] = 1
for i in range(1,n-1):
    for j in range(21):
        if mat[j][i-1]:

            if j+ arr[i] <= 20:
                mat[j+arr[i]][i] += mat[j][i-1]
            if j-arr[i] >= 0:
                mat[j-arr[i]][i] += mat[j][i-1]

print(mat[arr[n-1]][-1])