from collections import deque


n, w, l = map(int,input().split())
arr = list(map(int,input().split()))

truck = [0] * w
q = deque(truck)
t = 0
end = 0
while q:
    q.popleft()
    t += 1
    if end< n:
        if (sum(q) +  arr[end]) <= l:
            q.append(arr[end])
            end += 1
        else:
            q.append(0)

print(t)
