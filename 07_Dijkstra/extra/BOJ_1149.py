n = int(input())
mat = []
for i in range(n):
    mat.append(list(map(int,input().split())))

arr = [mat[0]]
for i in range(1,n):
    red = min(arr[-1][1],arr[-1][2]) + mat[i][0]
    green = min(arr[-1][0],arr[-1][2]) + mat[i][1]
    blue = min(arr[-1][1],arr[-1][0]) + mat[i][2]
    arr.append([red,green,blue])

print(min(arr[-1]))