from collections import deque

n = int(input())
tree = [[] for i in range(n+1)]
for i in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

visited = [0]*(n+1)
visited[1] = 1
cnt = 0
def dfs(start):
    global cnt
    q = deque()
    q.append(start)
    while q:
        start = q.pop()
        count = 0

        for i in tree[start]:
            if not visited[i]:
                visited[i] = visited[start] + 1
                q.append(i)
                count += 1
        if count == (tree[start]):
            cnt += visited[start] -1

dfs(1)

if cnt % 2:
    print("Yes")
else:
    print("NO")