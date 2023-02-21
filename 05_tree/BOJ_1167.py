import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline
def dfs(i):
    sample = deepcopy(mat)
    q = deque([i])
    arr = [0] * (V+1)
    while q:
        p = q.popleft()
        for j in range(1,V+1):
            if sample[p][j]:
                if arr[j] < arr[p] + sample[p][j]:
                    arr[j] = arr[p] + sample[p][j]
                sample[p][j] = 0
                sample[j][p] = 0
                q.append(j)
    mx = 0
    for i in range(V+1):
        if mx < arr[i]:
            idx = i
            mx = arr[i]
    return mx,idx

V = int(input())
mat = [[0]*(V+1) for i in range(V+1)]
for _ in range(V):
    arr = list(map(int,input().split()))
    lenth = len(arr)//2
    start = arr[0]
    for i in range(1,lenth):
        mat[start][arr[2*i-1]] = arr[2*i]
        mat[arr[2*i-1]][start] = arr[2*i]


print(dfs(dfs(1)[1])[0])