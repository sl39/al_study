T = int(input())
for i in range(T):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    graph = [[] for i in range(n+1)]
    for i in range(k):
        x,y = map(int,input().split())
        graph[x].append(y)
    w= int(input())

    