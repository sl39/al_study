TC =int(input())
    

def find(depth,cnt,next):
    global res
    
    if n == depth:
        res = min(res,cnt+mat[next][0])
        return
    
    for i in range(1,n):
        if mat[next][i] != 0:
            if arr[i] == 0:
                arr[i] = 1
                find(depth+1, cnt+mat[next][i],i)
                arr[i] = 0

for T in range(1,TC+1):
    n = int(input())
    mat = []
    for i in range(n):
        mat.append(list(map(int,input().split())))
    res = 5000
    arr = [0]* n
    for j in range(n):
        arr[j] = 1
        find(1,mat[0][j],j)
        arr[j] = 0
    print(f'#{T}',end=" ")
    print(res)
    