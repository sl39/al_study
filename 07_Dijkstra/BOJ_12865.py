n,k = map(int,input().split())

item = [(0,0)]
for i in range(n):
    w,v = map(int,input().split())
    item.append((w,v))

item.sort()

knapsack = [[0]*(k+1) for i in range(n+1)]

for i in range(n+1):
    w,v = item[i]
    for j in range(0,k+1):
        if i == 0 or j == 0:
            pass
        elif j < w:
            knapsack[i][j] = knapsack[i-1][j]
        else:
            knapsack[i][j] = max(knapsack[i-1][j],knapsack[i-1][j-w]+v)

print(knapsack[n][k])

