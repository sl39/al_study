import sys
input = sys.stdin.readline

n, k = map(int,input().split())
mat = []
for i in range(n):
    mat.append(list(map(int,input().split())))
arr = [0] * n
arr[k] = 1
ans = 10001

for i in range(n):
    for j in range(n):
        if i==j:
            continue
        for l in range(n):
            if l == j or i == l:
                continue
            r = mat[j][i] + mat[i][l]
            if r < mat[j][l]:
                mat[j][l] = r


def dfs(start,res,depth):
    global ans
    if depth == n:
        ans = min(ans,res)
        return
    
    if ans <= res:
        return
    
    for i in range(n):
        if not arr[i] and i!= start:
            arr[i] = 1
            dfs(i,res+mat[start][i],depth+1)
            arr[i] = 0
dfs(k,0,1)
print(ans)


