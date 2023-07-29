from collections import deque
n = int(input())
graph = [[] for i in range(n+1)]
for i in range(n):
    arr = list(map(int,input().split()))
    arr_l = len(arr)
    start = arr[0]
    for i in range((arr_l-1)//2):
        graph[start].append(([arr[2*i+1]],arr[2*i+2]))

def radius(go):
    visited = [0] * (n+1)
    visited[go] = 1
    q = deque([go])
    while q:
        node = q.popleft()
        for i in graph:
            
    
    mx = 0
    idx = 0
    for i in range(1,n+1):
        if mx < visited[i]:
            mx = visited[i]
            idx = i
    return (idx,mx)

print(radius(radius(1)[0])[1]-1)

