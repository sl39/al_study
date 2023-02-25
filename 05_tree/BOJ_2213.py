# 아이디어
# 한 노드에 두개의 값을 설정하는데
# 하나는 그 노드를 방문한 노드와
# 다른 하나는 방문하지 않는 노드를 만든다
# 그리고 방문한 노드는 그 이전에 방문하지 않는 값에 현재 가중치를 더해줌
# 방문하지 않은 노드에는 이전 노드의 2개 값중에서 더 큰 값을 더해줌
# 길도 마찬가지


import sys
input = sys.stdin.readline




n = int(input())
arr = [0]
arr += list(map(int,input().split()))
tree = [[] for i in range(n+1)]
visited = [0] *(n+1)
value = [[0,0] for i in range(n+1)]
path = [[[]for i in range(2)] for j in range(n+1)]


for i in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)


# 노드 함수
def indep(node):
    visited[node] = 1
    value[node][0] += arr[node]
    path[node][0].append(node)


    for i in tree[node]:
        if not visited[i]:
            indep(i)



            # 부모 노드의 방문 값은 자식 노드의 방문하지 않는 값을 더해준다
            value[node][0] += value[i][1]

            # 부모 노드의 방문하지 않는 값은 자식 노드 둘중에 큰 값을 더해줌
            value[node][1] += max(value[i][0],value[i][1])


            # 길도 마찬가지로 해준다
            path[node][0] += path[i][1]
            if value[i][0] > value[i][1]:
                path[node][1] += path[i][0]
            else:
                 path[node][1] += path[i][1]
    return
indep(1)

if value[1][0] > value[1][1]:
    print(value[1][0])
    print(*sorted(path[1][0]))
else:
    print(value[1][1])
    print(*sorted(path[1][1]))