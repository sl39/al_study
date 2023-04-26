n = int(input())
arr = []
for i in range(n):
    s,e = map(str,input().split())
    s = 60*int(s[:2]) + int(s[2:])-10
    e = 60*int(e[:2]) + int(e[2:])+10
    arr.append((s,e))
arr.sort()
mx = 0
mx = max(mx,arr[0][0] - 600)
t = 0
front = 0
while t < n:
    if arr[front][0] <= arr[t][0] <= arr[front][1]:
        if arr[front][1] <= arr[t][1]:
            front = t
        elif arr[front][1] > arr[t][1]:
            pass
    else:
        mx = max(mx,arr[t][0]- arr[front][1])
        front = t
    
    t+= 1
mx = max(mx,22*60-arr[front][1])

print(mx)

