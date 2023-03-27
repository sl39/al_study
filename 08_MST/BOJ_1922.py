#  BOJ_1647 와 비슷하게 하면 됨

n = int(input())
m = int(input())

arr = [i for i in range(n+1)]
graph = []

for i in range(m):
    a,b,c = map(int,input().split())
    graph.append((c,a,b))

graph.sort()

def find(x):
    if x != arr[x]:
        arr[x] = find(arr[x])
    
    return arr[x]

ans = 0
for i in graph:
    cost, a, b = i
    aa = find(a)
    bb = find(b)
    if aa != bb:
        if aa > bb:
            arr[aa] = bb
        else:
            arr[bb] = aa
        ans += cost
        
print(ans)