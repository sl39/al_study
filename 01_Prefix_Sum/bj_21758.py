import sys
input = sys.stdin.readline
N = int(input())
mys = list(map(int,input().split()))
msr = [0] * (N-2)
ms = sum(mys)
msr[0] = 2* (ms-mys[0]-mys[1]) # 왼쪽에서 시작할 때는 두마리의 꿀벌이 첫번쨰와 두번째자리를 차지하므로 전체합에서 그 2자리를 빼고 2배를 함
ans = msr[0]                   # ans 를 msr의 처음 수를 지정
for i in range(1,N-2):         # 마지막 자리에서는 꿀통을 넣는게 최대이므로 마지막 꿀통자리를 제외함
    msr[i] = msr[i-1] -2*mys[i+1] + mys[i]          # 첫번째 자리와 마지막 꿀통자리를 제외하고 나머지 꿀벌 하나를 움직임, 꿀벌 자리의 꿀수를 2곱해서 빼주고 바로 그 전 자리는 하나만 더 해줌
    ans = max(ans,msr[i])

msl = [0] *(N-2)
msl[0] = 2* (ms-mys[-1]-mys[-2])                #반대쪽으로 가는것도 마찬가지로 생각함
ans = max(msl[0],ans)
for i in range(1,N-2):                              #꿀벌이 양쪽 끝에 있고 꿀통이 그 사이에 있을 경우는
    msl[i] = msl[i-1] -2*mys[N-i-2] + mys[N-i-1]    #전체 합에서 양쪽 끝을 빼주고 꿀통에 있는 자리를 한번 더 더해줌
    ans = max(ans,msl[i])
mids = ms - mys[0] - mys[-1] + max(mys[1:N])
ans = max(ans,mids)

print(ans)