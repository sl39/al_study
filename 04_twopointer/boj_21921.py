### 누적합 비스무리하게 풀었음

N, X = map(int,input().split())
v = list(map(int,input().split()))
ls = [0] * (N - X + 1)
t = 1
ls[0] = sum(v[:X])
mx = ls[0]
for i in range(1, N - X + 1):
    a = ls[i-1] + v[X-1+i] - v[i-1]
    ls[i] = a
    if a == mx:
        t += 1
    elif a > mx:
        mx = a
        t = 1
if mx == 0:
    print("SAD")
else:
    print(mx)
    print(t)