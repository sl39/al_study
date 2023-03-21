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
