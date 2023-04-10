n = int(input())

mat = []
for i in range(n):
    mat.append(list(map(int,input().split())))

arr = [0] *n

ans = 1e9

def dsf(start,res,depth):
    global ans
    if ans <= res:
  
        return
    
    if depth == n:
        ans = min(ans,res)
        return
    if depth == n-1:
        
        dsf(k,res+mat[start][k],depth+1)
    
    for j in range(n):
        if mat[start][j] != 0 and not arr[j] and j != k:
            arr[j] = 1
            dsf(j,res+mat[start][j],depth+1)
            arr[j] = 0

for k in range(n):
    dsf(k,0,0)
print(ans)