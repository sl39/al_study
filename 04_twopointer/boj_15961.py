## 초밥 먹고 싶다


## 아이디어
## 처음 k개 만큼 종류의 개수를 결과에 더해준다
## 그리고 슬라이딩 윈도우를 진행하면서
## 초밥의 가짓수를 더해주거나 빼준다
## 만약에 초밥에 쿠폰초밥이 없다고 하면 cnt+= 1
## 없으면 그냥 cnt 와 최대값을 비교해서 max 값 출력
## 




import sys
from collections import deque

input = sys.stdin.readline

N, D, K, C = map(int, input().split())

check = [0] * (D+1)

sushi = []
for i in range(N):
    sushi.append(int(input()))


sushi = sushi + sushi[:K-1]    

res = []
cnt = 0
mx = 0

stack = deque([])
for k in range(len(sushi)):
    if check[sushi[k]] == 0:            ### 아직 먹지 않은 초밥이라면 cnt += 1한다
        cnt += 1
    check[sushi[k]] += 1                ### 그리고 먹은 거 더해주고
    stack.append(sushi[k])              ## 스택? 에 더해준다 생각해보니 큐더라

    if k<K-1:                           ## 먹어야하는 초밥 접시수 바로 전까지 계속 더해준다
        continue

    if check[C] == 0:                   ## 만약 쿠폰초밥이 가짓수에 안들어 간다면
        mx = max(mx,cnt+1)              ## max 값과 cnt += 1 을 더해줘서 비교
    else:
        mx = max(mx,cnt)                ## 아니면 그냥 비교

    a = stack.popleft()                 ## 그리고 하나씩 빼준다
    if check[a] == 1:                   ## 어떤 초밥의 먹은 접시수가 1개면 cnt -= 1
        cnt -= 1

    check[a] -= 1                       ## 그리고 체크에서 -= 1

print(mx)