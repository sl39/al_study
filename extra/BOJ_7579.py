n,m = map(int,input().split())

marr =[0] + list(map(int,input().split()))
carr =[0]+ list(map(int,input().split()))

visited = [[0]*(sum(carr)+1) for i in range(n+1)]
cost =10000
for i in range(1,n+1):
    x,y = marr[i],carr[i]
    for j in range(1,sum(carr)+1):
        if j < y:
            visited[i][j] = visited[i-1][j]
        else:
            visited[i][j] = max(visited[i-1][j],visited[i-1][j-y]+x)
        
        if visited[i][j] >= m:
            cost= min(cost,j)


print(cost)