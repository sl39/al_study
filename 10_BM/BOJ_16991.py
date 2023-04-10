n = int(input())
graph = [[0]*n for i in range(n)]
arr = [0] * n
cities = []
for i in range(n):
    cities.append(list(map(int,input().split())))

for i in range(n-1):
    for j in range(1,n):
        graph[i][j] = ((cities[i][0] - cities[j][0])**2 +(cities[i][1] - cities[j][1])**2) **(1/2)
        graph[j][i] = ((cities[i][0] - cities[j][0])**2 +(cities[i][1] - cities[j][1])**2) **(1/2)


ans = 1e9
def dfs(depth,res,start,k):
    global ans
    if depth == n:
        ans = min(res,ans)
        return

    if res >= ans:
        return

    if depth == n-1:
        dfs(depth+1, res+graph[start][k], start,k)
        return

    for i in range(n):
        if i != k and not arr[i]:
            arr[i] = 1
            dfs(depth+1, res + graph[start][i], i, k)
            arr[i] = 0

dfs(0, 0, 0, 0)



print(ans)