# 아이디어
# 1번 노드에서 가장 먼 거리에 있는 노드를 찾고
# 그리고 그 노드에서 가장 긴거리의 노드를 찾아
# 두 노드의 거리를 구한다


import sys
from collections import deque
input = sys.stdin.readline

# 거리를 구하는데, bfs 이용
def dfs(i):
    q = deque([i])
    arr = [0] * (V+1)


    while q:

        p = q.popleft()
        pl = len(mat[p])

        # 어떤 노드를 선택 했으면 그 노드와 연결된 노드와 거리를 이용함
        for k in range(pl):
            j,dis = mat[p][k]
            # arr[j] 가 비어 있다면 그 전 노드와 그 거리를 더해준다
            if not arr[j]:
                arr[j] = arr[p] + dis
                q.append(j)
    mx = 0

    # 그리고 그 arr 안에 최대값과 인덱스를 리턴해준다(시작 노드를 제외하고)
    for jj in range(V+1):
        if jj == i:
            pass
        elif mx <= arr[jj]:
            mx = arr[jj]
            idx = jj
    return mx ,idx



V = int(input())

# 각 노드와 그노드에 연결된 노드와 그에 대한 거리를 구할 리스트
mat = [[] for i in range(V+1)]


for _ in range(V):
    arr = list(map(int,input().split()))
    lenth = len(arr)//2
    start = arr[0]

    # 각 노드와 그 노드에 연결된 노드와 거리를 각각 저장
    for i in range(1,lenth):
        mat[start].append([arr[2*i-1],arr[2*i]])
        mat[arr[2*i-1]].append([start,arr[2*i]])
    
print(dfs(dfs(1)[1])[0])