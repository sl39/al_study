## D가 나왔을 때 D의 앞의 R의 개수가 짝수이면 배열을 돌릴 필요가 없으므로 맨앞의 수를 제거
## 홀수이면 배열을 돌려야 하므로 맨뒤의 수를 제거


import sys
from collections import deque   #popleft()의 속도를 위해 가져옴
input_ = sys.stdin.readline
TC = int(input_())
for _ in range(TC):
    p = input_().rstrip()
    n = int(input_())
    if n == 0 :                 #n = 0 일땐 nx = []로 받고
        input_()
        nx = []
    else:
        nx = list(map(int,input_().replace("[","").replace("]","").split(","))) #아닐땐 그냥 받음
    nx = deque(nx)              #deque를 이용해서 nx에 저장
    cnt = 0                     #R의 개수를 세기 위한 cnt 설정
    for j in p:
        if j == "R":            #R이면 cnt +1 
            cnt += 1
        else:
            if nx:
                if cnt%2 == 0:      ## D가 나왔을 때 D의 앞의 R의 개수가 짝수이면 배열을 돌릴 필요가 없으므로 맨앞의 수를 제거
                    nx.popleft()
                else:
                    nx.pop()       ## 홀수이면 배열을 돌려야 하므로 맨뒤의 수를 제거
            else:
                print("error")     ## nx가 비어있는데 D가 나오면 error를 출력 하고  break
                cnt = -1
                break
    l_t = len(nx)
    if cnt < 0:                     ## 하나의 testcase가 끝나야 되는데 내 생각으로는 이렇게 벗어나면 될 거라고 생각함
        pass
    elif l_t == 0:                  ## nx의 길이가 0 이면 []를 출력
        print("[]")
    elif cnt%2 == 0:                    ##최종 R의 개수가 짝수개이면 그냥 그대로 출력
        st = "[" + str(nx[0])
        for i in range(1,l_t):
            st = st + ","+str(nx[i])
        print(st+"]")
    else:
        st = "[" + str(nx[l_t-1])       ## 홀수이면 뒤집어서 출력
        for i in range(l_t-2,-1,-1):
            st = st + ","+str(nx[i])
        print(st+"]")
