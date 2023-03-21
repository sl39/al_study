n = int(input())


arr = [i for i in range(n)]
graph = []
stars = []
for i in range(n):
    stars.append(list(map(float,input().split())))

for i in range(n-1):
    for j in range(i+1,n):
        x,y = stars[i]
        a,b = stars[j]
        dis = ((x-a)**2 + (y-b)**2)**(1/2)
        graph.append((dis,i,j))
    
graph.sort()

def find(x):
    if x != arr[x]:
        arr[x] = find(arr[x])
    return arr[x]


ans = 0

for i in graph:
    cost , a, b, = i
    aa = find(a)
    bb = find(b)
    if aa != bb:
        if aa > bb:
            arr[aa] =bb
        else:
            arr[bb] = aa
        ans += cost
print(ans)