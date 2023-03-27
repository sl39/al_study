# 기본적인 크루스칼로 해결한다
# 크루스칼은 간선들중 가장 적은 것 부터 연결하는데
# 사이클이 만들어지지 않도록한다

# 먼저 간선을 이고 있는 두 노드의 부모노드중 제일 작은 번호를 가져온다
# 그리고 두 노드의 번호가 같다면 이미 두 간선은 연결 되어 있는 것이므로
# 그 간선은 선택하지 않는다
# 다르다면 두 노드는 연결 되지 않은 것으로 생각하고 그 간선을 선택해준다
# 그리고 그 두 노드의 제일 작은 번호를 리스트에 저장한다


n,m = map(int,input().split())

arr= [i for i in range(n+1)]
tree = [0] * (n+1)
graph = []

for i in range(m):
    graph.append(list(map(int,input().split())))

graph.sort(key= lambda x: x[2])


def find(x):
    if x != arr[x]:
        arr[x] = find(arr[x])
    return arr[x]

path = []
for i in graph:
    a,b,c = i
    aa = find(a)
    bb = find(b)
    if aa != bb:
        if aa > bb:
            arr[aa] = bb

        else:
            arr[bb] = aa
        path.append(c)
print(sum(path)- max(path))
