import sys
from collections import deque
input = sys.stdin.readline
def dfs(i):
    q = deque([i])
    arr = [0] * (V+1)
    while q:
        p = q.popleft()
        pl = len(mat[p])
        for k in range(pl):
            j,dis = mat[p][k]
            if not arr[j]:
                arr[j] = arr[p] + dis
                q.append(j)
    mx = 0
    print(arr)
    for jj in range(V+1):
        if jj == i:
            pass
        elif mx <= arr[jj]:
            mx = arr[jj]
            idx = jj
    return mx ,idx

V = int(input())
mat = [[] for i in range(V+1)]
for _ in range(V):
    arr = list(map(int,input().split()))
    lenth = len(arr)//2
    start = arr[0]
    for i in range(1,lenth):
        mat[start].append([arr[2*i-1],arr[2*i]])
        mat[arr[2*i-1]].append([start,arr[2*i]])
    

print(dfs(dfs(1)[1])[0])