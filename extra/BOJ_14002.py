n = int(input())

arr = list(map(int,input().split()))

visited = [[1,[i]] for i in arr]

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j] and visited[j][0] >= visited[i][0]:
            visited[i] = [visited[j][0]+1 , visited[j][1]+[arr[i]]]
idx = 0
for i in range(n):
    if visited[i][0] > visited[idx][0]:
        idx = i

print(visited[idx][0])

print(*visited[idx][1])