n,m = map(int,input().split())

arr = []
t = 0
while 2**t <= n:
    if 2**t&n:
        arr.append(0)
    else:
        arr.append(1)
    
    t += 1

k = 0
while 2**k <= m:
    k += 1
    arr.append(1)

res = []
while m > 0:
    if m >= 2**(k-1):
        m -= 2**(k-1)
        res.append(k-1)
    k -= 1

res.sort()
ans = 0
s = 0
e = 0
for i in range(len(arr)):
    if arr[i] == 1 and s == res[e]:
        e += 1
        ans += 2**i
    if arr[i] == 1:
        s += 1
    if len(res) == e:
        break

print(ans)