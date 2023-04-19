

v,e = map(int,input().split())

# 자신과 연결된 노드 중에서 노드 번호가 가장 작은걸
# 1,2 번 노드 연결 되어있다
# vroot[1] = 1
# vroot[2] = 1



graph = []

for i in range(e):
    a,b,c = map(int,input().split())
    graph.append((c,a,b))

graph.sort()



def find(s):

    if s != vroot[s]:
        vroot[s] = find(vroot[s])
    return vroot[s]

vroot = [i for i in range(v+1)]
ans = 0

# Union 과정
for i in graph:
    cost, a, b = i
    aa = find(a)
    bb = find(b)
    if aa != bb:
        if aa > bb:
            vroot[aa] = bb
        else:
            vroot[bb] = aa
            
        ans += cost
    elif aa == bb:
        pass

print(ans)

# 정점들을 연결하는데
# 간선들의 가중치의 최솟값들을 차례대로 연결 시켜주는데
# 사이클이 돌지 않게 연결 시켜준다