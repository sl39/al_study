### 아이디어?
### 먼저 소수 리스트를 만든다
### 그리고 n1,n2... 각각에 대해 소수들의 합이 소수가 되는 것을 확인한다
### 그리고 그중 최대값을 이용해서 최대값에 맞춰서 다른것들을 슬라이딩 윈도우?를 한다
### 그리고 그 최대값을 출력


### 에라토스테네스의 체를 이용했다
### 사실 많이 들어본 거긴하지만 실제로 구현 해본 것은 처음

### 어떤 경우에서 합이 소수인지 확인하는게 prime 리스트에서 찾는 것보다 그 p_list 인덱스를 넣어서 찾는게 더 빠름

import sys
input = sys.stdin.readline

num = 10000001

#### 소수 리스트를 에라토스테네스의 체를 이용해서 만듬
plist = [1] * num
plist[0] = 0
plist[1] = 0
prime = []
for i in range(num):
    if plist[i]:
        prime.append(i)
        for j in range(2*i,num,i):
            plist[j] = 0




TC = int(input())
for T in range(1,TC+1):
    m = int(input())
    arr = list(map(int,input().split()))

    ### 각각의 소수들의 개수를 준것들의 범위를 설정해주는 리스트
    ans = [[0,i-1] for i in arr]

    ### 각각의 경우에서 합을 구하는 리스트
    mys = [0] * m
    

    ### 처음 소수들의 합을 구하는 리스트
    for i in range(m):
        time = 1
        mys[i] = sum(prime[ans[i][0]:ans[i][1]+1])
        while not plist[mys[i]]:
            mys[i] = mys[i] + prime[ans[i][1]+1] - prime[ans[i][0]]
            ans[i] = [ans[i][0]+1,ans[i][1]+1]

    ### 그리고 비교할 max 값
    mx = max(mys)

    ### 어떤 경우를 구할 result 인덱스
    result = 0  



    while result < m:
        mx = max(mys)

        ### 최대값과 어떤 경우가 같을 경우는 다음 경우를 설정
        if mys[result] == mx:
            result += 1

        ### 최대값보다 작다면 최대값보다 같거나 클때까지 계속함
        elif mys[result] < mx:


            ### 슬라이딩 윈도우를 이용해 다음 값을 계산하고
            while mys[result] < mx:
                mys[result] = mys[result] - prime[ans[result][0]] + prime[ans[result][1]+1]
                ans[result] = [ans[result][0]+1,ans[result][1]+1]


            ### 소수가 아닐 경우에 계속해서 계산
                while not plist[mys[result]]:
                    mys[result] = mys[result] - prime[ans[result][0]] + prime[ans[result][1]+1]
                    ans[result] = [ans[result][0]+1,ans[result][1]+1]


            ### 만약에 구한 값이 mx 랑 같다면 다음 경우를 생각
            if mys[result] == mx:
                result += 1


            ### 최대값보다 더 크다면 그 값을 최대값으로 설정, 처음부터 다시 검사함
            elif mys[result] > mx:
                result = 0

                mx = mys[result]


    print(f"Scenario {T}:")
    print(mys[0])
    print()