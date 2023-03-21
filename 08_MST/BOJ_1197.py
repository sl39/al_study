

v,e = map(int,input().split())
vroot = [i for i in range(v+1)]
graph = []

for i in range(e):
    a,b,c = map(int,input().split())
    graph.append((c,a,b))
    
graph.sort()

def find(s):
    if s != vroot[s]:
        vroot[s] = find(vroot[s])
    return vroot[s]

ans = 0
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
print(ans)