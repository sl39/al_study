## do you wanna build the snowman~ 
## 눈덩이들을 정렬해놓고
## 모든 경우를 탐색하는데 두 점을 정해놓고
## 그 사에의 하나씩 경우를 줄여가면서 탐색



import sys
input = sys.stdin.readline

n = int(input())
snow = list(map(int,input().split()))

snow.sort()
i = 0
mn = 4000000001

for i in range(n-3):
    for j in range(i+3,n):
        a1 = snow[i] + snow[j]  ## 두 점을 정해놓고
        start = i+1             ## 그 사이를 탐색
        end = j-1
        while start < end:
            a2 = snow[start] + snow[end]
            mn = min(mn,abs(a2-a1))
            if a2 > a1:                 ## 만약 a2 가 더 크다면 큰쪽을 줄여 나가고
                end -= 1
            elif a2 < a1:               ## 아니라면 작은쪽을 키운다
                start += 1
            else:                       ## 만약 같다면 그냥 끝
                print(0)
                exit()
print(mn)