#### 검색해서 아이디어를 차용
#### 이런게 투포인트였구나
#### 근데 시간이 많이 걸림
#### ab와 cd를 묶어서 더함
#### ab 리스트에는 a와 b 의 덧셈을 한 모든 경우의 수가 있고
#### cd 리스트에는 c와 d 의 덧셈을 한 모든 경우의 수가 있다
#### 그리고 각각의 리스트를 정렬하고
#### ab는 앞에서 부터, cd는 뒤에서 부터 더함
#### 그리고 합이 0이 되는 지점을 찾음
#### 만약에 합이 0이 되면 ab리스트에는 그 다음으로 검색해서 같은게 있는지 확인
#### cd리스트에는 그 다음걸 검색해서 같은게 있는지 확인
#### 그리고 각각 그 수를 카운트 해서 곱한걸 전체에 더함


import sys
input = sys.stdin.readline
n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

ab = []
cd = []
for i in range(n):
    for j in range(n):
        ## ab와 cd의 각각의 경우의수를 더한 리스트
        ab.append(arr[i][0] + arr[j][1])
        cd.append(arr[i][2] + arr[j][3])


## ab 와 cd 리스트를 정렬
ab.sort()
cd.sort()

## ab와 cd 의 길이
n = n*n


start = 0
end = n-1
cnt = 0

### start 가 n**2 보다 크거나 end가 0보다 작으면 끝
while start < n and end >= 0: 

    # 같은거 끼리 있는지 확인 하는 count 
    
    cnt1 = 1
    cnt2 = 1
    
    ### ab 와 cd 의 합이 0이면
    if ab[start] + cd[end] == 0:

        # ab의 다음값과 cd의 다음값(이전값) 을 알기 위해서 
        ns = start + 1
        ne = end - 1


        # 이전 값과 같다면

        while ns < n and ab[start] == ab[ns]:
        
            cnt1 += 1
            ns = ns+1

        while ne >=0 and  cd[end] == cd[ne]:
            cnt2 += 1
            ne = ne - 1
        
        ## 두개를 곱해서 cnt 에 더해줌
        cnt += cnt1*cnt2
        
        # start와 end 는 그 다음으로 넘김
        start = ns
        end = ne

    ## ab가 cd 가 더 크다면 cd를 더 줄여서 맞춤
    elif ab[start] + cd[end]> 0:
        end -= 1

    ## ab 가 더 작다면 ab를 늘임
    else:
        start += 1


print(cnt)
