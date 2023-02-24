from collections import deque


n = int(input())
arr = [0]
arr =arr + list(map(int,input().split()))

mat = [[]for i in range(n+1)]
for i in range(n-1):
    a,b = map(int,input().split())
    mat[a].append(b)
    mat[b].append(a)
visited = [0]*(n+1)
stack = [1]
nodes = [[] for i in range(n+1)]

while stack:
    p = stack.pop()
    for i in mat[p]:
        if not visited[i]:
            visited[i] = p
            nodes[p].append(i)
            stack.append(i)
visited[1] = 0

leafnode= deque([])
for i in range(2,n+1):
    if not nodes[i]:
        leafnode.append(i)



tree = [[0,0] for i in range(n+1)]
while leafnode:
    i = leafnode.popleft()
    if i == 1:
        pass
    else:
        if not nodes[i]:
            tree[i] = [arr[i],0]
            tree[visited[i]][0] = max(tree[i][1] + tree[visited[i]][0]+arr[visited[i]],tree[visited[i]][0]+arr[visited[i]])
        else:
            tree[visited[i]][0] = max(tree[i][1] + tree[visited[i]][0]+arr[visited[i]],tree[visited[i]][0]+arr[visited[i]])
            tree[visited[i]][1] = max(tree[visited[i]][1]+tree[i][1],tree[visited[i]][1]+tree[i][0],tree[visited[i]][1])
        leafnode.append(visited[i])
        
print(tree)