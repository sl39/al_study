from collections import deque
n = int(input())
arr = [1000 for i in range(2*n+1)]
arr[1] = 0
q = deque([1])
while q:
    node = q.popleft()
    if node -1 >= 0:
        if arr[node-1] > arr[node] + 1:
            arr[node-1] = arr[node] + 1
            q.append(node-1)
    for i in range(2,n+1):
        if node*i > 2*n:
            break
        if arr[node*i] > arr[node] + i:
             arr[node*i] = arr[node] + i
             q.append(node*i)
print(arr[n])

