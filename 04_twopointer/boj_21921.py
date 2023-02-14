### 누적합 비스무리하게 풀었음

N, X = map(int,input().split())
v = list(map(int,input().split()))
ls = [0] * (N - X + 1)
t = 1


## 먼저 앞에 X 만큼 더한걸 맨처음 리스트에 넣어줌
ls[0] = sum(v[:X])
mx = ls[0]

for i in range(1, N - X + 1):

    ## 그리고 더한값에 i번째 에 더하고 맨앞에 있는걸 빼줌 
    a = ls[i-1] + v[X-1+i] - v[i-1]

    
    ls[i] = a

    if a == mx: ## 그리고 max 값과 ,그 값의 개수를 구함
        t += 1
    elif a > mx:
        mx = a
        t = 1
if mx == 0:
    print("SAD")
else:
    print(mx)
    print(t)