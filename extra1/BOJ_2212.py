n = int(input())
k = int(input())
arr =list(map(int,input().split()))
if n<=k:
    print(0)
else:

    arr.sort()
    visited = []
    for i in range(1,n):
        visited.append(arr[i]-arr[i-1])
    visited.sort(reverse=True)
    
    print(sum(visited[k-1:]))