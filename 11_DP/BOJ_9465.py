TC = int(input())
for _ in range(TC):
    n = int(input())
    
    mat = []
    for i in range(2):
        mat.append(list(map(int,input().split())))
    
    if n == 1:
        print(max(mat[0][0],mat[1][0]))
        continue

    if n == 2:
        print(max(mat[0][0]+mat[1][1],mat[0][1]+mat[1][0]))
        continue
    cost = [[0]*n for i in range(2)]
    cost[0][0] = mat[0][0]
    cost[1][0] = mat[1][0]
    cost[0][1] = mat[1][0] + mat[0][1]
    cost[1][1] = mat[0][0] + mat[1][1]
    for i in range(2,n):
        cost[0][i] = mat[0][i] + max(cost[1][i-1],cost[0][i-2],cost[1][i-2])
        cost[1][i] = mat[1][i] + max(cost[0][i-1],cost[0][i-2],cost[1][i-2])
    
    mx = 0

    for i in range(2):
        for j in range(n-2,n):
            mx = max(mx,cost[i][j])
    
    print(mx)