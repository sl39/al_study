

n,m = map(int,input().split())

arr = []


for i in range(m+1):
    s,e,c = map(int,input().split())

    arr.append((c,s,e))




def find(x,visited):
    if x != visited[x]:
        visited[x] = find(visited[x],visited)
    return visited[x]

def union(ls,start):
    visited = [i for i in range(n+1)]
    cost = start
    for i in ls:
        c,x,y = i

        xx = find(x,visited)
        yy = find(y,visited)
        if xx != yy:
            if xx > yy:
                visited[xx] = yy
            else:
                visited[yy] = xx
            if c == 0:
                cost += 1
    return cost

arr.sort()
x = union(arr,0)
arr.sort(reverse=True)
y = union(arr,0)
print(abs(y**2 - x**2))
