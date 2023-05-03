n = int(input())

planets = []
for i in range(n):
    planets.append([i]+list(map(int,input().split())))
distances = []
for k in range(1,4):
    planets.sort(key=lambda x:x[k])
    for i in range(n-1):
        distances.append((abs(planets[i][k]-planets[i+1][k]),planets[i+1][0],planets[i][0]))
    distances.append((abs(planets[0][k]-planets[n-1][k]),planets[0][0],planets[n-1][0]))

distances.sort()

arr = [i for i in range(n)]

def find(x):
    if x != arr[x]:
        arr[x] = find(arr[x])
    return arr[x]

ans = 0
for i in distances:
    cost,x,y = i
    xx = find(x)
    yy = find(y)
    if xx != yy:
        if xx > yy:
            arr[xx] = yy
        else:
            arr[yy] = xx
        ans += cost

print(ans)